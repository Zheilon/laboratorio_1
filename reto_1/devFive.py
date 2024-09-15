print()

#Se declaran las variables en un contexto Global
consumoAnual = 12000
promedioLuzSol = 5
EficienciaPanel = 0.15
superficePromedioP = 1.6
radiacionPromedio = 5

#En la variable potencia diaria se almacena la operación para
#hallar la potencia diaria: superficie promedio * radiación promedio * eficiencia del panel.
potenciaDiaria = superficePromedioP * radiacionPromedio * EficienciaPanel

#Por medio de este panel se imprime el resultado de la variable
#potenciaDiaria.
print(f"Potencia Diaria: {potenciaDiaria} Kwh.")

#En la variable potencia diaria se almacena la operación para
#hallar la potencia diaria: superficie promedio * radiación promedio * eficiencia del panel.
potenciaAnual = potenciaDiaria * 365
print(f"Potencia Anual: {potenciaAnual} Kwh.")

#Número de Paneles - División Entera
numeroDePaneles = consumoAnual // potenciaAnual
print(f"Número Paneles: {numeroDePaneles}")

print()
print("Extra\n")

consoleConsumoAnual = float(input("Ingresa Consumo Anual: "))
consoleEficienciaPanel = float(input("Ingresa Eficiencia del Panel %: "))
consoleSuperficiePromedio = float(input("Ingrese Superficie Promedio del Panel: "))
consoleRadiacionPromedio = float(input("Ingresa Radiación Solar Promedio: "))
consolePromedioLuzSol = float(input("Ingresa Horas Promedio de Sol / Día: "))

print()

nuevaPotenciaDiaria = consoleSuperficiePromedio * consoleRadiacionPromedio * (consoleEficienciaPanel / 100)
print(f"Potencia Diaria: {nuevaPotenciaDiaria} Kwh.")

nuevaPotenciaAnual = nuevaPotenciaDiaria * 365
print(f"Potencia Anual: {nuevaPotenciaAnual} Kwh.")

nuevoNumeroDePaneles = consoleConsumoAnual // nuevaPotenciaAnual
print(f"Número de Paneles: {int(nuevoNumeroDePaneles)}")

areaTotal = consoleSuperficiePromedio * nuevoNumeroDePaneles
print(f"El área necesaria para instalar {int(nuevoNumeroDePaneles)} paneles es de: {round(areaTotal, 2)} Metros Cuadrados.")