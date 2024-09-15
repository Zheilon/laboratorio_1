print(" ---------> Sistema de control de acceso <---------\n")

#La variable nivelAcceso almacena el valor que se ingresó.
#por la consola.
nivelAcceso = int(input("Ingrese su nivel de acceso: "))
print()

#La variable consulta almacena el valor que se ingresó.
#por la consola.
consulta = int(input('''Indique en días el último cambio que
tuvo la contraseña de su targeta: '''))
print()

#La variable actividadTargeta almenacena un resultado de
#dos opciones disponibles: True = t / False = f. 
actividadTargeta = str(input("¿Targeta de identificación ACTIVA? True = t / False = f: "))
print()

#En esta estructura if, else-if se evalua la condición del nivel de acceso,
#el cambio de contraseña en los último 30 días, la actividad de targeta
#el cual acompañando la variable actividadTargeta esta el método lower()
#que devuelve un str de minusculas.
if nivelAcceso == 5 and consulta <= 30 and actividadTargeta.lower() == 't':
    print("Acceso Concedido!")

elif nivelAcceso == 0 and consulta > 30 and actividadTargeta.lower() == 'f':
    print("Acceso Denegado!")

elif nivelAcceso == 0 and consulta <= 30 and actividadTargeta.lower() == 't':
    print("Acceso Denegado!")

elif nivelAcceso == 5 and consulta > 30 and actividadTargeta.lower() == 't':
    print("Acceso Denegado!")

#En este else, utilizado para cuando el usuario no halla ingresado alguno
#de los campos correctamente. 
else:
    print("Ingrese indicación correcta!")

