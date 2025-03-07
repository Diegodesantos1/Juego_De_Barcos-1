from juego import (choice,product,repeat)
from juego import *
instances = []
casillas_ocupadas = set()

def __init__(self, longitud):
        self.longitud = longitud
        self.orientacion = choice(classmethod.ORIENTACIONES)
        self.tocado = False
        self.hundido = False

        # performance / legibilidad:
        num_lineas = self.Conventions.tablero_num_lineas
        num_columnas = self.Conventions.tablero_num_columnas
        num2l = self.Conventions.generar_num_linea
        num2c = self.Conventions.generar_num_columna

        while True:
            if self.orientacion == classmethod.HORIZONTAL:
                rang = choice(range(num_lineas))
                primero = choice(range(num_columnas + 1 - longitud))
                letra = num2l(rang)
                cifras = [num2c(x) for x in range(primero, primero + longitud)]
                self.casillas = {self.Case.instances[l + c]
                for l, c in product(repeat(letra, longitud), cifras)}
            else:
                rang = choice(range(num_columnas))
                primero = choice(range(num_lineas + 1 - longitud))
                cifra = num2c(rang)
                letras = [num2l(x) for x in range(primero, primero + longitud)]
                # Crear el barco
                self.casillas = {self.Case.instances[l + c]
                for l, c in product(letras, repeat(cifra, longitud))}

            for existente in self.Barco.instances:
                if self.casillas.intersection(existente.casillas):
                    break  # break relativo al "for existente in barcos:"
            else:
                # Agregar el barco en el contenedor de barcos
                self.Barco.instances.append(self)
                # Informar la casilla que contiene un barco.
                for casilla in self.casillas:
                    casilla.barco = self
                # Agregar estas casillas a las casillas ocupadas :
                self.Barco.casillas_ocupadas |= self.casillas
                break  # break relativo al "while True:"

@classmethod
def generar_barcos(cls):
        for longitud in cls.Conventions.barcos_longitud:
            cls.Barco(longitud)
