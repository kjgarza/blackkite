import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain_core.documents import Document
from pymongo import MongoClient

from processors import Vectorizer


class VectorDBDAO:
    def __init__(self, uri: str):
        """Initialize the MongoDB client."""
        # self.client = MongoClient(uri)
        # self.db = self.client["vector_database"]  # Your DB name here
        # self.collection = self.db["vectors"]  # Your collection name here
        self.client = MongoClient(os.environ["MONGO_CONN_STRING"])
        self.db = self.client[os.environ["DB_NAME"]]
        self.collection = self.db[os.environ["COLLECTION_NAME"]]
        self.index_name = os.environ["INDEX_NAME"]

        # # Reset w/out deleting the Search Index
        # self.collection.delete_many({})

    def create_db_if_not_exists(self):
        """Creates the database if it does not already exist."""
        if self.db not in self.client.list_database_names():
            print("Database does not exist. Creating now...")
            self.db = self.client[os.environ["DB_NAME"]]
        else:
            print("Database already exists.")

    def insert_vectors(self, splits: list[Document], embeddings: OpenAIEmbeddings):
        MongoDBAtlasVectorSearch.from_documents(
            splits,
            embeddings,
            collection=self.collection,
            index_name=self.index_name,
        )
        # return True
        self.close()

    def query(self, query, K=2):
        self.vectorizer = Vectorizer()
        embeddings = self.vectorizer.process()
        vectorStore = MongoDBAtlasVectorSearch(
            self.collection, embeddings, index_name=self.index_name
        )
        print(query)
        docs = vectorStore.max_marginal_relevance_search(query, K=K)
        print(docs)
        return docs

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
