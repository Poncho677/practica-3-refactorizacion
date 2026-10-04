#Clase Elemento

class Elemento:

    #Constructor de la clase Elemento que será heredado por los hijos
    
    def __init__(self, nombre):
        if nombre.strip() == "" or nombre == none:
            raise ValueError("El nombre no puede estar vacio")
        self.nombre = nombre

    '''Método obtener tamanio
    método abstracto que será heredado por los hijos'''
    
    def obtener_tamanio(self):
        pass
