#ingresar datos por pantalla y asignarlos a una variable
from datetime import date, datetime

def calcularEdad(fecha_nacimiento):
    fecha_actual = date.today()
    fecha_nacimiento = datetime.strptime(
        fecha_nacimiento, "%d/%m/%Y"
    ).date()
    edad_en_anios = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (
        fecha_nacimiento.month,
        fecha_nacimiento.day
    ):
        edad_en_anios -= 1
    return edad_en_anios

print("- - - - - - - - - - Ingresar Datos Personales - - - - - - - - - - ")

nombre = input("Ingresar Nombre : ")
nickname = input("Ingresar NickName : ")
fecha = input("Ingrese su fecha de nacimiento (DD/MM/YYYY): ")
edad = calcularEdad(fecha)
profesion = input("Ingrese Profesion : ")
idiomas = {
    "idioma1" : input("Ingresar Lengua Nativa :"),
    "idioma2" : input("Ingresar Segunda Lengua :"),
    "idioma3" : input("Ingresar Tercer Lengua : "),
}

idioma1t = idiomas["idioma1"],
idioma2t = idiomas["idioma2"],
idioma3t = idiomas["idioma3"]

idiomas2 = (idioma1t,idioma2t,idioma3t)

#enviar a github




print("- - - - - - - - - - Mostrar Datos Ingresados - - - - - - - - - - ")
#print(f"Me llamo {nombre}\n  y me llaman {nickname}\n , naci {fecha}\n o sea que tengo {edad}\n años y soy {profesion}\n , hablo 3 idiomas {idiomas['idioma1']}\n, {idiomas['idioma2']}\n y {idiomas['idioma3']}\n , {idiomas['idioma3']}\n estoy en cursando Nivel 6 (B1)")
print(
    f"Me llamo {nombre}\n"
    f"Me llaman {nickname}\n"
    f"Nací el {fecha}\n"
    f"Tengo {edad} años\n"
    f"Soy {profesion}\n"
    f"Hablo 3 idiomas : {idiomas['idioma1']} {idiomas['idioma2']} y {idiomas['idioma3']}\n"
    f"{idiomas['idioma3']} estoy cursando Nivel 6 (B1)"
    )

print (f"Datos de la tupla : {idiomas2}")