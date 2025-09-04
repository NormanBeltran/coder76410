import pandas as pd
import random

# Definir los nombres de los juguetes
toys = [f"Juguete {i+1}" for i in range(20)]

# Definir los meses de la venta
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
          "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Generar datos aleatorios
data = []
for toy in toys:
    for month in months:
        quantity_sold = random.randint(1, 100)  # Cantidad de juguetes vendidos
        total_amount = quantity_sold * random.uniform(5.0, 50.0)  # Monto total de la venta
        data.append([toy, month, quantity_sold, round(total_amount, 2)])

# Crear un DataFrame de pandas
df = pd.DataFrame(data, columns=["Juguete", "Mes de la Venta", "Cantidad de juguetes vendidos", "Monto total de la venta"])

# Guardar el DataFrame en un archivo Excel
df.to_excel("ventas_juguetes.xlsx", index=False)