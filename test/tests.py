import datetime as dt
#import random

import pytest
from Classes.cQuesMaestra import *
from Classes.cManejoArchivo import *
from Classes.cSalaEspera import cSalaEspera
from Classes import cRandoms
def test_Error_Insercion_Gravedad():
    """
    Este test tiene que asertar si al paciente se lo instancia con una gravedad distinta a las posibles
    :return:
    """
    with pytest.raises(cErrorGravedad):
        paciente_1 = cPaciente("Julian", "-",1,None,None,None)

def test_Paciente_Indepndendica_Gravedad_MayusMinus():
    """
    Este test tiene que asertar al darle a diferentes pacientes la misma gravedad si se escribe diferente
        :return:
    """
    paciente_1 = cPaciente("Julian", "AZUL",1,None,None,None)
    paciente_2 = cPaciente("andres", "azul",1,None,None,None)
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


def test_cQuesMaestra_Insertar():
    paciente_1 = cPaciente("Julian1", "rojo",1,None,None,None)
    paciente_2 = cPaciente("Julian2", "naranja",1,None,None,None)
    paciente_3 = cPaciente("Julian3", "amarillo",1,None,None,None)
    paciente_4 = cPaciente("Julian4", "verde",1,None,None,None)
    paciente_5 = cPaciente("Julian5", "azul",1,None,None,None)
    Organizador = cQuesMaestra()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    Organizador.insert(paciente_3)
    Organizador.insert(paciente_4)
    Organizador.insert(paciente_5)
    assert Organizador.R.qsize() == 1
    assert Organizador.N.qsize() == 1
    assert Organizador.AM.qsize() == 1
    assert Organizador.V.qsize() == 1
    assert Organizador.AZ.qsize() == 1

def test_cQuesMaestra_Obtener():
    paciente_1 = cPaciente("Julian1", "rojo",1,None,None,None)
    paciente_2 = cPaciente("Julian2", "naranja",1,None,None,None)
    paciente_3 = cPaciente("Julian3", "amarillo",1,None,None,None)
    paciente_4 = cPaciente("Julian4", "verde",1,None,None,None)
    paciente_5 = cPaciente("Julian5", "azul",1,None,None,None)
    Organizador = cQuesMaestra()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    Organizador.insert(paciente_3)
    Organizador.insert(paciente_4)
    Organizador.insert(paciente_5)
    assert Organizador.Lista_de_colas[3].get() == paciente_4
    assert Organizador.Lista_de_colas[2].get() == paciente_3
    assert Organizador.Lista_de_colas[4].get() == paciente_5
    assert Organizador.Lista_de_colas[1].get() == paciente_2
    assert Organizador.Lista_de_colas[0].get() == paciente_1
def test_cQuesMaestra_Reorganizar():
    paciente_1 = cPaciente("Julian", "Naranja",1,None,None,None)
    paciente_2 = cPaciente("Julian2", "Verde",1,None,None,None)
    Organizador = cQuesMaestra()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    paciente_1.setTiempoLlegada( dt.datetime.now() - dt.timedelta(minutes=10))
    Organizador.Reorganizar()
    paciente_obtenido=Organizador.Lista_de_colas[0].get()
    assert paciente_obtenido==paciente_1

def test_cQuesMaestra_Reorganizar_Multiples_Pacientes():
    Organizador = cQuesMaestra()
    Lista_Pacientes=[]
    Enum=["rojo","naranja","amarillo","verde","azul"]
    cant = 20 #seteo el numero de pacientes
    # AGREGO 20 PACIENTES A UNA LISTA
    for i in range(0,cant):
        nombre = ""+str(i) #seteo el nombre de los pacientes
        gravedad = i%5 #seteo la gravedad de forma que la gravedad de los pacientes es ciclica de 0 a 4
        pac = cPaciente(nombre,Enum[gravedad],1,None,None,None) #El seteo de la gravedad es al estilo enum
        Lista_Pacientes.append(pac)#agrego al paciente a la listas de pacientes
        Organizador.insert(pac)#agrego al paciente a
    #cambio la gravedad de 3 pacientes que son categoria azul a la verde
    for j in range(2,cant-5,5):
        Lista_Pacientes[j].setTiempoLlegada(Lista_Pacientes[j].getTiempoLLegada() - dt.timedelta(minutes=61))
    # cambio la gravedad de 3 pacientes que son categoria amarilla a la naranja
    for t in range(4,cant-5,5):
        Lista_Pacientes[t].setTiempoLlegada(Lista_Pacientes[t].getTiempoLLegada() - dt.timedelta(minutes=241))
    """ #cambio la gravedad de 3 paciente que son categoría naranja
    for t in range(1, cant - 5, 5):
        Lista_Pacientes[t].setTiempoLlegada(Lista_Pacientes[t].getTiempoLLegada() - dt.timedelta(minutes=11))
    """
    Organizador.Reorganizar()
    assert Organizador.N.qsize()==7
    assert Organizador.V.qsize()==7

def test_cQuesMaestra_Reorganizar_Multiples_Rojos_Sin_posibilidad_atencion():
    Organizador = cQuesMaestra()
    Lista_Pacientes=[]
    Enum=["rojo","naranja","amarillo","verde","azul"]
    cant = 20 #seteo el numero de pacientes
    # AGREGO 20 PACIENTES A UNA LISTA
    for i in range(0,cant):
        nombre = ""+str(i) #seteo el nombre de los pacientes
        gravedad = i%5 #seteo la gravedad de forma que la gravedad de los pacientes es ciclica de 0 a 4
        pac = cPaciente(nombre,Enum[gravedad],1,None,None,None) #El seteo de la gravedad es al estilo enum
        Lista_Pacientes.append(pac)#agrego al paciente a la listas de pacientes
        Organizador.insert(pac)#agrego al paciente a

    # cambio la gravedad de 3 pacientes que son categoria azul a la roja
    for t in range(4, cant - 5, 5):
        Lista_Pacientes[t].setTiempoLlegada( Lista_Pacientes[t].getTiempoLLegada() - dt.timedelta(minutes=431))

    #cambio la gravedad de 3 pacientes que son categoria amarilla a la roja
    for j in range(2,cant-5,5):
        Lista_Pacientes[j].setTiempoLlegada( Lista_Pacientes[j].getTiempoLLegada() - dt.timedelta(minutes=71))

    #cambio la gravedad de 3 paciente que son categoría naranja a roja
    for t in range(1, cant - 5, 5):
        Lista_Pacientes[t].setTiempoLlegada( Lista_Pacientes[t].getTiempoLLegada() - dt.timedelta(minutes=10))
    Organizador.Reorganizar()
    assert Organizador.R.qsize()==13

def test_lectura_archivo():
    #creo el objeto enfermero
    enfermero=cEnfermero("ale","Mn 124121")

    #creo el objeto paciente
    cPaciente_aux = cPaciente("non", "azul", "0", "-", enfermero,"f")
    paciente_con_triage=enfermero.Clasificar("paciente 1","rojo",6354,9,"lo operaron de la rodillita ")


    #Trabajo con el operador de archivo
    handler = cManejoArchivo()
    handler.agregar_paciente(paciente_con_triage)
    cPaciente_aux=handler.buscar_en_archivo_paciente("paciente 1",paciente_con_triage.getTiempoLLegada())
    assert paciente_con_triage == cPaciente_aux




