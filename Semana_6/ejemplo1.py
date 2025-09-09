import pandas as pd
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase

import os
from dotenv import load_dotenv
load_dotenv("../.env")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Crear una base de datos SQLite en memoria y una tabla de ejemplo
df = pd.read_csv("ventas.csv")

engine = create_engine("sqlite:///:memory:", echo=False)

df.to_sql("ventas", con=engine, if_exists="replace", index=False)
db = SQLDatabase(engine)

# Configurar el LLM
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# Crar la cadena de consulta SQL
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Realizar una consulta
while True:
    query = input("¿Cuál es su consulta? (escriba 'salir' para terminar) ")
    if query.lower() == "salir":
        break
    print(db_chain.run(query))