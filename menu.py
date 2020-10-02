import os

def Numeros(n):
    posi = 0
    nega = 0
    cero = 0
    for i in range(1,n+1):
        numeritos = int(input("Ingrese un numero: "))
        if (numeritos>0):
            print("El numero es postivo")
            print("")
            posi = posi+1
        if (numeritos<0):
            print("El numero es negativo")
            print("")
            nega = nega+1
        if (numeritos==0):
            print("El numero es igual a 0")
            print("")
            cero= cero+1
    print("La cantidad de numeros positivos es de: ", posi)
    print("La cantidad de numeros negativos es de: ", nega)
    print("La cantidad de numeros iguales a 0 es de: ", cero)

    pause = input("Digite cualquier tecla para continuar: ")
    
def Personas(n):
    totaledad = 0
    prom = 0
    for i in range (n):
        nom = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        totaledad = totaledad+edad

    prom = round((totaledad/n),1)
    print("El promedio de edades de las personas ingresadas es de: ",prom)
    pause = input("Digite cualquier tecla para continuar: ")



seguir = True
n = 0
while (seguir):
    os.system('cls')

    print("1. Numeros")
    print("2. Daatos Personales")
    print("3. Finalizar")
    
    op = int(input("Digite opcion 1, 2 o 3: "))

    if(op==1):
        n = int(input("Ingrese una cantidad de numeros: "))
        Numeros(n)
    if(op==2):
        n = int(input("Ingrese una cantidad de personas: "))
        Personas(n)
    if(op==3):
        print("Programa finalizado!")
        pause = input("Digite cualquier tecla para continuar: ")
        break
    
