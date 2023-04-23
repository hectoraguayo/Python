def bisiesto(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
year = int(input("Ingresa el año: "))

if bisiesto(year):
    print(year, "es un año bisiesto")
else:
    print(year, "no es un año bisiesto")
