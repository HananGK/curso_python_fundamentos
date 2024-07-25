def facturaIVA():
    factura = float(input("Ingresa el valor de la factura: "))
    IVA = float(input("Ingresa el porcentaje del IVA: "))
    if IVA > 0: 
        return factura + (factura * (IVA / 100))
    elif IVA == 0:
        return factura + (factura * 0.21)
    else:
        return "El porcentaje de IVA no puede ser negativo"

print("El valor de la factura con el IVA aplicado es: ", facturaIVA())