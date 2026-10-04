class Elemento:
    
    def __init__(self, nombre):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self.nombre = nombre

    def obtener_tamanio(self):
        pass
