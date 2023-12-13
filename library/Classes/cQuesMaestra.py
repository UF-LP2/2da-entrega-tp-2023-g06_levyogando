import queue
from .cManejoArchivo import *
from .Errores.cErrorTamanio import cErrorTamanio
from .Errores.cErrorGravedad import cErrorGravedad
from .Errores.cErrorPaciente import cErrorPaciente

class cQuesMaestra:
    def __init__(self):
        self.R = queue.Queue(maxsize=0)
        self.N = queue.Queue(maxsize=0)
        self.AM = queue.Queue(maxsize=0)
        self.V = queue.Queue(maxsize=0)
        self.AZ = queue.Queue(maxsize=0)
        self.Lista_de_colas = []
        self.Lista_de_colas.append(self.R)
        self.Lista_de_colas.append(self.N)
        self.Lista_de_colas.append(self.AM)
        self.Lista_de_colas.append(self.V)
        self.Lista_de_colas.append(self.AZ)
        self.Handler = cManejoArchivo()

    def Reorganizar(self, indice_lista=4):
        if indice_lista == 0:
            return 1
        if(self.Lista_de_colas[indice_lista].qsize()==0):
            return self.Reorganizar(indice_lista - 1)
        obj_act = self.Lista_de_colas[indice_lista].queue[0]
        if obj_act.getTiempoRestante() > obj_act.getTiempoRestanteMayorGravedad():
            return self.Reorganizar(indice_lista - 1)
        else:
            num = obj_act.setGravedadMayorPaciente()
            obj_act = self.Lista_de_colas[indice_lista].get_nowait()
            self.Lista_de_colas[num].put_nowait(obj_act)
            return self.Reorganizar(indice_lista)


    def insert(self, _paciente):
        try:
            num = -1
            try:
                num = _paciente.getGravedad()
            except cErrorGravedad("En el insert") as err:
                num = _paciente.setGravedadMayorPaciente()
            self.Lista_de_colas[num].put_nowait(_paciente)
        except cErrorTamanio("Error en el insert") as errorTam:
            print(cErrorTamanio)

    def ObtenerProximo(self):
        if(self.R.qsize()>0):
            return self.R.get_nowait()
        elif (self.N.qsize() > 0):
            return self.N.get_nowait()
        elif (self.AM.qsize() > 0):
            return self.AM.get_nowait()
        elif (self.V.qsize() > 0):
            return self.V.get_nowait()
        elif (self.AZ.qsize() > 0):
            return self.AZ.get_nowait()
        else:
            raise cErrorTamanio("No hay pacientes a atender")

    def DerivarProximo(self):
        """En este metodo guasrdamos en el archivo al paciente mas importante"""
        self.Handler.agregar_paciente(self.ObtenerProximo())