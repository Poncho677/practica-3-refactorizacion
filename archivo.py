class Archivo(elemento):

    def __init__(self, nombre, tamanio):
        super().__init__(nombre)
        self.tamanio = tamanio
        
    def obtener_tamanio(self):
        return self.tamanio
