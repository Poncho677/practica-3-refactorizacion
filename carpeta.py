from elemento import Elemento

#Creando clase carpeta que contiene la clase o carpetas

class Carpeta(Elemento):

    #Constructor de Carpeta que recibe un nombre, si es invalido entonces salte ValueError
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []

    '''Método agregar que agrega un objeto de la clase elemento o aquellos que hereden de este
    salta ValueError si el elemento es invalido'''
    
    def agregar(self, elemento):
        if elemento == none or elemento.strip() == "":
            raise(ValueError)
        self.elementos.append(elemento)

    '''Método obtener tamanio
    este método sirve para obtener la suma de los tamaños de cada
    archivo y/o carpeta dentro de la carpeta'''
    
    def obtener_tamanio(self):
        total = 0
        for elemento in self.elementos:
            total  += elemento.obtener_tamanio()
        return total
