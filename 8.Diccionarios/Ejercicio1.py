diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

país = input("Dime un país y te digo su capital: ").title()
if país in diccionario:
    print("La capital de {} es {}".format(país, diccionario[país]))
else:
    print("El país {} no se encuentra en el diccionario".format(país))