print("\n" + "="*30)
print("Tienda insumos de pasteleria")
print("="*30)
#catalogo

print("\nCatalogo de insumos: ")
catalogo = {
    "Harina": 900,
    "Leche": 990,
    "Mantequilla": 2700,
    "Esencia de vainilla": 2500,
    "Chispas de chocolate": 4000,
    "Azucar": 1000,
    "Crema para batir": 5000,
    "Crema pastelera": 3800,
    "Merengue en polvo": 2700,
    "Gelatina sin sabor": 2500,
    "Chispas de arcoiris": 3100,  
}
#aqui se muestra el catalogo porque no salia
print("\n Catalogo de insumos disponibles: ")
for producto, precio in catalogo.items():
     print(f"-{producto}: ${precio}")
print("="*30)

#datos de usuario
while True:
    nombre = input("Para iniciar con su pedido ingrese su nombre: ")

    if len(nombre) >=3 and nombre.isalpha():
        break
    else:
        print("Error, debes ingresar minimo tres caracteres")

while True:
    rut = input("Ingrese su RUT (ej: 12345678-9): ").strip().upper()
    if 9 <= len(rut):
            break
    else:
        print("Erros ingrese un RUT valido")

while True: 
     direccion = input("Ingrese su direccion de envio: ").strip()
     if len(direccion) >= 5:
          break
     else:
          print("Error, Ingrese una direccion valida")

#carrito
carrito = []
total_venta = 0
contador = 0

while contador < 10:
     productos = input(f"Producto {contador + 1} (o escribe pagar): ").strip().capitalize()
#validador de carrito
     if productos == "Pagar":
          if len(carrito) > 0:
               break
          else:
               print("Debe ingresar al menos un producto para proceder a pagar")
          
     
     if productos in catalogo:
          precio = catalogo[productos]
          total_venta += precio
          carrito.append(productos)
          contador += 1
     else:
          print("Ese producto no esta disponible, intentalo nuevamente")

#calculo de iva
iva = total_venta * 0.19
descuento = 0 
if total_venta > 15000:
     descuento = total_venta * 0.10

#total 
pagar = total_venta + iva - descuento

#boleta
print("\n" + "="*30)
print("BOLETA ELECTRONICA")
print("\n" + "="*30)
print(f"Nombre: {nombre}")
print(f"Rut: {rut}")
print(f"Direccion: {direccion}")
print("-" *30)
print("Detalle de compra:")

for item in carrito:
     print(f"- {item:.<20} ${catalogo[item]:>8,}")

print("-" *30)
print(f"Subtotal Neto:      ${total_venta:>10,}")
print(f"IVA (19%):          ${iva:>10,}")
if descuento > 0:
    print(f"Descuento Aplicado: -${descuento:>9,}")
print("-" * 40)
print(f"TOTAL A PAGAR:      ${pagar:>10,}")
print("="*35)
print("      ¡Gracias por su compra!")
    


