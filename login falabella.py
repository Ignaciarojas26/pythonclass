print("----------Bienvenido a Falabella----------")

# validacion rut

while True:

    rut = input("Ingresa tu RUT(Sin punto ni guion)")

    if rut.isdigit() and len(rut) ==8: 
        break

    else:
        print("El RUT solo debe tener 8 digitos")

# valida codigo de verificacion

while True:

    dv = input("Ingresa tu digito verificador: ").upper()


    if len(dv) == 1 and (dv.isdigit() or dv == "K"):
        break

else:
    print("Error")

# nombre

nombre = input("Ingresa tu nombre: ")

#Valida compra 

while True:

    monto = input("Ingresa el monto de la compra: ")

    if monto.isdigit():

        monto = int(monto)

        if monto >=0:
            break
        
        else:
            print("Error, el monto es negativo")
    
    else:
        print("Error ingresa un solo numero")

#Imgresa el descuento

if monto < 10000:
    descuento = 0
    porcentaje = 0

elif monto <= 50000:
    descuento = monto *0.10
    porcentaje = 10

else:

    descuento = monto *0.20
    porcentaje = 20

total = monto - descuento 

# boleta

print("\n----------Boleta----------")

print(f"Rut: {rut}-{dv}")

print(f"Nombre: {nombre}")

print(f"Monto: {monto}")

print(f"Descuento: {descuento}")

print(f"El total a pagar es: {total}")




 

