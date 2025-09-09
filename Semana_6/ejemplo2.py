import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns

from langchain_openai import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

import os
from dotenv import load_dotenv
load_dotenv("../.env")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Crear una base de datos SQLite en memoria y una tabla de ejemplo
df = pd.read_csv("ventas.csv")


# Configurar el LLM
llm = OpenAI(temperature=0, model="gpt-4o-mini")

# Crar el agente de consulta de DataFrame
agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

# Preguntas en Lenguaje Natural
#query = "Dame todas las ventas del producto que comienza con la letra C"
#print(agent.run(query))

agent.run("import seaborn as sns")
agent.run("Dibuja un grafico de torta con el total de  las cantidades por producto")