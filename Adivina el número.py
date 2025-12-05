


print("Juego: Adivina el número")
print("Instrucción: Adivina el número (entre 1 y 5) con una única pista. Puedes elegir entre tres niveles.")


nivel = int(input("Selecciona el nivel (1, 2 o 3): ")) # Solicitar al usuario que elija un nivel
if nivel == 1:
    print("Nivel 1: El número de letras de la siguiente palabra: ")
    numero_correcto = 4  # La palabra "gato" tiene 4 letras
    for letra in "gato": # Desplegar cada letra de la palabra "gato"
        print(letra)
    intento = int(input("Adivina el número: ")) # Solicitar al usuario que adivine el número
    if intento == numero_correcto: # Verificar si el intento es correcto
        print("Correcto!")
    else:
        print("Incorrecto. Intenta de nuevo.")
elif nivel == 2:
    print("Nivel 2: El número es par.")
    numero_correcto = 2
    intento = int(input("Adivina el número: ")) # Solicitar al usuario que adivine el número
    if intento == numero_correcto: # Verificar si el intento es correcto
        print("Correcto!")
    else:
        print("Incorrecto. Intenta de nuevo.")
elif nivel == 3:
    print("Nivel 3: El número es impar.")
    numero_correcto = 3
    intento = int(input("Adivina el número: ")) # Solicitar al usuario que adivine el número
    if intento == numero_correcto: # Verificar si el intento es correcto
        print("Correcto")
    else:
        print("Incorrecto. Intenta de nuevo.")
else:
    print("Nivel no válido. Terminado el juego.")
print("¡Gracias por jugar!")
