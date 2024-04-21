# processors.py
import os

from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


class Tokenizer:
    def process(self, file_paths):
        """Simulate tokenization of input data."""
        # return data.split()
        # # Read documents
        docs = []
        for file_path in file_paths:
            loader = UnstructuredMarkdownLoader(str(file_path))
            docs.extend(loader.load())

        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )
        splits = text_splitter.split_documents(docs)
        return splits


class Vectorizer:
    def process(self, tokens):
        """Simulate converting tokens to a vector (dummy implementation)."""
        # This is a placeholder for actual vectorization logic.
        embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
        return embeddings
