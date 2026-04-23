intento = 5

while intento > 0:

    def mascota():
        minimo= {"min": 2}
        print("¡Bienvenido al selector de mascotas, para comenzar responde un par de preguntas!")
        vivienda = input("¿Casa o Departamento?: ")
        horas = int(input("Horas libres en casa: "))
        if vivienda[0] == "c" or horas >= 6:
            if horas != 0 and horas > 4: return "Perro"
            else: return "Gato"
        elif horas < 6 and horas <= minimo["min"]: return "Pez"
        else: return "Hámster"
    print(mascota())

    intento -= 1 

    if intento == 0: 
        print("Gracias por usar nuestro selector de mascotas, espero te haya sido util.")