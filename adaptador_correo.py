from notificador import Notificador

# Clase AdaptadorCorreo: adapta CorreoLegacy para la interfaz Notificador

class AdaptadorCorreo(Notificador):

    # Constructor de AdaptadorCorreo
    # Recibe el objeto de correo legacy.
    def __init__(self, correo):
        self.correo = correo

    # Método enviar
    # Valida el correo de destino y deja el envío a CorreoLegacy.
    def enviar(self, destino, mensaje):
        if destino is None or destino.strip() == "" or "@" not in destino:
            raise ValueError("El destino no es n correo válido")
        self.correo.send_email(destino, mensaje)
