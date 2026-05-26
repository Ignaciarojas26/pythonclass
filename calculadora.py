def suma(a,b):
    return a + b 

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b  

def division(a,b):
    if b == 0:
        return "Error, no se puede dividir por 0"

    return a / b 


print("\n ==========Calculadora==========")
      
num1=float(input("Ingresa tu primer numero: "))
num2=float(input("Ingresa tu segundo numero: "))

#menu
print("\n1 Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = input("Seleccione una opcion: ")

if opcion == "1":
    print("Resultado: ", suma(num1,num2))

elif opcion == "2":
    print("Resultado: ", resta(num1,num2))

elif opcion == "3":
    print("Resultado: ", multiplicacion(num1,num2))

elif opcion == "4":
    print("Resultado: ", division(num1,num2))

else:
    print("Opcion invalida, intente de nuevo")