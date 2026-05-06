from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3.2:3b")

client = chromadb.PersistentClient(path="D:\\chroma_project")
collection = client.get_or_create_collection(name="my_collection_01")

__loader__ = PyPDFLoader("D:\\chroma_project\\sample.pdf")
documents = __loader__.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
texts = text_splitter.split_documents(documents)

texts = [text.page_content for text in texts]

collection.add(documents=texts, ids=[f"doc{i}" for i in range(len(texts))])
print("Documents added to the collection.")
Query = ["How much is standalone revenue and profit?"]
results = collection.query(query_texts=Query, n_results=3)
print("Query_results:", results)
# Output should show the most relevant document based on the query
# Cleanup: Remove the collection after testing
#client.delete_collection(name="my_collection_01")
