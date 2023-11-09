#import datetime

import os
import pandas as pd
from .cEnfermero import *
class cManejoArchivo:
    def __init__(self, archivo_csv=None):

        directorio_actual = os.path.dirname(__file__)
        carpeta_superior = os.path.join(directorio_actual,
                                        "../../../Laboratorio de programacion 2/G06_LevyOgando_Triage")
        archivo_csv = os.path.join(carpeta_superior, "lista_pacientes.csv")

        if archivo_csv==None or not os.path.isfile(archivo_csv):
            self._archivo_csv = archivo_csv
            self._base_de_pacientes = pd.DataFrame(
                columns=["Nombre", "Edad", "Gravedad", "Historial", "Enfermero", "Fecha", "Caso Clinico"])
            self.guardar_archivo()  # Guardar el archivo nuevo

        else:
            # El archivo ya existe, cargar los datos
            self._archivo_csv = archivo_csv
            self._base_de_pacientes = pd.read_csv(self._archivo_csv)
    def agregar_paciente(self, paciente):
        enfermero= paciente.getEnfermero()
        nuevo_paciente = pd.DataFrame(
            {"Nombre": [paciente.getNombre()], "Edad": [paciente.getEdad()], "Gravedad": [paciente.getGravedad()],
             "Historial": [paciente.getHistorial()], "Enfermero": [enfermero.getNombreEnfermero()],
             "Matricula": [enfermero.getMatricula()],
             "Caso Clinico": [paciente.getCasoClinico()],
             "Fecha": [paciente.getTiempoLLegada()]})
        self._base_de_pacientes = pd.concat([self._base_de_pacientes, nuevo_paciente], ignore_index=True)
        self.guardar_archivo()



    def editar_paciente(self, nombre,fecha, nueva_edad, nueva_gravedad, nuevo_historial, nuevo_enfermero):
        paciente = self.busqueda_interna(nombre, fecha)
        if paciente is not None:
            self._base_de_pacientes.at[paciente.index, "Edad"] = nueva_edad
            self._base_de_pacientes.at[paciente.index, "Gravedad"] = nueva_gravedad
            self._base_de_pacientes.at[paciente.index, "Historial"] = nuevo_historial
            self._base_de_pacientes.at[paciente.index, "Enfermero"] = nuevo_enfermero
            self.guardar_archivo()  # Guardar el DataFrame actualizado
            return True
        else:
            return False

    def leer_otro_archivo(self, archivo_csv_otro):
        try:
            pacientes_otro = pd.read_csv(archivo_csv_otro)
            self._base_de_pacientes = pd.concat([self._base_de_pacientes, pacientes_otro], ignore_index=True)
            self.guardar_archivo()
            return True
        except FileNotFoundError:
            return False

    def guardar_archivo(self):
        self._base_de_pacientes.to_csv(self._archivo_csv, index=False)
        print(f"Archivo con paciente derivado guardado en {self._archivo_csv}")

    def obtener_indice_paciente(self, nombre, fecha):
        paciente = self.buscar_paciente(nombre, fecha)
        if paciente is not None:
            return paciente.index
        else:
            return None

    def busqueda_interna(self, nombre, fecha):
        # Filtra el DataFrame en función del nombre y la fecha
        pacientes_filtrados = self._base_de_pacientes[
            (self._base_de_pacientes["Nombre"] == nombre) & (self._base_de_pacientes["Fecha"] == fecha)
            ]

        # Si no se encontraron pacientes, devuelve None
        if pacientes_filtrados.empty:
            return None

        # Devuelve el DataFrame correspondiente al paciente encontrado
        return pacientes_filtrados

    def BusquedaUltimo(self):
        indice_max_valor = self._base_de_pacientes['Caso Clinico'].idxmax()
        caso_clinico_mas_grande = self._base_de_pacientes.loc[indice_max_valor]['Caso Clinico']
        return caso_clinico_mas_grande

    def buscar_en_archivo_paciente(self, nombre,fecha):
        # Filtra el DataFrame en función del nombre y la fecha
        pacientes_filtrados = self._base_de_pacientes[
            (self._base_de_pacientes["Nombre"] == nombre) & (self._base_de_pacientes["Fecha"] == fecha)
            ]

        # Si no se encontraron pacientes, devuelve None
        if pacientes_filtrados.empty:
            return None

        # Extrae los datos del primer paciente encontrado
        paciente_data = pacientes_filtrados.iloc[0]

        _color = 0
        if(paciente_data["Gravedad"]==0):
            _color = "rojo"
        elif(paciente_data["Gravedad"]==1):
            _color = "naranja"
        elif (paciente_data["Gravedad"] == 2):
            _color = "amarillo"
        elif (paciente_data["Gravedad"] == 3):
            _color = "verde"
        elif (paciente_data["Gravedad"] == 4):
            _color = "azul"

        #Creo el Objeto Enfermero
        enfermero = cEnfermero(paciente_data["Enfermero"],paciente_data["Matricula"])

        # Crea un objeto cPaciente con los datos extraídos
        paciente = cPaciente(
            paciente_data["Nombre"],
            _color, #le agrego la clase gravedad
            paciente_data["Edad"],
            paciente_data["Caso Clinico"],
            enfermero, #le agrego la clase enfermero
            paciente_data["Historial"]
        )

        return paciente

    def obtener_ultimos_datos(self):
        ultimos_datos = self._base_de_pacientes.tail(5)
        return ultimos_datos

    def pacientes_buscando_cama(self):
        """
        Devuelve una lista de pacientes que están buscando una cama en función del historial.
        """
        if "Historial" not in self._base_de_pacientes.columns:
            # Asegúrate de que la columna "Historial" existe en el DataFrame
            return []

        pacientes_buscando_cama = self._base_de_pacientes[self._base_de_pacientes["Historial"] == "Buscando Cama"]
        return pacientes_buscando_cama
