from elemento import Elemento

class Archivo(Elemento):
    def __init__(self, nombre, tamanio):
        super().__init__(nombre)
        if tamanio < 0:
            raise ValueError("El tamanio no puede ser negativo")
        self.tamanio = tamanio

    def obtener_tamanio(self):
        return self.tamanio

class ArchivoPDF(Archivo):
    pass

class ArchivoTexto(Archivo):
    pass
