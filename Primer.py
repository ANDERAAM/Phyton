import  math

num1 = int(input("\nIngreese Su Primer  Numero : "))
num2 = int(input("Ingreese Su Segundo Numero : "))

print("\n")

print("1-> SUMA")
print("2-> RESTA")
print("3-> MULTIPLICACION")
print("4-> DIVISION")

Opcion = int(input("\n ESCOJA UNA OPCION PARA REALIZAR LOS CALCULOS : "))

if Opcion==4 and num1==0 or num2==0: print("No SE Puede Realizar Esta Operacion")

if Opcion==1:
    total = num1+num2
if Opcion==2:
    total = num1 - num2
if Opcion == 3:
    total = num1 * num2
if Opcion == 4:
    total = num1 / num2


print("\n ESTE ES EL RESULTADO DE LA OPERACION : ", total)