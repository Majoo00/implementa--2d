# Solicita al usuario que ingrese el texto que desea cifrar
texto = input("Tu texto: ")

# Verifica si el texto está en mayúsculas
if texto == texto.upper():
    # Si el texto está en mayúsculas, usa el alfabeto en mayúsculas
    abc = "ABCDEFGHIJKLMNOPQRSTVXYZ"
else:
    # Si el texto está en minúsculas, usa el alfabeto en minúsculas
    abc = "abcdefghijklmnopqrstuvwxyz"

# Solicita al usuario que ingrese el valor de desplazamiento para el cifrado
k = int(input("Valor de desplazamiento "))

# Inicializa una cadena vacía para almacenar el texto cifrado
cifrad = ""

# Itera sobre cada carácter en el texto ingresado
for c in texto:
    # Verifica si el carácter está en el alfabeto seleccionado
    if c in abc:
        # Si está en el alfabeto, encuentra su posición y aplica el desplazamiento
        cifrad += abc[(abc.index(c) + k) % (len(abc))]
    else:
        # Si no está en el alfabeto (por ejemplo, espacios o signos de puntuación), lo agrega sin cambios
        cifrad += c

# Imprime el texto cifrado
print("Texto cifrado: ", cifrad) 
