pikachu = 0
otaku = 0
pulpo = 0
anguila = 0 
subtotal = 0

#menu
print("\n" + "*"*25)
print("TIENDA DE SUSHI")
print("1. Pikachu Roll: $4.500")
print("2. Otaku Roll: $5.000")
print("3. Pulpo Venenoso Roll: $5.200")
print("4. Anguila Electrica Roll: $4.800")

#seleccion
while True:
    menu = input("Selecciona los rolls que desea llevar (presione solo el numero o 'Listo' para pagar): ")

    if menu == "1": 
        pikachu +=1
        subtotal += 4500
        print("Agregaste Pikachu Roll a tu orden")
    
    elif menu == "2":
        otaku += 1
        subtotal += 5000
        print("Agregaste Otaku Roll a tu orden")
    
    elif menu == "3":
        pulpo +=1
        subtotal += 5200
        print("Agregaste Pulpo Venenoso Roll a tu orden")
    
    elif menu == "4":
        anguila +=1
        subtotal+= 4800
        print("Agregaste Anguila Electrica a tu orden")

    elif menu == "listo" or "Listo":
        break

#descuento

descuento = 0
volver_menu = False

while True:
    codigo = input("¿Posees un codigo de descuento? (s/n): ")

    if codigo == "soyotaku":
        descuento = int(subtotal * 0.10)
        print("Codigo aplicado, tienes un 10% de descuento!!")
        break

    else:
        print("Codigo invalido")

        opc = input("Si desea reintentar marque 'si'. Para volver al menu principal marque x: ")

        if opc == "x":
            volver_menu = True
            break
        else:
            continue
        break

#boleta
total_sushis = pikachu + otaku + pulpo + anguila

total_final = subtotal - descuento

print("\n" + "*"*25)
print("TOTAL PRODUCTOS: ", {total_sushis})
print("*"*25)
print(f"Pikachu Roll : {pikachu}")
print(f"Otaku Roll : {otaku}")
print(f"Pulpo Venenoso Roll : {pulpo}")
print(f"Anguila Electrica Roll : {anguila}")
print("*"*25)
print(f"Subtotal: ${subtotal}")
print(f"Descuento aplicado: ${descuento}")
print(f"Total: ${total_final}")
