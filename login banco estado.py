intento = 5

while intento > 0:
    usuario = input("Nombre del usuario: ")
    password = input("Ingrese su clave: ")

    if password =="banco123": 

        print ("Bienvenido a Banco estado", usuario)

        break
    else:

        intento -= 1

        print(f"Usuario o contraseña invalido. Tienes  {intento} intentos restantes")

        if intento == 0:
            print("Por favor comuniquese con nuestro call center, 660 770 8880")
