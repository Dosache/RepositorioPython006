par=0
impar=0
for x in range(1,11):
    num = int(input("Ingrese un numero: "))
    if num%2==0:
        print("El numero es par")
        par = par+1
    else:
        print("Es impar")
        impar = impar+1

    x = x+1

print("La cantidad de numeros pares es: "+str(par))
print("La cantidad de numeros impares es: "+str(impar))