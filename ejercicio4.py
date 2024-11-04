'''Crea un programa que pida al usuario dos numeros y muestre su division
si el segundo es cero, o un mensaje de aviso en caso contradictorio'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
if num2 == 0:
    print(f"No se puede dividir entre cero.")
else:
    print(f"la division es: ", num1/num2)
