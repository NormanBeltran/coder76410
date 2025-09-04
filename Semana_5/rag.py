import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

# 1. Cargar los documentos (puede ser desde archivos locales, bases de datos, pdf, excel,etc.)

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import UnstructuredExcelLoader

from langchain.text_splitter import CharacterTextSplitter

#loader = PyPDFLoader("./El_espejo.pdf")
#loader = TextLoader("./cuento.txt", encoding="utf-8")
loader = UnstructuredExcelLoader("ventas_juguetes.xlsx", mode="elements")

docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separator="\n")
docs_chunked = text_splitter.split_documents(docs)

print(f"Fragmentos creados a partir del documento : {len(docs_chunked)}")

# 2. Crear los embeddings (vectores) de los documentos para cada fragmento e indexarlos en una base de datos vectorial
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
vectorstore = FAISS.from_documents(docs_chunked, embeddings)

print(f"Vector Store creado con {vectorstore.index.ntotal} vectores")

# 3. Configurar el modelo de lenguaje y la cadena de Q&A con recuperación
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA

# Inicializar el modelo de lenguaje 
llm = OpenAI(temperature=0.0)

# Crear la cadena de QA con recuperación indicando la base de datos vectorial y el LLM
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# 4. Realizar consultas al modelo con contexto

while True:
    query = input("Ingrese su pregunta (o 'salir' para terminar): ")
    if query.lower() == 'salir':
        break
    response = qa_chain.invoke(query)
    print(f"Respuesta: {response['result']}\n")

print("Fin de Programa")    
