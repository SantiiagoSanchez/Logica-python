import random

letras = ["A", "B", "C"]
numeros = ["1", "2", "3"]

elementos_contrasena = letras + numeros

def generar_contrasena() -> str:
    return "".join(random.sample(elementos_contrasena, 4))


contrasena_secreta = generar_contrasena()

intentos = 1

print("==============ADIVINA LA CONTRASEÑA==============")

while intentos <= 10:

    print(f"\nIntento: {intentos}")
    contrasena = input("Introduce la contraseña: ").upper()

    #MANEJO DE ERRORES.
    if len(contrasena) != 4:
        print("ERROR: La contraseña tiene que tener 4 caracteres.\n")
        continue
    
    if not all(caracter in elementos_contrasena for caracter in contrasena):
        print(f"ERROR: Solo se permite colocar los siguientes caracteres: {elementos_contrasena}")
        continue

    #GANAR
    if contrasena == contrasena_secreta:
        print(f"\nGANASTE!\nLa contraseña es : {contrasena}\nLo conseguiste en el intento: {intentos}\n")
        break

    intentos += 1

    if intentos > 10:
        print(f"\nPERDISTE: Los 10 intentos han sido incorrectos\nLa contraseña era {contrasena_secreta}")
    else:
        for index, caracter in enumerate(contrasena):
            if caracter == contrasena_secreta[index]:
                print(f"{caracter}: Esta en la posicion correcta")
            elif caracter in contrasena_secreta:
                print(f"{caracter}: Esta pero no en la posicion correcta")
            else:
                print(f"{caracter}: No esta en la contraseña")
