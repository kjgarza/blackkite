# processing_pipeline.py
from processors import Tokenizer, Vectorizer
from vector_db_dao import VectorDBDAO
import os


class ProcessingPipeline:
    def __init__(self):
        # Initialize the processors to be used in the pipeline
        self.tokenizer = Tokenizer()
        self.vectorizer = Vectorizer()
        self.storage = VectorDBDAO(os.environ["MONGO_CONN_STRING"])

    def process(self, data: list[str]):
        """Process the data through all stages of the pipeline."""
        print("Starting the processing pipeline...")
        # Tokenization stage
        tokens = self.tokenizer.process(data)
        print("Tokenization complete:", tokens)
        self.splits = tokens

        # Vectorization stage
        self.embeddings = self.vectorizer.process()
        print("Vectorization complete:", self.embeddings)

        # Here you could add additional processing stages
        return self.embeddings

    def store(self):
        try:
            self.storage.insert_vectors(self.splits, self.embeddings)
            print("Data stored successfully.")
        except Exception as e:
            print("Error storing data:", str(e))


# Example usage within this module
if __name__ == "__main__":
    # Example data
    data = "Hello world! Processing pipeline test."
    pipeline = ProcessingPipeline()
    processed_data = pipeline.process([data])
    print("Processed data:", processed_data)
