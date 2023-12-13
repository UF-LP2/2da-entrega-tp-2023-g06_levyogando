from .cEnfermero import cEnfermero
from Classes import cQuesMaestra
from random import randrange
from random import choice
from Classes import cPaciente
from .Errores.cErrorSalaEspera import cErrorSalaEspera
import datetime as dt
from Classes import cManejoArchivo
from Classes import cMedico
class cSalaEsera:
    def __init__(self):
        self.medico = cMedico()
        self.Lista_pacientes = cQuesMaestra()
        self.Sala_Espera = []
        self.HandlerArchivos = cManejoArchivo()
        self.Num_ulitmo_caso_clinico = self.HandlerArchivos.BusquedaUltimo()


    def Pacientes_sin_Clasificar(self,paciente): #sirve para los 2 metodos
        self.Sala_Espera.append(paciente)

    def Pacientes_Clasificados(self): #d&c
        paciente = self.Sala_Espera.pop(0)
        paciente.setClasificado()
        self.Lista_pacientes.insert(paciente)

    def Pacientes_Clasificados_greedy(self):
        paciente = self.Sala_Espera.pop(0)
        self.Lista_pacientes.Insertar_greedy(paciente)

    def NoMasDe3Mins(self,paciente): #sirve para los 2
        fecha = dt.timedelta(0,0,0,0,paciente.getTiempoLLegada().minute,paciente.getTiempoLLegada().hour,0)
        hora = dt.datetime.now()
        ahora = dt.timedelta(0,0,0,0,hora.minute,hora.hour,0)
        diferencia = (fecha - ahora).total_seconds() / 60
        if (paciente.getClasificado == 'false' and diferencia > 3):
            raise cErrorSalaEspera("El paciente lleva mas de 3 minutos en la sala de espera")


    def Atender(self):
        _Paciente_atendido = self.Lista_pacientes.ObtenerProximo()
        if self.medico.getDisponibilidad() == 'true':  # hay medicos disponibles
                if(_Paciente_atendido.getCasoClinico()== 'Morgue'):
                    self.HandlerArchivos.agregar_paciente(_Paciente_atendido)
                else:
                    _Paciente_atendido.setDerivar()
                    sala = choice(['cuidados_intensivos', 'preparar_para_cirugia ', 'psicologia', 'Morgue', 'Buscar Cama'])
                    _Paciente_atendido.setCasoClinico(sala)
                    self.HandlerArchivos.agregar_paciente(_Paciente_atendido)

        else:
            raise cErrorSalaEspera("Error No hay medicos disponibles")

    def Atender_automatico(self, medico):
            for x in self.Lista_pacientes:
                _Paciente_atendido = self.Lista_pacientes.ObtenerProximo()
                if medico.getDisponibilidad() == 'true':  # hay medicos disponibles
                    _Paciente_atendido.setDerivar()
                    sala = choice(['cuidados_intensivos', 'preparar_para_cirugia ', 'psicologia', 'morgue', 'Buscar Cama'])
                    _Paciente_atendido.setCasoClinico(sala)
                    self.HandlerArchivos.agregar_paciente(_Paciente_atendido)

                else:
                    raise cErrorSalaEspera("Error No hay medicos disponibles")


    def Cambiar_gravedad(self):
        p = self.Lista_pacientes.ObtenerProximo()
        fecha = dt.timedelta(0, 0, 0, 0, p.getTiempoLLegada().minute, p.getTiempoLLegada().hour, 0)
        hora = dt.datetime.now()
        ahora = dt.timedelta(0, 0, 0, 0, hora.minute, hora.hour, 0)
        diferencia = (fecha - ahora).total_seconds() / 60
        if (diferencia > p.getGravedad__.getTiempoGravedadActual()):
            self.Lista_pacientes.Reorganizar()

    def Cambiar_gravedad_greedy(self):
        p = self.Lista_pacientes.ObtenerProximo()
        fecha = dt.timedelta(0, 0, 0, 0, p.getTiempoLLegada().minute, p.getTiempoLLegada().hour, 0)
        hora = dt.datetime.now()
        ahora = dt.timedelta(0, 0, 0, 0, hora.minute, hora.hour, 0)
        diferencia = (fecha - ahora).total_seconds() / 60
        if (diferencia > p.getGravedad__.getTiempoGravedadActual()):
            self.Lista_pacientes.Reorganizar_greedy(p)
