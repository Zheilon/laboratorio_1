	Algoritmo CalcularPorcentajeRetraso
		Escribir "Calcular porcentaje de d�as de retraso"
		
		Definir diasRetraso Como Entero
		Escribir "Ingrese D�as de retraso: "
		Leer diasRetraso
		
		Definir diasAsignados Como Entero
		Escribir "Ingrese D�as Asignados: "
		Leer diasAsignados
		
		Definir porcentajeRetraso Como Real
		porcentajeRetraso = (diasRetraso / diasAsignados) * 100
		
		Escribir "Porcentaje de retraso: ", Trunc(porcentajeRetraso), " %"
FinAlgoritmo
