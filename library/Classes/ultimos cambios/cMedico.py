from Classes import cManejoArchivo

class Medico:
    def __init__(self):
        self.Medicos_disponibles = 'true'
        self.Matricula = '7800234'

    def getDisponibilidad(self):
        return self.Medicos_disponibles

    def setDisponibilidad(self):
        self.Medicos_disponibles = 'false'  # solo true o false

