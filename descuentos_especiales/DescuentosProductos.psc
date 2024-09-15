Algoritmo DescuentosProductos
    Escribir "Descuentos a Productos."
    
    Definir montoCompra Como Real
    Definir esVip, codigoEspecial, codigoName Como Cadena
    Definir total Como Real
    
    Escribir "Ingresa Monto de compra: "
    Leer montoCompra
    
    Escribir "¿Eres miembro VIP? s / n: "
    Leer esVip
    
    Escribir "¿Código de descuento? s / n: "
    Leer codigoEspecial
    
    codigoName <- ""
    total <- 0
    
    Si codigoEspecial = "s" Entonces
        Escribir "Ingresa Código: "
        Leer codigoName
    FinSi
    
    Si montoCompra > 100 Y esVip = "s" Y codigoName = "UniSan" Entonces
        total <- montoCompra - ((montoCompra * 0.2) + (montoCompra * 0.1) + (montoCompra * 0.05))
        Escribir "Total: ", montoCompra
        Escribir "Total Descuento| + 20% + 10% + 5% |: ", total
    Sino
        Si montoCompra <= 100 Y esVip = "s" Y codigoName = "UniSan" Entonces
            total <- montoCompra - ((montoCompra * 0.1) + (montoCompra * 0.05))
            Escribir "Total: ", montoCompra
            Escribir "Total Descuento| +10% + 5% |: ", total
        Sino
            Si montoCompra <= 100 Y esVip = "n" Y codigoName = "UniSan" Entonces
                total <- montoCompra - (montoCompra * 0.05)
                Escribir "Total: ", montoCompra
                Escribir "Total Descuento| + 5% |: ", total
            Sino
                Si montoCompra > 100 Y esVip = "s" Y codigoName <> "UniSan" Entonces
                    total <- montoCompra - ((montoCompra * 0.2) + (montoCompra * 0.1))
                    Escribir "Total: ", montoCompra
                    Escribir "Total Descuento| + 20% + 10% |: ", total
                Sino
                    Si montoCompra > 100 Y esVip = "n" Y codigoName = "UniSan" Entonces
                        total <- montoCompra - ((montoCompra * 0.2) + (montoCompra * 0.05))
                        Escribir "Total: ", montoCompra
                        Escribir "Total Descuento| + 20% + 5% |: ", total
                    Sino
                        Si montoCompra > 100 Y esVip = "n" Y codigoName <> "UniSan" Entonces
                            total <- montoCompra - (montoCompra * 0.2)
                            Escribir "Total: ", montoCompra
                            Escribir "Total Descuento| +20% |: ", total
                        Sino
                            Si montoCompra <= 100 Y esVip = "s" Y codigoName <> "UniSan" Entonces
                                total <- montoCompra - (montoCompra * 0.1)
                                Escribir "Total: ", total
                                Escribir "Total Descuento| + 10% |: ", total
                            Sino
                                Escribir "Total ", montoCompra, " | Sin descuento por ningun concepto."
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo

