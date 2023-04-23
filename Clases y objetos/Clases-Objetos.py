# // CLASE
# class Dino:
#     encendido = False

#     def apaga(self):
#         pass

# d = Dino()
# print(d.encendido)

# // SELF
# class Dino:
#     _encendido = True

#     def apaga(self):
#         self._encendido = False

# d = Dino()
# d.apaga()
# print(d._encendido)

# // SELF OTRO METODO
class Dino:
    _encendido = True

    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido;

d1 = Dino()
d1.apaga()
print(d1.isEncendido())

d2 = Dino()
d2.enciende()
print(d2.isEncendido())

print(d1.isEncendido())