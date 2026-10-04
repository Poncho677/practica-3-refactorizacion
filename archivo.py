from elemento import Elemento

# Clase Archivo

class Archivo(Elemento):
    
    # Constructor de Archivo.
    # Recibe nombre y tamanio; lanza ValueError si alguno es invalido.
    def __init__(self, nombre, tamanio):
        super().__init__(nombre)
        if tamanio < 0:
            raise ValueError("El tamanio no puede ser negativo")
        self.tamanio = tamanio

    # Metodo obtener_tamanio
    # Reescribe el de Elemento y regresa el tamanio del archivo.
    def obtener_tamanio(self):
        return self.tamanio

class ArchivoPDF(Archivo):
    pass

class ArchivoTexto(Archivo):
    pass
