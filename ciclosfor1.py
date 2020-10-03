import os
par=0
impar=0
cont = 0
for x in range(10):
    print("")
    print("Ingrese el digito numero",cont)
    num = int(input())
    if num%2==0:
        print("")
        print("El numero es par")
        par = par+1
        cont = cont+1
    else:
        print("")
        print("Es impar")
        impar = impar+1
        cont = cont+1
    x = x+1

print("")
print("La cantidad de numeros pares es: "+str(par))
print("La cantidad de numeros impares es: "+str(impar))
print("")

#el + se ocupa para concadenar con la palabra str o int, y con comas se utiliza la variable sin la necesidad de escribir str o int