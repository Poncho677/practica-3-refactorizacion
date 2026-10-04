from archivo import ArchivoPDF, ArchivoTexto

# Clase CreadorArchivo: interfaz comun para crear archivos

class CreadorArchivo:

    # Metodo crear_archivo
    # Metodo abstracto que sera reescrito por las subclases creadoras.
    def crear_archivo(self, nombre, tamanio):
        pass

# Clase CreadorPDF: Crea archivos PDF
    
class CreadorPDF(CreadorArchivo):

    # Metodo crear_archivo
    # Instancia y regresa un objeto especifico de la clase ArchivoPDF.
    def crear_archivo(self, nombre, tamanio):
        return ArchivoPDF(nombre, tamanio)

# Clase CreadorTexto: Crea archivos de Texto
    
class CreadorTexto(CreadorArchivo):

    # Metodo crear_archivo
    # Instancia y regresa un objeto especifico de la clase ArchivoTexto.
    def crear_archivo(self, nombre, tamanio):
        return ArchivoTexto(nombre, tamanio)
