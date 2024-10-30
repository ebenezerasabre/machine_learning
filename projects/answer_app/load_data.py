# will be used to load the documents and inject the text and vector embeddings
# in the mongodb collections

from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain.llms import openai
from langchain.chains import retrieval_qa
import gradio as gr # for creating frontend
from gradio.themes.base import Base
import key_param


# we are going to get sample documents
# we will load 3 text from our directory using DirectoryLoader


client = MongoClient(key_param.MONGO_URI)
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

loader = DirectoryLoader('./sample_files', glob="./*.txt", show_progress=True)
data = loader.load()

# create embeddings on mongo
embeddings = OpenAIEmbeddings(openai_api_key=key_param.openai_api_key)

# add embeddings to mongodb atlas
vectorStore = MongoDBAtlasVectorSearch.from_documents(data, embeddings, collection=collection )

#create search index on mongo



