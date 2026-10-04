from elemento import Elemento

#Clase Archivo

class Archivo(Elemento):

    #Constructor de la clase Archivo
    #Recibe nombre y tamaño, salta ValueError en caso de que alguno sea inválido
    
    def __init__(self, nombre, tamanio):
        super().__init__(nombre)
        if tamanio < 0:
            raise ValueError("El tamanio no puede ser negativo")
        self.tamanio = tamanio

    '''Método obtener_tamanio
    método heredado de Elemento y que regresa el tamaño designado del archivo'''
    
    def obtener_tamanio(self):
        return self.tamanio

class ArchivoPDF(Archivo):
    pass

class ArchivoTexto(Archivo):
    pass
