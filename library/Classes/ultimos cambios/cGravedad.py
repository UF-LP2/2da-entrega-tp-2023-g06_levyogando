import datetime as dt
import string #chequear si es necesario esta libreria
from .Errores.cErrorGravedad import cErrorGravedad

class cGravedad:
    def __init__(self, _color):
        _color = _color.lower()
        if(_color == "rojo"):
            _color = 0
            self.TiempoGravedad = dt.timedelta(0,0,0,0,0)
        elif(_color == "naranja"):
            _color = 1
            self.TiempoGravedad = dt.timedelta(0,0,0,0,10)
        elif(_color == "amarillo"):
            _color = 2
            self.TiempoGravedad = dt.timedelta(0,0,0,0,60)
        elif(_color == "verde"):
            _color = 3
            self.TiempoGravedad = dt.timedelta(0,0,0,0,120)
        elif(_color == "azul"):
            _color = 4
            self.TiempoGravedad = dt.timedelta(0,0,0,0,240)
        else:
            raise cErrorGravedad("Creacion Objeto cGravedad")
        self.color = _color
        self.atendido = False
    def getTiempoGravedadActual(self)->dt.timedelta:
        _color = self.color
        if (_color == 0):#rojo
            return dt.timedelta(0,0,0,0,0)
        elif (_color == 1):#naranja
            return dt.timedelta(0,0,0,0,10)
        elif (_color == 2):#amarillo
            return dt.timedelta(0, 0, 0, 0, 60)
        elif (_color == 3):#verde
            return dt.timedelta(0,0,0,0,120)
        elif (_color == 4): #azul
            return dt.timedelta(0,0,0,0,240)
        else:
            raise cErrorGravedad("Error en GetTiempoGravedadActual")
    def getTiempoGravedadMayor(self, _color = 9)->dt.timedelta:
        if (_color == 9):
            _color = self.color
        _color = _color - 1
        if (_color == 0):  # rojo
            return dt.timedelta(0,0,0,0,0)
        elif (_color == 1):  # naranja
            return dt.timedelta(0,0,0,0,10)
        elif (_color == 2):  # amarillo
            return dt.timedelta(0, 0, 0, 0, 60)
        elif (_color == 3):  # verde
            return dt.timedelta(0,0,0,0,120)
        else:
            raise cErrorGravedad("Error en GetGravedadMayor, Puede que haya muerto el paciente")

    def setGravedadMayor(self,Nuevo_color):
        self.color = Nuevo_color
        _color = self.color
        if (_color == 0):  # rojo
            self.TiempoGravedad = dt.timedelta(0,0,0,0,0)
        elif (_color == 1):  # naranja
            self.TiempoGravedad = dt.timedelta(0,0,0,0,10)
        elif (_color == 2):  # amarillo
            self.TiempoGravedad = dt.timedelta(0, 0, 0, 0, 60)
        elif (_color == 3):  # verde
            self.TiempoGravedad = dt.timedelta(0,0,0,0,120)
        else:
            raise cErrorGravedad("Error en AsignarNuevaGravedad, Puede que haya muerto el paciente")

    """
    def Gravedades_posibles(self):
        L = []
        for i in range (0,self.color): 
            L.append(i)
        return L"""