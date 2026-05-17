"""
Sistema de alumnos
Ingresar datos por consola
nombre , edad . materias , año , curso , nota
Mostrar : lista de alumnos (diccionario completo)
Mostrar : alumnos aprobados y desaprobados
Mostrar: promedio aprobados desaprobados
Mostrar mayor y menor calificacion obtenida junto al nombre , materia del alumno

"""
alumnos = {}

for alumno in range (3):
  nomb = input("Ingresar Nombre : ")
  ed = int(input("Ingresar Edad :"))
  materia = input("Ingresar Materia :")
  año = int(input("Ingresar año :"))
  nota = int(input("Ingresar Nota : "))
  
  alumnos[alumno] = {
  "nombre": nomb,
  "edad": ed,
  "materia": materia,
  "anio": año,
  "nota": nota
    }
 
print("\n----- LISTA DE ALUMNOS -----\n")

for clave, datos in alumnos.items():

    print(f'Alumno #{clave + 1}')

    for campo, valor in datos.items():
        print(f'{campo}: {valor}')

    print("-------------------")