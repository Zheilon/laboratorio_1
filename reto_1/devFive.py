print()

#Se declaran las variables en un contexto Global
consumoAnual = 12000
promedioLuzSol = 5
EficienciaPanel = 0.15
superficePromedioP = 1.6
radiacionPromedio = 5

#En la variable potenciaDiaria se almacena la operación para
#hallar la potencia diaria: superficie promedio * radiación promedio * eficiencia del panel.
potenciaDiaria = superficePromedioP * radiacionPromedio * EficienciaPanel

#Por medio de este print se imprime el resultado de la variable
#potenciaDiaria.
print(f"Potencia Diaria: {potenciaDiaria} Kwh.")

#En la variable potenciaAnual se almacena la operación para
#hallar la potencia Anual: potencia diaria * 365.
potenciaAnual = potenciaDiaria * 365

#Por medio de este print se imprime el resultado de la variable
#potenciaAnual.
print(f"Potencia Anual: {potenciaAnual} Kwh.")

#En la variable número de paneles se almacena la operación para hallar
#El número de paneles: consumo anual / potencia anual. 
#En esta operación es efectuada por medio de la división Entera,
#La cual nos devuelve un cociente si la parte entera, redondeando hacia abajo.
numeroDePaneles = consumoAnual // potenciaAnual

#Por medio de este print se imprime el resultado de la variable
#numeroDePaneles.
print(f"Número Paneles: {numeroDePaneles}")

print()
print("Extra\n")

#Este conjunto de variables toman el valor flotante que se ingresa por consola.
consoleConsumoAnual = float(input("Ingresa Consumo Anual: "))
consoleEficienciaPanel = float(input("Ingresa Eficiencia del Panel %: "))
consoleSuperficiePromedio = float(input("Ingrese Superficie Promedio del Panel: "))
consoleRadiacionPromedio = float(input("Ingresa Radiación Solar Promedio: "))
consolePromedioLuzSol = float(input("Ingresa Horas Promedio de Sol / Día: "))

print()

#En la variable nuevaPotenciaDiaria se almacena la operación para
#hallar la potencia diaria: superficie promedio * radiación promedio * eficiencia del panel.
nuevaPotenciaDiaria = consoleSuperficiePromedio * consoleRadiacionPromedio * (consoleEficienciaPanel / 100)

#Por medio de este print se imprime el resultado de la variable
#nuevaPotenciaDiaria.
print(f"Potencia Diaria: {nuevaPotenciaDiaria} Kwh.")

#En la variable nuevaPotenciaAnual se almacena la operación para
#hallar la potencia Anual: potencia diaria * 365.
nuevaPotenciaAnual = nuevaPotenciaDiaria * 365

#Por medio de este print se imprime el resultado de la variable
#nuevaPotenciaAnual.
print(f"Potencia Anual: {nuevaPotenciaAnual} Kwh.")

#En la nuevaNumeroDePaneles se almacena la operación para hallar
#El número de paneles: consumo anual / potencia anual. 
#En esta operación es efectuada por medio de la división Entera,
#La cual nos devuelve un cociente si la parte entera, redondeando hacia abajo.
nuevoNumeroDePaneles = consoleConsumoAnual // nuevaPotenciaAnual

#Por medio de este print se imprime el resultado de la variable
#nuevoNumeroDePaneles.
print(f"Número de Paneles: {int(nuevoNumeroDePaneles)}")


#En la variable areaTotal se almacena la operación para hallar la superficie
#Necesaria respecto a la cantidad de paneles a instalar. 
areaTotal = consoleSuperficiePromedio * nuevoNumeroDePaneles

#Por medio de este print se imprime el area necesitada para instalar
#cierto número de paneles.
print(f"El área necesaria para instalar {int(nuevoNumeroDePaneles)} paneles es de: {round(areaTotal, 2)} Metros Cuadrados.")