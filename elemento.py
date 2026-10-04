# Clase Elemento: interfaz comun de Archivo y Carpeta

class Elemento:

    # Constructor que heredan los hijos.
    # Lanza ValueError si el nombre es None o esta vacio.
    def __init__(self, nombre):
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self.nombre = nombre

    """
    Método obtener tamanio
    método abstracto que será heredado por los hijos
    """
    def obtener_tamanio(self):
        pass
