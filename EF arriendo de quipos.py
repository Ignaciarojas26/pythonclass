#nombre
while True:

    nombre = input("Para empezar, por favor, introduzca su nombre: ")
    if len(nombre) >=3 and nombre.isalpha():
        break
    else: 
        print("Debes ingresar minimo 3 caracteres, sin numeros o espacios")

#telefono
while True:
    telefono = input("\n Ingrese su número de teléfono: ")
    if telefono.isdigit() and (len(telefono) == 8 or len(telefono) == 9):
        break
    else: 
        print("El numero de telefono debe contener entre 8 a 9 digitos")

#horas de trabajo y validacion de que sea numero
horas = input("¿Por cuantas horas necesitas la maquinaria?: ")
if horas.isdigit():
    horas= int(horas)
    

else:
    print("Error, ingrese un numero valido")


#tipo de equipo

print("\n ------Catalogo------")
print("-Excavadora: $200.000")
print("-Grua: $250.000")
print("-Mezcladora: $150.000")

while True:
    equipo = input("Ingrese el equipo que necesita: ").lower().strip()

    if equipo == "excavadora" or equipo == "Excavadora":
        precio_hora = 200000
        break
    elif equipo == "grua" or equipo == "Grúa":
        precio_hora = 250000
    elif equipo == "mezcladora" or equipo == "Mezcladora":
        precio_hora = 150000
        break
    else:
        print("Equipo no valido, intente nuevamente")

total = horas * precio_hora

#salida

print("\n ----------BOLETA DE ARRIENDO----------")
print(f"Nombre:         {nombre}")
print(f"Telefono:       {telefono}")
print(f"Equipo:         {equipo}")
print(f"Total de horas: {horas}")
print("\n --------------------------------------")
print(f"Total a pagar: ${total:,}")
print("\n --------------------------------------")





