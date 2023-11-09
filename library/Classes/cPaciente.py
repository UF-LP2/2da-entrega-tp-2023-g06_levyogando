from .cPaciente_sinGravedad import *
from .cGravedad import cGravedad
from .Errores.cErrorPaciente import cErrorPaciente
from .Errores.cErrorGravedad import cErrorGravedad
import datetime as dt


class cPaciente(cPaciente_sinGravedad):
    def __init__(self, nombre, color,edad,casoClinico,enfermero,textohisotrial,):
        super().__init__(edad,casoClinico,enfermero,textohisotrial)
        self._nombre=nombre
        self._gravedad = cGravedad(color)
        HaceCuantoleDuele=[24,48,72]
        GradoDolor=[1,2,3,4,5,6,7,8,9,10]
        #ver si poner o no como parametros el grado que seleciono el enfermero en triage


    def getNombre(self):
        return self._nombre
    def getGravedad(self):
        """
        este metodo devuelve el color de la gravedad actual
        :return:
        """
        return self._gravedad.color

    def getTiempoRestante(self):
        """
        Este metodo devuelve el tiempo que le queda en esa gravedad asignada
        :return:
            x > 0 si el tiempo de la gravedad actual es mayor al tiempo que estvuo esperando
            x = 0 si el tiempo de espera fue igual o mayor al de la gravedad mayor
        """

        # Compara las fechas
        fecha_reciente = self._gravedad.getTiempoGravedadActual()
        fecha_antigua = self.getHaceCuantoLLego()
        if fecha_reciente > fecha_antigua:
            resultado = fecha_reciente - fecha_antigua
        else:
            resultado = dt.timedelta(0)
        return resultado


    def getTiempoRestanteMayorGravedad(self):
        """
        Este metodo devuelve el tiempo que le queda si la gravedad es mayor
        :return:
            x > 0 si el tiempo de la gravedad es mayor al tiempo que estvuo esperando
            x = 0 si el tiempo de espera fue igual o mayor al de la gravedad mayor
        """
        fecha_reciente = self._gravedad.getTiempoGravedadMayor()
        fecha_antigua = self.getHaceCuantoLLego()
        if fecha_reciente > fecha_antigua:
            resultado = fecha_reciente - fecha_antigua
        else:
            resultado = dt.timedelta(0)
        return resultado

    def setGravedadMayorPaciente(self):
        """
        Este metodo tiene como objetivo cambiar de gravedad al paciente si el tiempo que le queda en su gravedad
        es menor en otra gravedad mayor
        :return:
        """

        t_restante_gravedad_actual = self.getTiempoRestante() #Obtengo tiempo restante actual
        t_restante_gravedadad_mayor = self.getTiempoRestanteMayorGravedad() #obtengo timpo restante gravedad mayor
        #if (t_restante_gravedadad_mayor <= t_restante_gravedad_actual)
        if t_restante_gravedad_actual <= t_restante_gravedadad_mayor:
            #Se cumple si el tiempo restante de la gravedad actual es menor al de una gravedad mayor
            num = self.gestionar_paciente()
            self._gravedad.setGravedadMayor(num)
        else:
            raise cErrorPaciente("Error en setGravedadMayorPaciente")
        return self.getGravedad()

    def gestionar_paciente(self):

        """
        Este metodo cumple dos funciones:
                -  La primera es en el caso de que un paciente halla esperado mucho mas
                    tiempo del deseado, cambie directamente a una gravedad mucho mayor
                -  La segunda sería en el caso de que haya esperado el tiempo justo,
                    este se le debería asignar la gravedad siguiente
        :return:
         numero de la nueva gravedad
        """

        """
        tengo que hacer que si los pacientes exceden 
        el tiempo de espera de la gravedad siguiente evaluar cual sería la
        gravedad a la cual saltar
        """
        tiempo_restante = self.getHaceCuantoLLego() - self._gravedad.getTiempoGravedadActual() - self._gravedad.getTiempoGravedadMayor()
        if(tiempo_restante > dt.timedelta(0)): #si esto se cumple es pq el paciente espero mucho
            tiempo_restante = self.getHaceCuantoLLego() - self._gravedad.getTiempoGravedadActual()
            try:
                num = self.Funcion_recursiva_gravedades_mayores(tiempo_restante,self.getGravedad()) #obtengo cuantas gravedades habría que saltear
                return self.getGravedad() - (num+1)
            except(cErrorGravedad):
                return 0 #el paciente espero demasiado y se esta por morir teoricamente


        tiempo_llegada = self.getHaceCuantoLLego()  # Obtener hace cuanto llego el paciente
        color = self.getGravedad()  # Obtener la gravedad actual

        if tiempo_llegada > dt.timedelta(minutes=120) and color > 3:
            # Acciones para pacientes con más de 120 minutos de tiempo restante
            return 3
        elif tiempo_llegada > dt.timedelta(minutes=60) and color > 2:
            # Acciones para pacientes con más de 60 minutos y menos de 120 minutos de tiempo restante
            return 2
        elif tiempo_llegada > dt.timedelta(minutes=10) and color > 1:
            # Acciones para pacientes con más de 10 minutos y menos de 60 minutos de tiempo restante
            return 1
        else:
            # Acciones para pacientes con menos de 10 minutos de tiempo restante
            return 0


    def Funcion_recursiva_gravedades_mayores(self,tiempo_restante,gravedad_act):

        tiempo_restante = tiempo_restante - self._gravedad.getTiempoGravedadMayor(gravedad_act)

        if(tiempo_restante>dt.timedelta(0)):# si > 0, significa que hay que saltear al menos una gravedad mas
            return 1 + self.Funcion_recursiva_gravedades_mayores(tiempo_restante,gravedad_act-1)
        else:
            return 0

    def __eq__(self, other):

        val_2 = self._tiempoLlegada - other._tiempoLlegada
        if (self.getGravedad()==other.getGravedad()) and (val_2<dt.timedelta(milliseconds=100)) and (self._nombre == other._nombre):
            return True
        else:
            return False