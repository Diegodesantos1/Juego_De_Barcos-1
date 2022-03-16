
instances = ()
jugadas = set()

def __init__(self, x, y):
  # Adición de las coordenadas
  self.x = x
  self.y = y
  # Queremos poder acceder a una casilla a partir de sus coordenadas
  self.instances[x, y] = instances
  # Generación del nombre de la casilla
  self._generar_nombre(self, x, y)
  # Queremos poder acceder a una casilla a partir de su nombre
  instances[self.nombre] = self.casillas_ocupadas
  # Evolución de la casilla
  self.jugada = False
  self.barco = None  # No toca a un barco de momento.

def generar_nombre(self):
  """Este método puede ser sobrecargado fácilmente"""
  self.nombre = self.generar_nombre_casilla(self, self.x, self.y)

def jugar(self):
  """Describe qué pasa cuando jugamos una casilla"""
  self.jugada = True
  self.jugadas.add(self)
  if self.barco is not None:
      if len(self.casilla.barco.casillas - self.casillas_jugadas) == 0:
          print("Hundido !!")
      else:
          print("Tocado !")
  else:
      print("Agua !")

@classmethod
def generar_casillas():
  for x, y in classmethod.product(range(classmethod.tablero_num_lineas),
    range(classmethod.tablero_num_columnas)):
      classmethod.Case(x, y)

def __str__(self):
  """Sobrecarga del método de transformación en cadena"""
  if not self.jugada:
      return classmethod.CASO_NO_JUGADO
  elif self.barco is None:
      return classmethod.CASO_AGUA
  return classmethod.CASO_TOCADO
