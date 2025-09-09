import pandas as pd
from openai import OpenAI

import os
from dotenv import load_dotenv
load_dotenv("../.env")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Crear una base de datos SQLite en memoria y una tabla de ejemplo
df = pd.read_csv("ventas.csv")

# Pasamos el DF a JSON para que el agente pueda interpretarlo mejor
contexto = df.to_json(orient="records")

# Configurar el LLM
llm = OpenAI()

prompt = f"""Dame todas las ventas del producto Camisa 
{contexto}
"""

# Preguntas en Lenguaje Natural
resp = llm.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
print(resp.choices[0].message.content)