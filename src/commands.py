# commands.py
import os

from ingestion_service import IngestionService


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
