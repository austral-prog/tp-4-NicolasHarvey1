def leap_year():
    anio = int(input("Ingrese un año: "))
    nPar = float(anio / 4)
    if (anio == 4 or anio == -4) or nPar % 2 == 0: 
	    print(f"El año {anio} es bisiesto")
    else: 
	    print(f"El año {anio} no es bisiesto")
