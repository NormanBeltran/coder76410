import pandas as pd
import os
import google.generativeai as genai

from dotenv import load_dotenv

# Load environment variables from the .env file.
load_dotenv()

# Configure the API key for the generative AI.
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create an instance of the GenerativeModel.
# The model name is specified in the generate_content call.
model = genai.GenerativeModel("gemini-1.5-flash")

# 1. Create a sample product review dataframe.
data = {
    "producto": ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E", "Producto F"],
    "reseña": [
        "Me encanta este producto, es justo lo que necesitaba.",
        "No estoy satisfecho con la calidad, esperaba más.",
        "Excelente relación calidad-precio, lo recomiendo.",
        "El producto llegó dañado, muy decepcionado.",
        "Buena calidad, pero el envío fue lento.",
        "Me gusta, pero el precio es un poco alto."
    ]
}

df = pd.DataFrame(data)

# 2. Define the function to analyze reviews.
def analizar_resenas(resenas):
    prompt = f"""
    Clasifica el siguiente texto con solo una de estas palabras: 'positivo', 'negativo' o 'neutro'.
    Texto: {resenas}
    """
    try:
        # Use the generate_content method to get the sentiment.
        response = model.generate_content(prompt)
        sentimiento = response.text.strip().lower()
        return sentimiento
    except Exception as e:
        print(f"Error al analizar la reseña: {e}")
        return "error"

# 3. Apply the function to each review and add the result to the dataframe.
df["sentimiento"] = df["reseña"].apply(analizar_resenas)

# 4. Show the resulting dataframe.
print(df)

# 5. Simple count of each sentiment category.
conteo_sentimientos = df["sentimiento"].value_counts()
print("\nConteo de sentimientos:")
print(conteo_sentimientos)
