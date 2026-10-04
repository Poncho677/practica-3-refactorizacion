from carpeta import Carpeta
from creador_archivo import CreadorPDF, CreadorTexto
from adaptador_correo import AdaptadorCorreo

class CorreoLegacy:
    def send_email(self, to, body):
        print("Para: " + to)
        print(body)

def enviar_resultado(carpeta, destino, notificador):
    mensaje = "Tamanio total: " + str(carpeta.obtener_tamanio())
    notificador.enviar(destino, mensaje)

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
    notificador = AdaptadorCorreo(CorreoLegacy())
    enviar_resultado(clase, "profesor@universidad.edu", notificador)

if __name__ == "__main__":
    main()
