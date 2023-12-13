from .cPaciente import cPaciente

class cEnfermero:
    """
    Esta clase tiene como objetivo dar a conocer el/la enfermer@ de triage que se encargo de
    clasificar al pacientes que fue registrado y luego de esto se encuentra en la sala de espera para ser
    atendidos
    """

    def __init__(self, Nombre="def", Matricula="111111"):
        self._nombre = Nombre
        self._Matricula = Matricula



    def getNombreEnfermero(self):
        return self._nombre

    def getMatricula(self):
        return self._Matricula

    def Clasificar(self, _nombre, _color, _casoClinico,edad,textohisotrial):
        """
        toda esta informacion viene de la interfaz del usario, y el usuario que agendo
        :param:
        :return:
            Se agrego al paciente a la base de datos
        """
        NuevoPaciente = cPaciente(_nombre, _color,edad,_casoClinico,self,textohisotrial)
        return NuevoPaciente

