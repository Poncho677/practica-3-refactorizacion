from carpeta import Carpeta
from creador_archivo import CreadorPDF, CreadorTexto

class CorreoLegacy:
    def send_email(self, to, body):
        print("Para: " + to)
        print(body)

def enviar_resultado(carpeta, destino):
    correo = CorreoLegacy()
    correo.send_email(destino, "Tamanio total: " + str(carpeta.obtener_tamanio()))

def main():
    creador_pdf = CreadorPDF()
    creador_texto = CreadorTexto()

    clase = Carpeta("MyP")
    clase.agregar(creador_pdf.crear_archivo("practica.pdf", 120))
    clase.agregar(creador_texto.crear_archivo("notas.txt", 80))

    ejemplos = Carpeta("Ejemplos")
    ejemplos.agregar(creador_texto.crear_archivo("ejemplo.txt", 50))
    clase.agregar(ejemplos)

    print(clase.obtener_tamanio())
    enviar_resultado(clase, "profesor@universidad.edu")

if __name__ == "__main__":
    main()
