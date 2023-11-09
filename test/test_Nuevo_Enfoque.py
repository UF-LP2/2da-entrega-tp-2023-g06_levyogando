import datetime as dt
#import random

import pytest
from Classes.Nuevo_enfoque import *
from Classes.cManejoArchivo import *
from Classes.cSalaEspera import cSalaEspera
from Classes import cRandoms
def test_Error_Insercion_Gravedad():
    """
    Este test tiene que asertar si al paciente se lo instancia con una gravedad distinta a las posibles
    :return:
    """
    with pytest.raises(cErrorGravedad):
        paciente_1 = cPaciente("Julian", "-", 1, None, None, None)


def test_Paciente_Indepndendica_Gravedad_MayusMinus():
    """
    Este test tiene que asertar al darle a diferentes pacientes la misma gravedad si se escribe diferente
        :return:
    """
    paciente_1 = cPaciente("Julian", "AZUL", 1, None, None, None)
    paciente_2 = cPaciente("andres", "azul", 1, None, None, None)
    assert paciente_1.getGravedad() is paciente_2.getGravedad()


def test_Paciente_cambio_de_gravedad_naranja():
    """
    Si el paciente esta en sala de espera por mas del tiempo permitido debe cambiar de gravedad
    :return:
    """
    paciente_1 = cPaciente("1", "naranja",1,None,None,None)
    paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=10))
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 0

def test_Paciente_sin_cambio_de_gravedad_amarillo():
    with pytest.raises(cErrorPaciente):
        paciente_1 = cPaciente("2", "Amarillo",1,None,None,None)
        paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=50))
        paciente_1.setGravedadMayorPaciente()
        assert paciente_1.getGravedad() == 2

def test_Paciente_cambio_de_gravedad_amarillo():
    paciente_1 = cPaciente("2", "Amarillo",1,None,None,None)
    paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=60))
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 1
def test_Paciente_sin_cambio_de_gravedad_verde():
    with pytest.raises(cErrorPaciente):
        paciente_1 = cPaciente("3", "verde",1,None,None,None)
        paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=110))
        paciente_1.setGravedadMayorPaciente()
        assert paciente_1.getGravedad() == 3

def test_Paciente_cambio_de_gravedad_verde():
    paciente_1 = cPaciente("2", "verde",1,None,None,None)
    paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=120))
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 2
def test_Paciente_sin_cambio_de_gravedad_azul():
    with pytest.raises(cErrorPaciente):
        paciente_1 = cPaciente("4", "azul",1,None,None,None)
        paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=230))
        paciente_1.setGravedadMayorPaciente()
        assert paciente_1.getGravedad() == 4

def test_Paciente_cambio_de_gravedad_azul():
    paciente_1 = cPaciente("3", "azul",1,None,None,None)
    paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=241))
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 3

def test_Paciente_cambio_de_gravedad_varias_gravedades():
    paciente_1 = cPaciente("1", "azul",1,None,None,None)
    paciente_1.setTiempoLlegada( paciente_1.getTiempoLLegada() - dt.timedelta(minutes=421))
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 1

def test_Paciente_tiempo_restante():
    """
    Revisar este test
    :return:
    """
    paciente_1 = cPaciente("Julian", "naranja",1,None,None,None)
    paciente_1.setTiempoLlegada( dt.datetime.now() - dt.timedelta(minutes=10))
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getTiempoRestante() == dt.timedelta(0,0,0,0,0)




def test_insertar_DyC():
        """
               :return:
               """
        paciente_1 = cPaciente("Julian", "Azul", 1, None, None, None)
        paciente_2 = cPaciente("Julian2", "naranja", 1, None, None, None)
        paciente_3 = cPaciente("Julian3", "Amarillo", 1, None, None, None)
        Nuevo_enfoque=cNuevoEnfoque()
        Nuevo_enfoque.insert(paciente_1)
        Nuevo_enfoque.insert(paciente_2)
        Nuevo_enfoque.insert(paciente_3)
        assert len(Nuevo_enfoque.Lista_de_pacientes)==3


