# commands.py
import os

from ingestion_service import IngestionService
from vector_db_dao import VectorDBDAO


class IngestDataCommand:
    def __init__(self, path: str):
        # self.filename = filename
        self.path = path
        self.ingestion_service = IngestionService()

    # def execute(self):
    #     if not os.path.exists(self.filename):
    #         print(f"Error: File '{self.filename}' not found.")
    #         return

    #     with open(self.filename, "r") as file:
    #         data = file.read()

    #     print("Ingesting data...")
    #     self.ingestion_service.ingest(data)
    #     print("Data ingestion complete.")

    def execute(self):
        if not os.path.exists(self.path):
            print(f"Error: Path '{self.path}' not found.")
            return

        # data = ""
        # for root, _, files in os.walk(self.path):
        #     for file in files:
        #         with open(os.path.join(root, file), "r") as f:
        #             data += f.read()

        file_paths = []
        for root, _, files in os.walk(self.path):
            for file in files:
                file_paths.append(os.path.join(root, file))

        print("Ingesting data...")
        print(file_paths)
        self.ingestion_service.ingest(file_paths)
        print("Data ingestion complete.")


class QueryDataCommand:
    def __init__(self, query: str):
        self.query = query
        self.vectorStore = VectorDBDAO(os.environ["MONGO_CONN_STRING"])

    def execute(self):
        print("Querying data...")
        docs = self.vectorStore.query(self.query)
        print(docs[0].metadata["title"])
        print(docs[0].page_content)
        print("Query complete.")
