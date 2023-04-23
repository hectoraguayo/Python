peso = input("Ingresa tu peso en Kilogramos: ")
estatura = input("Ingresa tu estatura en metros: ")
IMC = round(float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal es: ", IMC)