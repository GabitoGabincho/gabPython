palabra = input("Ingresar un text o palabra:")
cantidadcaracteres = len(palabra)

if cantidadcaracteres == 0:
    print("No se ingreso palabra o text")
else: 
    print(f'la cantidad de palabras que contiene es de {cantidadcaracteres} y el texto o palabra ingresado fue {palabra}')
    
