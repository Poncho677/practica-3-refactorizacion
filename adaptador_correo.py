from notificador import Notificador

class AdaptadorCorreo(Notificador):

    def __init__(self, correo):
        self.correo = correo

    def enviar(self, destino, mensaje):
        if destino is None or destino.strip() == "" or "@" not in destino:
            raise ValueError("El destino no es n correo válido")
        self.correo.send_email(destino, mensaje)
