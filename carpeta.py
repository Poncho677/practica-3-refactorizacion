from elemento import Elemento

class Carpeta(Elemento):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def obtener_tamanio(self):
        total = 0
        for elemento in self.elementos:
            total  += elemento.obtener_tamanio()
        return total
