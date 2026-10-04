# Practica-3 :smile:
# Equipo: 2 y un infiltrado :shushing_face:

## Integrantes:
* Cruz Escobar Aarón
* Góngora Barroso Alfonso
* Quirino Roman Emmanuel

## ¿Qué hace el programa?
Calcula el tamaño total de una carpeta (sumando sus archivos y los de sus
subcarpetas) y lo envía por un correo simulado.

## Requisitos
* Python 3
* pytest (para las pruebas): `pip install pytest`

## ¿Cómo ejecutar el programa?
Desde el directorio del proyecto:

    python main.py

Debe imprimir:

    250
    Para: profesor@universidad.edu
    Tamanio total: 250

## ¿Cómo ejecutar las pruebas?

    pytest -v

Deben pasar las 9 pruebas.

## Archivos
* main.py: arma el ejemplo (MyP con la subcarpeta Ejemplos), calcula el
  tamaño y envía el resultado. Contiene CorreoLegacy, sin modificar.
* elemento.py: Elemento, interfaz común de archivos y carpetas.
* archivo.py: Archivo, ArchivoPDF y ArchivoTexto.
* carpeta.py: Carpeta, que guarda elementos y suma sus tamaños.
* creador_archivo.py: CreadorArchivo, CreadorPDF y CreadorTexto
  (Factory Method).
* notificador.py: interfaz Notificador.
* adaptador_correo.py: AdaptadorCorreo (Adapter), conecta Notificador con
  CorreoLegacy.
* test_main.py: pruebas.
* ANALISIS.md: análisis, cambios, pruebas, diagrama y respuestas.

## Código inicial
Este es el código original, sin refactorizar. También está en el historial
de commits (commit `ee749bd` con las pruebas de la etapa 2).

```python
"""Codigo inicial de la practica 3: aun NO esta refactorizado.

El equipo debe separar responsabilidades, identificar oportunidades de
Composite / Factory Method / Adapter y comprobar que conserva la salida.
"""


class Archivo:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio


class ArchivoPDF(Archivo):
    def __init__(self, nombre, tamanio):
        super().__init__(nombre, tamanio)


class ArchivoTexto(Archivo):
    def __init__(self, nombre, tamanio):
        super().__init__(nombre, tamanio)


class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = []
        self.subcarpetas = []


class CorreoLegacy:
    def send_email(self, to, body):
        print("Para: " + to)
        print(body)


def agregar_archivo(carpeta, tipo, nombre, tamanio):
    if tipo == "pdf":
        carpeta.archivos.append(ArchivoPDF(nombre, tamanio))
    elif tipo == "txt":
        carpeta.archivos.append(ArchivoTexto(nombre, tamanio))


def obtener_tamanio(carpeta):
    total = 0
    for archivo in carpeta.archivos:
        total += archivo.tamanio
    for subcarpeta in carpeta.subcarpetas:
        total += obtener_tamanio(subcarpeta)
    return total


def enviar_resultado(carpeta, destino):
    correo = CorreoLegacy()
    correo.send_email(destino, "Tamanio total: " + str(obtener_tamanio(carpeta)))


def main():
    clase = Carpeta("MyP")
    agregar_archivo(clase, "pdf", "practica.pdf", 120)
    agregar_archivo(clase, "txt", "notas.txt", 80)

    ejemplos = Carpeta("Ejemplos")
    agregar_archivo(ejemplos, "txt", "ejemplo.txt", 50)
    clase.subcarpetas.append(ejemplos)

    print(obtener_tamanio(clase))
    enviar_resultado(clase, "profesor@universidad.edu")


if __name__ == "__main__":
    main()
```