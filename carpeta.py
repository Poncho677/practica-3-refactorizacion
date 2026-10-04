from elemento import Elemento

# Clase Carpeta: contiene archivos y/o otras carpetas

class Carpeta(Elemento):

    # Constructor de Carpeta.
    # Recibe un nombre; si es invalido, Elemento lanza ValueError.
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []

    # Metodo agregar
    # Agrega un Elemento (Archivo o Carpeta).
    # Lanza ValueError si el elemento es None.
    def agregar(self, elemento):
        if elemento is None:
            raise ValueError("El elemento no puede ser None")
        self.elementos.append(elemento)

    # Metodo obtener_tamanio
    # Suma el tamanio de todo lo que hay dentro de la carpeta.
    def obtener_tamanio(self):
        total = 0
        for elemento in self.elementos:
            total += elemento.obtener_tamanio()
        return total
