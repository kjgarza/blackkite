# ingestion_service.py
from processing_pipeline import ProcessingPipeline


class IngestionService:
    def __init__(self):
        # Initialize any necessary components or services here,
        # For example, a logger or a database connection if needed.
        pass

    def ingest(self, data: list[str]):
        """
        Process the data received from the CLI.

        Args:
            data (str): The raw data from a file as a string.
        """
        print("Starting to process data...")
        processed_data = self.preprocess(data)
        self.send_to_pipeline(processed_data)
        print("Data sent to the processing pipeline.")

    def preprocess(self, data):
        """
        Preprocess the data, for instance, converting to lowercase,
        removing special characters, etc.

        Args:
            data (str): The raw text data to preprocess.

        Returns:
            str: The preprocessed data.
        """
        # Example preprocessing: convert to lowercase
        return data

    def send_to_pipeline(self, processed_data):
        """
        Placeholder method to simulate sending data to the processing pipeline.
        In a real implementation, this would handle interfacing with the actual
        data processing components.

        Args:
            processed_data (str): The processed data ready for further 
            processing.
        """
        pp = ProcessingPipeline()
        processed_data = pp.process(processed_data)
        print("Processing data:", processed_data)
        pp.store()
        print("Stored data:", processed_data)
