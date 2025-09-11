import pandas as pd
import google.generativeai as genai
import matplotlib.pyplot as plt
import io

# Configura tu clave de API de Gemini
import os
from dotenv import load_dotenv

load_dotenv("../.env")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Crea una instancia del modelo Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

# Lee el archivo CSV
try:
    df = pd.read_csv('ventas.csv')
    print("DataFrame cargado exitosamente:\n", df)
except FileNotFoundError:
    print("Error: El archivo 'ventas.csv' no fue encontrado.")
    exit()

def generate_bar_chart(data, title, x_label, y_label):
    """
    Genera y guarda un gráfico de barras en un archivo temporal.
    """
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar', x=x_label, y=y_label, legend=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Guarda el gráfico en un buffer en memoria
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def ask_gemini_about_data(query, dataframe):
    # Convierte el DataFrame a formato de cadena (por ejemplo, Markdown)
    df_markdown = dataframe.to_markdown(index=False)
    
    # Construye el prompt para Gemini
    prompt = f"""
    Eres un experto en análisis de datos. Tienes un set de datos de ventas de productos por mes.
    El set de datos es el siguiente:
    {df_markdown}
    
    Pregunta del usuario: {query}
    
    Responde la pregunta. Si la pregunta solicita una visualización o un gráfico, confirma que harás una, pero NO generes el gráfico en tu respuesta. Simplemente di "Generando gráfico..."
    """
    
    # Envía el prompt a Gemini
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    print("¡Bienvenido! Puedes preguntar sobre el set de datos de ventas.")
    print("Ejemplos: '¿Cuál fue el total de ventas en marzo?', 'Muestra las ventas de pantalones en un gráfico de barras.'")
    print("Escribe 'salir' para terminar.")
    
    while True:
        user_query = input("\nTu pregunta: ")
        if user_query.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        # Primero, pide a Gemini que analice la pregunta
        response_text = ask_gemini_about_data(user_query, df)
        print("\nRespuesta de Gemini:")
        print(response_text)
        
        # Detecta si Gemini sugirió un gráfico
        if "generando gráfico" in response_text.lower():
            try:
                # Si es una pregunta sobre productos
                if "producto" in user_query.lower():
                    # Agrupa los datos por producto para el gráfico
                    product_summary = df.groupby('producto')['ventas'].sum()
                    chart_data = pd.DataFrame({'producto': product_summary.index, 'ventas': product_summary.values})
                    chart_buffer = generate_bar_chart(chart_data, 'Ventas Totales por Producto', 'producto', 'ventas')
                    
                    # Guarda el gráfico en un archivo local
                    with open("ventas_por_producto.png", "wb") as f:
                        f.write(chart_buffer.getbuffer())
                    print("Gráfico generado y guardado como 'ventas_por_producto.png'.")
                
                # Si es una pregunta sobre meses
                elif "mes" in user_query.lower():
                    # Agrupa los datos por mes para el gráfico
                    month_summary = df.groupby('mes')['ventas'].sum()
                    chart_data = pd.DataFrame({'mes': month_summary.index, 'ventas': month_summary.values})
                    chart_buffer = generate_bar_chart(chart_data, 'Ventas Totales por Mes', 'mes', 'ventas')
                    
                    # Guarda el gráfico en un archivo local
                    with open("ventas_por_mes.png", "wb") as f:
                        f.write(chart_buffer.getbuffer())
                    print("Gráfico generado y guardado como 'ventas_por_mes.png'.")
                        
            except Exception as e:
                print(f"Ocurrió un error al generar el gráfico: {e}")