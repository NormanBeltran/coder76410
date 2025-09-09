import pandas as pd

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage

import matplotlib.pyplot as plt

import os

# Asegúrate de tener la API Key en variable de entorno
# Windows PowerShell: setx OPENAI_API_KEY "tu_api_key_aqui"

import os
from dotenv import load_dotenv
load_dotenv("../.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Cargar CSV
df = pd.read_csv("ventas1.csv")

def pregunta_csv(pregunta: str):
    data_str = df.to_json
    print(data_str)
    # Template del prompt
    template = """
    Eres un asistente experto en análisis de datos. Te doy un JSON con la información:

    {data_str}

    Responde la siguiente pregunta de manera clara y concreta:
    {pregunta}
    """

    prompt = PromptTemplate(input_variables=["data", "pregunta"], template=template)

    # Crear LLM
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)

    # Ejecutar prompt
    respuesta = llm.invoke([HumanMessage(content=template)])
    return respuesta

def grafico_ventas_por_producto():
    df_grouped = df.groupby("Producto")["Cantidad"].sum()
    df_grouped.plot(kind="bar", color="skyblue")
    plt.title("Ventas Totales por Producto")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print(pregunta_csv("¿Cuál es el producto más vendido?"))
    grafico_ventas_por_producto()
