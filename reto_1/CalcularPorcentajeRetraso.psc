	Algoritmo CalcularPorcentajeRetraso
		Escribir "Calcular porcentaje de días de retraso"
		
		Definir diasRetraso Como Entero
		Escribir "Ingrese Días de retraso: "
		Leer diasRetraso
		
		Definir diasAsignados Como Entero
		Escribir "Ingrese Días Asignados: "
		Leer diasAsignados
		
		Definir porcentajeRetraso Como Real
		porcentajeRetraso = (diasRetraso / diasAsignados) * 100
		
		Escribir "Porcentaje de retraso: ", Trunc(porcentajeRetraso), " %"
FinAlgoritmo
