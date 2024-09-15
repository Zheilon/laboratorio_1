print(" ---------> Calcular porcentaje de días de retraso <---------\n")

#En la variable diasRetraso se almacena el valor
#ingresado por consola.
diasRetraso = int(input("Ingrese Días de retraso: "))

#En la variable diasAsignados se almacena el valor
#ingresado por consola.
diasAsignados = int(input("Ingrese Días Asignados: "))

#En la variable se almacena el resultado de la 
#formula para hallar el porcentaje de retraso - 
#(dias de retraso / dias asignados) * 100.
porcentajeRetraso = (diasRetraso / diasAsignados) * 100

#Por medio de este print se imprime por consola
#el resultado de la variable porcentaje: 
#porcentajeRetraso.
print(f"Porcentaje de retraso: {int(porcentajeRetraso)} %")