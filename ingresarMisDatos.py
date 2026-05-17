
"""
Clave
%Y → año (2026)
%m → mes (01-12)
%d → día (01-31)
"""
#from datetime import datetime, date
import datetime

nombre1 = input("Ingresar primer nombre : ")
nombre2 = input("Ingresar segundo nombre: ")
apellido = input("Ingresar Apellido: ")
fechanacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
profesion = input("Ingresar profesion : ")
dni = input("Ingresar numero de documento : ")
localidad = input("Ingresar Localidad donde habita : ")

# Convertir string a fecha
fecha_nac = datetime.datetime.strptime(fechanacimiento, "%Y-%m-%d").date()

# Fecha actual
hoy = datetime.date.today()
# Calcular edad (forma correcta)
edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))


print("------------------------------------------------------------")
print(f'Me llamo {nombre1} {nombre2} {apellido}, tengo {edad} años, mi DNI es {dni}, nací el {fechanacimiento}. Soy {profesion} y vivo en {localidad}')
print("------------------------------------------------------------")

persona = {
    "nombre1": nombre1,
    "nombre2": nombre2,
    "apellido": apellido,
    "edad": edad,
    "fechaDeNacimiento" : fechanacimiento,
    "profesion": profesion,
    "dni": dni,
    "localidad": localidad
}

print(persona)