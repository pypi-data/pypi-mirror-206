# %%
import requests
import os
import json
import dotenv
import logging
from typing import Optional
from base64 import urlsafe_b64encode
from hashlib import sha1
from urllib.parse import urlsplit
import pandas as pd
import pyodbc

from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
from azure.data.tables import TableServiceClient, UpdateMode
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy, BinaryBase64DecodePolicy

requests.packages.urllib3.disable_warnings()  # type: ignore

logger = logging.getLogger("logger_name")
logger.disabled = True

dotenv.load_dotenv('.env')
if not os.environ.get('CONNECTION_STRING'):
    logging.error(f"{os.environ.get('CONNECTION_STRING')=}")


def make_id(text):
    """ generate unique id from text (str or bytes) """
    source = text.encode('utf-8') if isinstance(text, str) else text
    return urlsafe_b64encode(sha1(source).digest()).decode('utf-8')


class BlobApi:
    def __init__(self, container_name: str, folder: Optional[str]):
        self.container_name = container_name
        self.folder = folder

    def list_items_blob(self):
        container_client = ContainerClient.from_connection_string(str(os.environ.get('CONNECTION_STRING')),
                                                                  self.container_name, logger=logger)
        if self.folder:
            blob_list = container_client.list_blobs(name_starts_with=self.folder, include=['metadata'])
        else:
            blob_list = container_client.list_blobs(include=['metadata'])
        blob_list = [i for i in blob_list]
        return blob_list

    def write_to_blob(self, path: str, output, overwrite=True):
        blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=str(os.environ.get('CONNECTION_STRING')), logger=logger)

        container_check = ContainerClient.from_connection_string(str(os.environ.get('CONNECTION_STRING')),
                                                                 self.container_name, logger=logger)
        if not container_check.exists():
            # create_container gives a container client, but we don't need it
            _ = blob_service_client.create_container(self.container_name)

        if '.' not in path:
            logging.error('Please include file type in path!')
            raise

        if self.folder is not None:
            save_path = f'{self.folder}/{path}'
        else:
            save_path = path
        blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=save_path)
        blob_client.upload_blob(output, overwrite=overwrite)

    def download_from_blob(self, path: str, object_hook=None) -> dict:
        # TODO: maak class variables
        blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=str(os.environ.get('CONNECTION_STRING')), logger=logger)
        blob_client = blob_service_client.get_container_client(container=self.container_name)

        if self.folder is not None:
            download_path = f'{self.folder}/{path}'
        else:
            download_path = path
        if object_hook is None:
            json_results = json.loads(blob_client.download_blob(download_path).readall())
        else:
            json_results = json.loads(blob_client.download_blob(download_path).readall(), object_hook=object_hook)

        return json_results

    def read_from_blob(self, path: str) -> bytes:
        if self.folder is not None:
            download_path = f'{self.folder}/{path}'
        else:
            download_path = path

        blob_client = BlobClient.from_connection_string(
            conn_str=os.environ.get('CONNECTION_STRING'),
            container_name=self.container_name,
            blob_name=download_path,
            logger=logger
        )

        return blob_client.download_blob().readall()

    def delete_blob(self, filepath: str):
        blob_client = BlobClient.from_connection_string(
            conn_str=os.environ.get('CONNECTION_STRING'),
            container_name=self.container_name,
            blob_name=filepath,
            logger=logger
        )

        return blob_client.delete_blob()


class TableApi:
    def __init__(self):
        self.table_service_client = TableServiceClient.from_connection_string(str(os.environ.get('CONNECTION_STRING')),
                                                                              logger=logger)

    def create_entity(self, table_name: str, entity: dict):
        table_client = self.table_service_client.get_table_client(table_name=table_name, logger=logger)
        # create_entity returns the entity, but we don't need it
        _ = table_client.create_entity(entity=entity)

    def update_entity(self, table_name: str, entity: dict):
        table_client = self.table_service_client.get_table_client(table_name=table_name, logger=logger)
        table_client.update_entity(mode=UpdateMode.MERGE, entity=entity)

    def querying_entities(self, table_name: str, my_filter: str):
        table_client = self.table_service_client.get_table_client(table_name=table_name, logger=logger)
        entities = table_client.query_entities(my_filter)
        records = [entity for entity in entities]
        return records

    def remove_entity(self, table_name: str, partion: str, key: str):
        table_client = self.table_service_client.get_table_client(table_name=table_name, logger=logger)
        table_client.delete_entity(partition_key=partion, row_key=key)


class QueueApi:
    def __init__(self, q_name) -> None:
        self.q_name = q_name
        self.queue_client = QueueClient.from_connection_string(
            str(os.environ.get('CONNECTION_STRING')),
            self.q_name,
            message_encode_policy=BinaryBase64EncodePolicy(),
            message_decode_policy=BinaryBase64DecodePolicy(),
            logger=logger)

    def peek_at_messages(self):
        messages = self.queue_client.peek_messages(max_messages=32)
        messages = [json.loads(m['content']) for m in messages]
        return messages

    def send_message(self, message):
        message = json.dumps(message).encode()
        self.queue_client.send_message(message)

class SQLApi:
    def connect_to_db():
        server_name = os.environ.get('SERVER_NAME')
        database_name = os.environ.get('DB_NAME')
        username = os.environ.get('USERNAME_DB')
        password = os.environ.get('PASSWORD_DB')

        cnxn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};" 
            f"Server={server_name};" 
            f"Database={database_name};"
            f"Uid={username};"
            f"Pwd={password};"
            )
        cursor = cnxn.cursor() 

        return cursor

    cursor = connect_to_db()

    def get_data_from_db(query):
        data = pd.read_sql(query, cursor.connection)
        return data

    def add_data_to_table(df: pd.DataFrame, table_name: str) -> None:
        df.to_sql(table_name, cursor.connection, if_exists='append', index=False)
        
def on_black_list(url) -> list:
    # Not pulling this out into a global variable: this list is only used here.
    # save this for later         ".gov", "google", ".edu", ".org", ".edu",
    block_list = [
        'linkedin', 'twitter', 'facebook', 'instagram', 'tiktok', 'pinterest', 'fandom', 'youtu',
        'amazon.com',
        '.pdf', '.doc', '.docx', '.txt', '.csv', '.png', '.xlsx', '.xls', '.odt', '.ods', '.ppt', '.pptx',
        'google','msn', 'yahoo',  
        'times.', 'springer', 'media', 'telegraph', 'news', 'magazin', 'medium.com', 'daily'
        'research', 'investopedia', 'wikipedia', 'sciencedirect', 'tandfonline'
    ]
    return any(y in url for y in block_list)

def extract_base_url(url):
    parsed_url = urlsplit(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return base_url
