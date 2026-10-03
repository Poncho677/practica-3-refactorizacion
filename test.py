import pytest
from main import Archivo, Carpeta, agregar_archivo, obtener_tamanio

def test_carpeta_vacia():
    assert obtener_tamanio(Carpeta("Vacia")) == 0

def test_carpeta_con_pdf_de_120():
    carpeta = Carpeta("Carpeta")
    agregar_archivo(carpeta, "pdf", "practica.pdf", 120)
    assert obtener_tamanio(carpeta) == 120

def test_carpeta_con_pdf_de_120_y_texto_de_80():
    carpeta = Carpeta("Carpeta")
    agregar_archivo(carpeta, "pdf", "practica.pdf", 120)
    agregar_archivo(carpeta, "txt", "texto.txt", 80)
    assert obtener_tamanio(carpeta) == 200

def test_ejemplo_con_subcarpeta_de_50():
    padre = Carpeta("Carpeta Padre")
    agregar_archivo(padre, "pdf", "practica.pdf", 120)
    agregar_archivo(padre, "txt", "texto.pdf", 80)
    hija = Carpeta("Carpeta hija")
    agregar_archivo(hija, "txt", "ejemplo.txt", 50)
    padre.subcarpetas.append(hija)
    assert obtener_tamanio(padre) == 250

def test_carpeta_con_archivo_tamanio_0():
    carpeta = Carpeta("Carpeta")
    agregar_archivo(carpeta, "txt", "texto.txt", 0)
    assert obtener_tamanio(carpeta) == 0
    
def test_constructor_archivo_vacio():
    with pytest.raises(ValueError):
        Archivo("texto.txt", 0)

def test_constructor_archivo_negativo():
    with pytest.raises(ValueError):
        Archivo("texto.txt", -1)
