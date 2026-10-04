from archivo import ArchivoPDF, ArchivoTexto

class CreadorArchivo:
    def crear_archivo(self, nombre, tamanio):
        pass

class CreadorPDF(CreadorArchivo):
    def crear_archivo(self, nombre, tamanio):
        return ArchivoPDF(nombre, tamanio)

class CreadorTexto(CreadorArchivo):
    def crear_archivo(self, nombre, tamanio):
        return ArchivoTexto(nombre, tamanio)
