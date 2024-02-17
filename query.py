import argparse
import warnings

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient

import params

# Filter out the UserWarning from langchain
warnings.filterwarnings('ignore', category=UserWarning, module='langchain.chains.llm')

# Process arguments
parser = argparse.ArgumentParser(description='Atlas Vector Search Demo')
parser.add_argument('-q', '--question', help='The question to ask')
args = parser.parse_args()

if args.question is None:
    # Some questions to try...
    query = 'How big is the telecom company?'
    query = 'Who started AT&T?'
#    #query = "Where is AT&T based?"
#    #query = "What venues are AT&T branded?"
#    #query = "How big is BofA?"
#    #query = "When was the financial institution started?"
#    #query = "Does the bank have an investment arm?"
#    #query = "Where does the bank's revenue come from?"
#    #query = "Tell me about charity."
#    #query = "What buildings are BofA branded?"

else:
    query = args.question

print('\nYour question:')
print('-------------')
print(query)

# Initialize MongoDB python client
client = MongoClient(params.mongodb_conn_string)
collection = client[params.db_name][params.collection_name]

# initialize vector store
vectorStore = MongoDBAtlasVectorSearch(
    collection, OpenAIEmbeddings(openai_api_key=params.openai_api_key), index_name=params.index_name
)

# perform a similarity search between the embedding of the query and the embeddings of the documents
# print("\nQuery Response:")
print('---------------')
docs = vectorStore.max_marginal_relevance_search(query, K=1)

print(docs[0].metadata['title'])
print(docs[0].page_content)

# Contextual Compression
llm = OpenAI(openai_api_key=params.openai_api_key, temperature=0)
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorStore.as_retriever()
)

print('\nAI Response:')
print('-----------')
compressed_docs = compression_retriever.get_relevant_documents(query)
print(compressed_docs[0].metadata['title'])
print(compressed_docs[0].page_content)
