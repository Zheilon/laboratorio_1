Proceso SistemaDeControlDeAcceso
    Escribir "Sistema de control de acceso"
    
    Definir nivelAcceso Como Entero
    Escribir "Ingrese su nivel de acceso: "
    Leer nivelAcceso
    
    Definir consulta Como Entero
    Escribir "Indique en d�as el �ltimo cambio que tuvo la contrase�a de su tarjeta: "
    Leer consulta
    
 
    Definir actividadTarjeta Como Caracter
    Escribir "�Tarjeta de identificaci�n ACTIVA? True = t / False = f: "
    Leer actividadTarjeta
    
 
    Si nivelAcceso = 5 y consulta <= 30 y Minusculas(actividadTarjeta) = "t" Entonces
        Escribir "Acceso Concedido!"
    Sino
        Si nivelAcceso = 0 y consulta > 30 y Minusculas(actividadTarjeta) = "f" Entonces
            Escribir "Acceso Denegado!"
        Sino

            Escribir "Los valores ingresados con incorrectos!"
        FinSi
    FinSi
FinProceso

