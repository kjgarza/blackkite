# commands.py
import os

from ingestion_service import IngestionService
from vector_db_dao import VectorDBDAO


class IngestDataCommand:
    def __init__(self, filename):
        self.filename = filename
        self.ingestion_service = IngestionService()

    def execute(self):
        if not os.path.exists(self.filename):
            print(f"Error: File '{self.filename}' not found.")
            return

        with open(self.filename, "r") as file:
            data = file.read()

        print("Ingesting data...")
        self.ingestion_service.ingest(data)
        print("Data ingestion complete.")


class QueryDataCommand:
    def __init__(self, query):
        self.query = query
        self.vectorStore = VectorDBDAO(os.environ["MONGO_CONN_STRING"])

    def execute(self):
        print("Querying data...")
        docs = self.vectorStore.query(self.query)
        print(docs[0].metadata["title"])
        print(docs[0].page_content)
        print("Query complete.")
