import pytest
from carpeta import Carpeta
from archivo import Archivo
from creador_archivo import CreadorPDF, CreadorTexto

def test_carpeta_vacia():
    assert Carpeta("Vacia").obtener_tamanio() == 0

def test_carpeta_con_pdf_de_120():
    carpeta = Carpeta("Carpeta")
    carpeta.agregar(CreadorPDF().crear_archivo("practica.pdf", 120))
    assert carpeta.obtener_tamanio() == 120

def test_carpeta_con_pdf_de_120_y_texto_de_80():
    carpeta = Carpeta("Carpeta")
    carpeta.agregar(CreadorPDF().crear_archivo("practica.pdf", 120))
    carpeta.agregar(CreadorTexto().crear_archivo("notas.txt", 80))
    assert carpeta.obtener_tamanio() == 200

def test_ejemplo_con_subcarpeta_de_50():
    padre = Carpeta("MyP")
    padre.agregar(CreadorPDF().crear_archivo("practica.pdf", 120))
    padre.agregar(CreadorTexto().crear_archivo("notas.txt", 80))
    hija = Carpeta("Ejemplos")
    hija.agregar(CreadorTexto().crear_archivo("ejemplo.txt", 50))
    padre.agregar(hija)
    assert padre.obtener_tamanio() == 250

def test_carpeta_con_archivo_tamanio_0():
    carpeta = Carpeta("Carpeta")
    carpeta.agregar(CreadorTexto().crear_archivo("vacio.txt", 0))
    assert carpeta.obtener_tamanio() == 0

def test_constructor_archivo_vacio():
    with pytest.raises(ValueError):
        Archivo("", 120)

def test_constructor_archivo_negativo():
    with pytest.raises(ValueError):
        Archivo("texto.txt", -1)
        
def test_creador_pdf_devuelve_pdf():
    archivo = CreadorPDF().crear_archivo("practica.pdf", 120)
    assert archivo.nombre == "practica.pdf"
    assert archivo.obtener_tamanio() == 120

def test_creador_texto_devuelve_texto():
    archivo = CreadorTexto().crear_archivo("texto.txt", 80)
    assert archivo.nombre == "texto.txt"
    assert archivo.obtener_tamanio() == 80
