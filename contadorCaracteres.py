palabra = input("Ingresar un text o palabra:").strip()
cantidadcaracteres = len(palabra)

#convertir el testo en Mayuscula 

if cantidadcaracteres == 0:
    print("No se ingreso palabra o text")
elif palabra.isupper(): 
     pm = palabra.lower()
     print(f'la cantidad de palabras que contiene es de {cantidadcaracteres}  y el texto en minuscula ingresado fue {pm}')
else:
    if palabra.islower():
        pmm = palabra.upper()
        print(f'la cantidad de palabras que contiene es de {cantidadcaracteres}  y el texto en mayuscula ingresado fue {pmm}')
    else:
        print(f'la cantidad de palabras que contiene es de {cantidadcaracteres}  y el texto ingresado NO se modifica   {palabra}')