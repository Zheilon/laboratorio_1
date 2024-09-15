print("---+---+---> Descuentos a Productos <---+---+---\n")

#En la variable montoCompra lmacena el valor ingresado
#Por consola.
montoCompra = float(input("Ingresa Monto de compra: "))

#En la variable esVip almacena un valor ingresado por consola
#De 2 opciones disponibles.
esVip = str(input("¿Eres miembro VIP? s / n: "))

#En la variablef codigoEspecial almacena un valor ingresado por consola
#De 2 opciones disponibles.
codigoEspecial = str(input("¿Código de descuento? s / n: "))

#Variable Alcance Global.
codigoName = ""

#En la variable total se almacena el resultado de operación que
#Que se le aplica al monto de compra para calcular sus posibles descuentos.
total = 0

#En Esta Estructura if, else-if, verifica si el código almacenacenado en la
#Variable códigoName es correcto.
if codigoEspecial == 's':
    codigoName = str(input("Ingresa Código: "))

#En esta Super Estructura de condicional if y else-if's, evalua cada uno de los posibles
#Descuentos suceptibles a la aplicación del monto de compra, tomando en cuenta las variables
#Que insiden en el problema - 

#Monto de Compra = (a) - ¿Es miembro VIP? = (b) - ¿Posee Código de Descuento? =(c).
#Numero de combinaciones, Que se pueden cumplir.
#1. | a - b - c |
#2. | a - b |
#3. | b - c |
#4. | a - c |
#5. | a |
#6. | b |
#7. | c |

#Uso de métodos: lower() = retorna una cadena de caracteres en forma minúscula.

#Condicional N° ( 1 )
if montoCompra > 100 and esVip.lower() == 's' and codigoName == "UniSan":
    total = montoCompra - ((montoCompra * 0.2) + (montoCompra * 0.1) + (montoCompra * 0.05))

    print(f"Total: {montoCompra:,.2f}")
    print(f"Total Descuento| + 20% + 10% + 5% |: {total:,.2f} $")

#Condicional N° ( 2 )
elif montoCompra <= 100 and esVip.lower() == 's' and codigoName == "UniSan":
    total = montoCompra - ((montoCompra * 0.1) + (montoCompra * 0.05))

    print(f"Total: {montoCompra:,.2f}")
    print(f"Total Descuento| +10% + 5% |: {total:,.2f} $")

#Condicional N° ( 3 )
elif montoCompra <= 100 and esVip.lower() == 'n' and codigoName == "UniSan":
    total = montoCompra - (montoCompra * 0.05)

    print(f"Total: {montoCompra:,.2f}")
    print(f"Total Descuento| + 5% |: {total:,.2f} $")

#Condicional N° ( 4 )
elif montoCompra > 100 and esVip.lower() == 's' and codigoName != "UniSan":
    total = montoCompra - ((montoCompra * 0.2) + (montoCompra * 0.1))

    print(f"Total: {montoCompra:,.2f}")
    print(f"Total Descuento| + 20% + 10% |: {total:,.2f} $")

#Condicional N° ( 5 )
elif montoCompra > 100 and esVip.lower() == 'n' and codigoName == "UniSan":
    total = montoCompra - ((montoCompra * 0.2) + (montoCompra * 0.05))

    print(f"Total: {montoCompra:,.2f}")
    print(f"Total Descuento| + 20% + 5% |: {total:,.2f} $")

#Condicional N° ( 6 )
elif montoCompra > 100 and esVip.lower() == 'n' and codigoName != "UniSan":
    total = montoCompra - (montoCompra * 0.2)

    print(f"Total: {montoCompra:,.2f} $")
    print(f"Total Descuento| +20% |: {total:,.2f} $")

#Condicional N° ( 7 )
elif montoCompra <= 100 and esVip.lower() == 's' and codigoName != "UniSan":
    total = montoCompra - (montoCompra * 0.1)

    print(f"Total: {total:,.2f} $")
    print(f"Total Descuento| + 10% |: {total:,.2f} $")

#Salida Opcional
else:
    print(f"Total {montoCompra} | Sin descuento por ningun concepto.")