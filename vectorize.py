
import os
import sys
from pathlib import Path  # used to manipulate file paths elegently

from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient

import params


def configure_retriever(file_paths):
    # Read documents
    docs = []
    for file_path in file_paths:
        loader = UnstructuredMarkdownLoader(str(file_path))
        docs.extend(loader.load())

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    # Create embeddings and store in vectordb
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])

    client = MongoClient(params.mongodb_conn_string)
    collection = client[os.environ['DB_NAME']][os.environ['COLLECTION_NAME']]

    # # Reset w/out deleting the Search Index
    collection.delete_many({})

    MongoDBAtlasVectorSearch.from_documents(
        splits, embeddings, collection=collection, index_name=os.environ['INDEX_NAME']
    )


def main():
    print('initiating DB index...')
    directory = sys.argv[1]

    print('digesting docs...')
    configure_retriever(list(Path(directory).glob('**/*.md')))


if __name__ == '__main__':
    main()
