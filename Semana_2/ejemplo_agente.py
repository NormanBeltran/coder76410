# Solicita 5 nombres al usuario y los almacena en una lista
nombres = []
for i in range(5):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    nombres.append(nombre)

# Ordena la lista alfabéticamente
nombres.sort()

# Muestra los nombres ordenados
print("Nombres ordenados alfabéticamente:")
for nombre in nombres:
    print(nombre)