def test_orden_DyC():
    """
           :return:
           """
    paciente_1 = cPaciente("Julian", "Azul", 1, None, None, None)
    paciente_2 = cPaciente("Julian2", "naranja", 1, None, None, None)
    paciente_3 = cPaciente("Julian3", "Amarillo", 1, None, None, None)
    Nuevo_enfoque = cNuevoEnfoque()
    Nuevo_enfoque.insert(paciente_1)
    Nuevo_enfoque.insert(paciente_2)
    Nuevo_enfoque.insert(paciente_3)
    sacado_1 = Nuevo_enfoque.Lista_de_pacientes.pop(0)
    assert sacado_1 == paciente_2

    sacado_2 = Nuevo_enfoque.Lista_de_pacientes.pop(0)
    assert sacado_2 == paciente_3

    sacado_1 = Nuevo_enfoque.Lista_de_pacientes.pop(0)
    assert sacado_1 == paciente_1
    assert len(Nuevo_enfoque.Lista_de_pacientes) == 0

def test_buscar_limite_gravedades():
    """
               :return:
               """
    paciente_1 = cPaciente("Julian", "Rojo", 1, None, None, None)
    paciente_2 = cPaciente("Julian2", "naranja", 1, None, None, None)
    paciente_3 = cPaciente("Julian3", "Amarillo", 1, None, None, None)
    paciente_4 = cPaciente("Julian4", "naranja", 1, None, None, None)
    Nuevo_enfoque = cNuevoEnfoque()
    Nuevo_enfoque.insert(paciente_1)
    Nuevo_enfoque.insert(paciente_2)
    Nuevo_enfoque.insert(paciente_3)
    Nuevo_enfoque.insert(paciente_4)
    #Si es limite me devuelve inferior
    limite = Nuevo_enfoque.encontrar_limites_inferior_gravedad(0)
    assert limite == 0

    limite = Nuevo_enfoque.encontrar_limites_inferior_gravedad(1)
    assert limite == 1

    limite = Nuevo_enfoque.encontrar_limites_superior_gravedad(1)
    assert limite == 3

    #Si es superior me devuelve el limite superior
    limite = Nuevo_enfoque.encontrar_limites_inferior_gravedad(2)
    assert limite == 3

def test_orden_insersion_MismaGravedad():
    paciente_1 = cPaciente("N-a-R", "Naranja",1,None,None,None)
    paciente_2 = cPaciente("A-a-N", "Amarillo",1,None,None,None)
    paciente_4 = cPaciente("A-a-N1", "Amarillo",1,None,None,None)
    Organizador = cNuevoEnfoque()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    Organizador.insert(paciente_4)
    paciente_1.setTiempoLlegada(dt.datetime.now() - dt.timedelta(minutes=10))
    Organizador.Reorganizar()
    paciente_obtenido_1 = Organizador.Lista_de_pacientes[0]
    paciente_obtenido_2 = Organizador.Lista_de_pacientes[1]
    paciente_obtenido_3 = Organizador.Lista_de_pacientes[2]

    assert paciente_obtenido_1 == paciente_1
    assert paciente_obtenido_2 == paciente_2
    assert paciente_obtenido_3 == paciente_4


    assert paciente_obtenido_1.getGravedad() == 0
    assert paciente_obtenido_2.getGravedad() == 2
    assert paciente_obtenido_3.getGravedad() == 2
def test_Nuevo_enfoque_Reorganizar():
    paciente_1 = cPaciente("Julian", "Naranja",1,None,None,None)
    paciente_2 = cPaciente("Julian2", "Verde",1,None,None,None)
    Organizador = cNuevoEnfoque()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    paciente_1.setTiempoLlegada(dt.datetime.now() - dt.timedelta(minutes=10))
    Organizador.Reorganizar()
    paciente_obtenido=Organizador.Lista_de_pacientes[0]
    assert paciente_obtenido==paciente_1
    assert paciente_obtenido.getGravedad()==0

