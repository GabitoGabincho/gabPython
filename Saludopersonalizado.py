"""
Pedir: nombre edad
Mostrar: Hola Juan, tenés 25 años
Practicás:  variables input f-string
"""
import datetime

nombre = input("Ingresar nombre: ")
edad = int(input("Ingresar Edad: "))

hoy = datetime.date.today()

anio_actual = hoy.year
mes_nacimiento = 5
dia_nacimiento = 23

if (hoy.month, hoy.day) >= (mes_nacimiento,dia_nacimiento):
    anio_nacimiento = anio_actual - edad
else:
    anio_nacimiento = anio_actual - edad - 1
    
def saludoPersonalizado(nom,ed):
    print(f'Hola {nom}, tenès {ed} años naci en el año {anio_nacimiento}')
   
saludoPersonalizado(nombre,edad)



