print("----------Tienda Retail----------")

while True:
    nombre = input("Ingrese su nombre: ")

    if len(nombre) >=3 and nombre.isalpha():
        break

    else:
        print("Debes ingresar minimo 3 caracteres, sin numeros o espacios")

#monto

while True:
    monto = input("Ingrese el monto de compra: ")
    if monto.isdigit():
        monto = int(monto)
        if monto >=0:
            break

        else:
            print("Error, el monto no puede ser negativo")
        
    else:
        print("Error, intentalo nuevamente")

#descuento


if monto < 10000:
    porcentaje = 0
    descuento = 0
elif monto <= 50000:
    porcentaje = 10
    descuento = monto * 0.10
else: 
    porcentaje = 20
    descuento = monto * 0.20


descuento = monto * (porcentaje / 100)
total = monto - descuento

print(f"Tu monto a pagar es: {total}")

    