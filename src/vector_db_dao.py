import os

from langchain.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient


class VectorDBDAO:
    def __init__(self, uri):
        """Initialize the MongoDB client."""
        # self.client = MongoClient(uri)
        # self.db = self.client["vector_database"]  # Your DB name here
        # self.collection = self.db["vectors"]  # Your collection name here
        self.client = MongoClient(os.environ["MONGO_CONN_STRING"])
        self.collection = self.client[os.environ["DB_NAME"]][
            os.environ["COLLECTION_NAME"]
        ]
        self.index_name = os.environ["INDEX_NAME"]

        # # Reset w/out deleting the Search Index
        self.collection.delete_many({})

    def insert_vectors(self, splits, embeddings):
        MongoDBAtlasVectorSearch.from_documents(
            splits,
            embeddings,
            collection=self.collection,
            index_name=self.index_name,
        )
        # return True
        self.close()

    # def insert_vector(self, vector_data):
    #     """Inserts vector data into MongoDB."""
    #     result = self.collection.insert_one(vector_data)
    #     print("Inserted Vector with ID:", result.inserted_id)
    #     return result.inserted_id

    # def get_vector_by_id(self, vector_id):
    #     """Retrieves a vector by its MongoDB ObjectId."""
    #     result = self.collection.find_one({"_id": ObjectId(vector_id)})
    #     return result

    def close(self):
        """Close the MongoDB connection."""
        self.client.close()
