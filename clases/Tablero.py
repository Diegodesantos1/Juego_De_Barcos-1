from Case import *
from Barco import *
from Conventions import *



def __init__(self):
# Creamos las casillas:
  self.generar_casillas()

  # Creamos los barcos:
  self.generar_barcos()
  # performance / legibilidad:
  num_lineas = self.Conventions.tablero_num_lineas
  num_columnas = self.Conventions.tablero_num_columnas
  num2l = self.Conventions.generar_num_linea
  num2c = self.Conventions.generar_num_columna
  # Creamos la herramienta para poder seguir la situación
  self.casillas_jugadas = set()
  # Generamos aquí los etiquetas para facilitar la visualización
  self.etiqueta_lineas = [num2l(x) for x in range(num_lineas)]
  self.etiqueta_columnas = [num2c(x) for x in range(num_columnas)]
  trazo_horizontal = " --" + "+---" * 10 + "+"

def ver(self):
  print("   |", " | ".join(self.etiqueta_columnas), "|")
  iter_etiqueta_lineas = iter(self.etiqueta_lineas)
  for x, y in product(range(self.Conventions.tablero_num_lineas),
    range(self.Conventions.tablero_num_columnas)):
      # Trazo horizontal para cada nueva línea
      if y == 0:
          print(self.trazo_horizontal)
          print(" {}".format(next(iter_etiqueta_lineas)), end="")
      casilla = self.Case.instances[x, y]
      print(" |", casilla, end="")
      # Ver la barra vertical derecha de la tabla:
      if y == 9:
          print(" |")
  # Ver la última línea horizontal
  print(self.trazo_horizontal + "\n\n")




