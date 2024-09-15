print("---+---+---> Calcular Volumen de pelota <---+---+---\n")

#Se implementan las librerias math.pi y math.pow
#la primera nos ofrece el valor de PI
#la segunda nos ayuda calcular la variable elevada al cubo.
import math

#En la variable radio se almacena el valor
#ingresado por consola.
radio = float(input("Ingrese radio de la pelota en Centimetros: "))

#En la variable volumenPelota almacena el resultado de
#la formula para hallar el volumen de la esfera -
#4 / 3 * PI * radio^3.
volumenPelota = 4 / 3 * math.pi * math.pow(radio, 3)

#Por medio de este print se imprime el resultado
#de la variable volumenPelota.
print(f"Volumen de la pelota: {volumenPelota} Centimetros Cúbicos.")