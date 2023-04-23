# temperatura = 22.0

def miFuncion(nombre="Luis"):
    hoyHace = 24
    # print("Temperatura", temperatura)
    print("Hola", nombre, "la temperatura es de", hoyHace, "centigrados")

# def matematicas(a,b):
#     def suma(a,b):
#         print(a + b)

#     def resta(a,b):
#         print(a - b)

#     suma(a,b)
#     resta(a,b)

# def suma(a=1, b=2, c=5):
#     print(a + b + c)

# suma( c = 9 )
# miFuncion()
# miFuncion("Hector")
# # matematicas(5,3)

# // ARGS
# def suma(*args):
#     resultado = 0
#     for arg in args:
#         resultado += arg
#     print(resultado)

# suma(9, 9)

# def suma(**kwargs):
#     for key, value in kwargs.items():
#         print(key, "=", value)

# suma(vivienda="piso", coche="rojo")

# // NAMED PARAMETERS
# def suma(**kwargs):
#     if 'coche' not in kwargs:
#         return
    
#     if kwargs['coche'] == 'bonito':
#         print("Tu coche es bonito")

# suma()

# def operaciones(a, b):
#    return a + b, a - b, a * b, a / b

# # resultado = operaciones(2, 4)
# suma, resta, multi, divi = operaciones(2, 4)
# print(suma)
# print(resta)
# print(multi)
# print(divi)

# // OTRO EJEMPLO KWARGS
def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else inicial
    # final = kwargs['final] ? kwargs['final] = 0 // OTRO LENGUAGE

    resultado = 0
    for x in range(inicial, final + 1):
        resultado += x

    return resultado

# print(sumador(final=5))

# // FUNCIONES ANONIMAS - LAMBDA

anonima  = lambda nombre,nombre2: print("hola", nombre, "adios", nombre2)

anonima("Hector", "Rotz")


# ES LO MISMO:
# def sumatoria(x):
#     return x+x

sumatoria = lambda x: x+x
print(sumatoria(2))