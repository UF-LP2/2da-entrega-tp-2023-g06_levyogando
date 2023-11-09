import datetime as dt


class cPaciente_sinGravedad:
    def __init__(self, edad,casoClinico,enfermero,textohisotrial):
        self._edad= edad
        self._tiempoLlegada = dt.datetime.now()
        self._casoClinico= casoClinico
        self._enfermero_quien_categorizo=enfermero
        self._historial=textohisotrial


    def getHistorial(self):
        """

        :return: Nombre del paciente
        """
        return self._historial

    def getEdad(self):
        """

        :return: Nombre del paciente
        """
        return self._edad

    def getEnfermero(self):
        """

        :return: devuelvo el enfermero
        """
        return self._enfermero_quien_categorizo

    def getCasoClinico(self):
        """

        :return:
        caso clinico
        """
        return self._casoClinico

    def getTiempoLLegada(self):
        return self._tiempoLlegada



    def getHaceCuantoLLego(self):
        return dt.datetime.now()-self._tiempoLlegada

    def setTiempoLlegada(self, tiempo_llegada):
        """Este metodo lo voy a ir comentando o no dependiendo si estoy testeando funciones"""
        self._tiempoLlegada = tiempo_llegada





    def __eq__(self, other):
        val_2 = self._tiempoLlegada - other._tiempoLlegada
        if (val_2<dt.timedelta(milliseconds=100)):
            return True
        else:
            return False