def test_Nuevo_enfoque_Reorganizar_un_par():
    paciente_1 = cPaciente("N-a-R", "Naranja",1,None,None,None)
    paciente_2 = cPaciente("A-a-N", "Amarillo",1,None,None,None)
    Organizador = cNuevoEnfoque()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    paciente_1.setTiempoLlegada(dt.datetime.now() - dt.timedelta(minutes=10))
    paciente_2.setTiempoLlegada(dt.datetime.now() - dt.timedelta(minutes=60))
    Organizador.Reorganizar()
    paciente_obtenido_1=Organizador.Lista_de_pacientes[0]
    paciente_obtenido_2=Organizador.Lista_de_pacientes[1]
    assert paciente_obtenido_1==paciente_1
    assert paciente_obtenido_2==paciente_2
    assert paciente_obtenido_1.getGravedad()==0
    assert paciente_obtenido_2.getGravedad()==1
def test_Nuevo_enfoque_Reorganizar_conjugados():
    paciente_1 = cPaciente("N-a-R", "Naranja",1,None,None,None)
    paciente_2 = cPaciente("A-a-N", "Amarillo",1,None,None,None)
    paciente_4 = cPaciente("A-a-N 1", "Amarillo",1,None,None,None)
    Organizador = cNuevoEnfoque()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    Organizador.insert(paciente_4)
    paciente_1.setTiempoLlegada(dt.datetime.now() - dt.timedelta(minutes=10))
    paciente_2.setTiempoLlegada(dt.datetime.now() - dt.timedelta(minutes=60))
    Organizador.Reorganizar()
    paciente_obtenido_1 = Organizador.Lista_de_pacientes[0]
    paciente_obtenido_2 = Organizador.Lista_de_pacientes[1]
    paciente_obtenido_3 = Organizador.Lista_de_pacientes[2]

    assert paciente_obtenido_1.getGravedad() == 0
    assert paciente_obtenido_2.getGravedad() == 1
    assert paciente_obtenido_3.getGravedad() == 2

"""
hay que fixearlo 
def test_Nuevo_enfoque_Reorganizar_Multiples_Pacientes():
    Organizador = cNuevoEnfoque()
    Lista_Pacientes = []
    Enum = ["rojo", "naranja", "amarillo", "verde", "azul"]
    cant = 20  # seteo el numero de pacientes
    # AGREGO 20 PACIENTES A UNA LISTA
    for i in range(0, cant):
        nombre = "" + str(i)  # seteo el nombre de los pacientes
        gravedad = i % 5  # seteo la gravedad de forma que la gravedad de los pacientes es ciclica de 0 a 4
        pac = cPaciente(nombre, Enum[gravedad], 1, None, None, None)  # El seteo de la gravedad es al estilo enum
        Lista_Pacientes.append(pac)  # agrego al paciente a la listas de pacientes
        Organizador.insert(pac)  # agrego al paciente a
    # cambio la gravedad de 3 pacientes que son categoria azul a la verde
    for j in range(2, cant - 5, 5):
        Lista_Pacientes[j].setTiempoLlegada(Lista_Pacientes[j].getTiempoLLegada() - dt.timedelta(minutes=61))
    # cambio la gravedad de 3 pacientes que son categoria amarilla a la naranja
    for t in range(4, cant - 5, 5):
        Lista_Pacientes[t].setTiempoLlegada(Lista_Pacientes[t].getTiempoLLegada() - dt.timedelta(minutes=241))
     #cambio la gravedad de 3 paciente que son categoría naranja
    for t in range(1, cant - 5, 5):
        Lista_Pacientes[t].setTiempoLlegada(Lista_Pacientes[t].getTiempoLLegada() - dt.timedelta(minutes=11))
    

    Para poder probar si el test cambio bien de gravedad a los pacientes que esperaron mucho en la
    sala de espera tengo que recorrer todo el arreglo de lista pacientes y ir sumando uno por uno
     Organizador.Reorganizar()
    #contadores
    rojo=0
    naranja=0
    amarillo=0
    verde=0
    azul=0
    for i in range(0,len(Organizador.Lista_de_pacientes)):
        if(Lista_Pacientes[i].getGravedad()==0):
            rojo=rojo+1
        if (Lista_Pacientes[i].getGravedad() == 1):
            naranja = naranja + 1
        if (Lista_Pacientes[i].getGravedad() == 2):
            amarillo = amarillo + 1
        if (Lista_Pacientes[i].getGravedad() == 3):
            verde = verde + 1
        if (Lista_Pacientes[i].getGravedad() == 4):
            azul = azul + 1

    assert naranja== 7
    assert verde == 7"""