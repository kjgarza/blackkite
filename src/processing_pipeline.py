# processing_pipeline.py
from processors import Tokenizer, Vectorizer
from vector_db_dao import VectorDBDAO


class ProcessingPipeline:
    def __init__(self):
        # Initialize the processors to be used in the pipeline
        self.tokenizer = Tokenizer()
        self.vectorizer = Vectorizer()
        self.storage = VectorDBDAO()

    def process(self, data):
        """Process the data through all stages of the pipeline."""
        print("Starting the processing pipeline...")
        # Tokenization stage
        tokens = self.tokenizer.process(data)
        print("Tokenization complete:", tokens)
        self.tokens = tokens

        # Vectorization stage
        self.vectors = self.vectorizer.process(tokens)
        print("Vectorization complete:", self.vectors)

        # Here you could add additional processing stages
        return self.vectors

    def store(self, tokens=[]):
        try:
            self.storage.insert_vectors(self.tokens, self.vectors)
            print("Data stored successfully.")
        except Exception as e:
            print("Error storing data:", str(e))


# Example usage within this module
if __name__ == "__main__":
    # Example data
    data = "Hello world! Processing pipeline test."
    pipeline = ProcessingPipeline()
    processed_data = pipeline.process(data)
    print("Processed data:", processed_data)
