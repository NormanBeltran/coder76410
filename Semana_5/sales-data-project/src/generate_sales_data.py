import pandas as pd
import random

# Definir los nombres de los juguetes
toys = [f"Juguete {i+1}" for i in range(20)]

# Definir los meses de la venta
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
          "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Generar datos aleatorios
data = {
    "Juguete": [],
    "Mes de la Venta": [],
    "Cantidad de juguetes vendidos": [],
    "Monto total de la venta": []
}

for toy in toys:
    for month in months:
        quantity_sold = random.randint(1, 100)  # Cantidad entre 1 y 100
        total_amount = quantity_sold * random.uniform(5.0, 50.0)  # Monto total entre 5 y 50 por juguete
        data["Juguete"].append(toy)
        data["Mes de la Venta"].append(month)
        data["Cantidad de juguetes vendidos"].append(quantity_sold)
        data["Monto total de la venta"].append(round(total_amount, 2))

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_excel("ventas_juguetes.xlsx", index=False)