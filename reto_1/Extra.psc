Algoritmo CalculoPanelesSolaresExtra
    Definir consoleConsumoAnual, consoleEficienciaPanel, consoleSuperficiePromedio, consoleRadiacionPromedio, consolePromedioLuzSol Como Real
    Definir nuevaPotenciaDiaria, nuevaPotenciaAnual, nuevoNumeroDePaneles, areaTotal Como Real
	
    Escribir "Extra"
    Escribir ""
	
    Escribir "Ingresa Consumo Anual: "
    Leer consoleConsumoAnual
    Escribir "Ingresa Eficiencia del Panel %: "
    Leer consoleEficienciaPanel
    Escribir "Ingrese Superficie Promedio del Panel: "
    Leer consoleSuperficiePromedio
    Escribir "Ingresa Radiaci�n Solar Promedio: "
    Leer consoleRadiacionPromedio
    Escribir "Ingresa Horas Promedio de Sol / D�a: "
    Leer consolePromedioLuzSol
	
    Escribir ""
	

    nuevaPotenciaDiaria <- consoleSuperficiePromedio * consoleRadiacionPromedio * (consoleEficienciaPanel / 100)
    Escribir "Potencia Diaria: ", nuevaPotenciaDiaria, " Kwh."
	

    nuevaPotenciaAnual <- nuevaPotenciaDiaria * 365
    Escribir "Potencia Anual: ", nuevaPotenciaAnual, " Kwh."
	

    nuevoNumeroDePaneles <- Trunc(consoleConsumoAnual / nuevaPotenciaAnual)
    Escribir "N�mero de Paneles: ", nuevoNumeroDePaneles
	

    areaTotal <- consoleSuperficiePromedio * nuevoNumeroDePaneles
    Escribir "El �rea necesaria para instalar los paneles solares es de:" , areaTotal, " Metros Cuadrados"
FinAlgoritmo


