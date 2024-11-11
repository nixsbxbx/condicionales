'''El director de una escuela esta organizando un viaje de estudios, y requiere determinar
cuanto debe cobrar a cada alumno y cuanto debe de pagar a la compañia de viajes por el servicio. 
La forma de cobrar es la siguiente:
 si son 100 alumnos o mas, el costo por cada alumno es de 65 euros
 de 50 a 99 alumnos, el costo es de 70 euros
 de 30 a 49 alumnos, de 95 euros
 y si son menos de 30
 el costo de la renta del autobus es de 4000 euros, sim importar el numero de alumnos
 Realice un programa que permita determinar el pago a la compañia de autobuses y lo que debe pagar
 cada alumno por el viaje

 Entrada:
         numero de alumnos
 Salida:
        precio total a pagar por alumno
        pago a la compañia'''

def calcular_costos(num_alumnos):
    if num_alumnos >= 100:
        costo_por_alumno = 65
        pago_compania = num_alumnos * costo_por_alumno
    elif 50 <= num_alumnos < 100:
        costo_por_alumno = 70
        pago_compania = num_alumnos * costo_por_alumno
    elif 30 <= num_alumnos < 50:
        costo_por_alumno = 95
        pago_compania = num_alumnos * costo_por_alumno
    else:
        costo_por_alumno = 4000 / num_alumnos
        pago_compania = 4000

    return costo_por_alumno, pago_compania

# Leer la cantidad de alumnos
num_alumnos = int(input("Ingrese el número de alumnos: "))

# Obtener los costos
costo_por_alumno, pago_compania = calcular_costos(num_alumnos)

# Mostrar los resultados
print(f"El costo por alumno es: {costo_por_alumno} euros")
print(f"El pago total a la compañía de autobuses es: {pago_compania} euros")