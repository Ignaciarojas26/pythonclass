print("="*25)
print("     Tienda de armas")
print("="*25)

#identificacion usuario
while True:
    nombre = input("Para iniciar su pedido ingrese su nombre o usuario: ").strip()
    if len(nombre) >=3 and nombre.isalpha():
        break
    else:
        print("Nombre o usuario no valido, necesita minimo 3 caracteres")

while True:
    rut = input("Ingrese su RUT sin digito verificador: ")
    dv = input("Ingrese su dígito verificador: ").upper()
    if dv == "K" or (dv.isdigit() and 0 <= int(dv) <= 9):
        break
    else:
        print("Error, vuelve a intentarlo de nuevo")

print("\n ¡Recuerda tenemos el 10% de descuento en compras sobre $15.000")

print("\n" + "="*25)
print("     Armas disponibles      ")
print("="*25)
print("Espada: $5.000")
print("Arco: $7.000")
print("Baston magico: $9.000")


#carrito
subtotal = 0
index_productos = []
while True:
    arma = input("Ingresa el arma que deseas comprar (o escribe 'salir' para pagar): ").lower().strip()

    if arma == "salir" or arma == "pagar":
        break

    elif arma == "espada":
        subtotal += 5000
        index_productos.append("Espada ($5.000)")
        print("¡Agregaste Espada a tu carrito!")

    elif arma == "arco":
        subtotal += 7000
        index_productos.append("Arco ($7.000)")
        print("¡Agregaste Arco a tu carrito!")

    elif arma == "baston magico" or arma == "baston":
        subtotal += 9000
        index_productos.append("Baston magico ($9.000)")
        print("¡Agregaste Baston magico a tu carrito!")

    else:
        print("Opcion no valida. Por favor elige una de la lista")

#descuentos
descuento = 0
if subtotal > 15000:
    descuento = int(subtotal *0.10)

total = subtotal - descuento

#boleta
print("\n" + "="*30)
print("         Boleta de venta         ")
print("="*30)
print(f"Cliente:    {nombre}")
print(f"RUT:    {rut}-{dv}")
print("-"*30)

print("Pruductos adquiridos: ")
if len(index_productos) == 0:
    print("No compraste ningun producto")
else:
    for item in index_productos:
        print(f" * {item}")
        
print(f"Subtotal:   ${subtotal:,}")
print("-"*30)
print(f"Total a pagar:  ${total:,}")
print("="*30)
print("¡Disfruta tu compra aventurero!")
