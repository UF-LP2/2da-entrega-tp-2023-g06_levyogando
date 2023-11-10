import datetime as dt
from .cManejoArchivo import *
from .Errores.cErrorTamanio import cErrorTamanio
from .Errores.cErrorGravedad import cErrorGravedad
from .Errores.cErrorPaciente import cErrorPaciente

class cNuevoEnfoque:
    def __init__(self):
        self.Lista_de_pacientes = []
        self.Handler = cManejoArchivo()

    def Reorganizar(self, indice_lista=None):
        if(indice_lista==None):
            indice_lista = len(self.Lista_de_pacientes)-1

        if indice_lista ==0:
            obj_act = self.Lista_de_pacientes[indice_lista]
            if(obj_act.getGravedad()==0):
                return 1
            else:
                obj_act = self.Lista_de_pacientes.pop(indice_lista)
                num = obj_act.setGravedadMayorPaciente()
                limite = self.encontrar_limites_inferior_gravedad(num)
                self.Lista_de_pacientes.insert(limite, obj_act)
                return 1

        if indice_lista == -1:
            return 1

        if(self.Lista_de_pacientes[indice_lista] is None):
            return 1

        obj_act = self.Lista_de_pacientes[indice_lista]
        if obj_act.getTiempoRestante() > obj_act.getTiempoRestanteMayorGravedad():
            num = obj_act.getGravedad()
            limite = self.encontrar_limites_inferior_gravedad(num)
            if(limite == indice_lista):
                return self.Reorganizar(limite-1)
            return self.Reorganizar(limite)
        else:
            obj_act = self.Lista_de_pacientes.pop(indice_lista)
            num = obj_act.setGravedadMayorPaciente()
            limite = self.encontrar_limites_inferior_gravedad(num) +1
            self.Lista_de_pacientes.insert(limite,obj_act)
            return self.Reorganizar(indice_lista-1)

    def encontrar_limites_inferior_gravedad(self,cual_es_limite_con_una_gravedad_mayor,lista=None, inicio=0, fin=None):
        """
        En este metodo buso cual sería el limite con una gravedad mayor (osea la posicion de la izquierda)
        :param lista:
        :param cual_es_limite_con_una_gravedad_mayor:
        :param inicio:
        :param fin:
        :return:
        """
        if lista is None:
            lista = self.Lista_de_pacientes

        if fin is None:
            fin = len(lista) - 1

        if inicio > fin:
            return 0

        if inicio > fin:
            return None  # No se encontró el límite

        mid = (inicio + fin) // 2

        if lista[mid].getGravedad()  == cual_es_limite_con_una_gravedad_mayor:
            # Si el elemento en la posición media es igual al objetivo, hemos encontrado el límite
            return mid
        elif lista[mid].getGravedad() < cual_es_limite_con_una_gravedad_mayor:
            # El objetivo está a la derecha del medio
            return self.encontrar_limites_inferior_gravedad(cual_es_limite_con_una_gravedad_mayor,lista, mid + 1, fin)
        else:
            # El objetivo está a la izquierda del medio
            return self.encontrar_limites_inferior_gravedad(cual_es_limite_con_una_gravedad_mayor,lista, inicio, mid - 1)

    def encontrar_limites_superior_gravedad(self,cual_es_limite_con_una_gravedad_menor,lista=None,  inicio=0, fin=None):

        if lista is None:
            lista = self.Lista_de_pacientes

        if fin is None:
            fin = len(lista) - 1

        if inicio > fin:
            return None  # No se encontró el límite superior

        mid = (inicio + fin) // 2

        if lista[mid].getGravedad() == cual_es_limite_con_una_gravedad_menor:
            # Mientras el siguiente elemento también sea igual al objetivo, seguimos buscando a la derecha, mas grandes
            next_index = mid + 1
            while lista[next_index].getGravedad() <= lista[fin].getGravedad() and lista[next_index].getGravedad() == cual_es_limite_con_una_gravedad_menor:
                next_index += 1
            return next_index
        elif lista[mid].getGravedad() < cual_es_limite_con_una_gravedad_menor:
            # El objetivo está a la derecha del medio
            return self.encontrar_limites_superior_gravedad(cual_es_limite_con_una_gravedad_menor, lista, mid + 1, fin)
        else:
            # El objetivo está a la izquierda del medio
            return self.encontrar_limites_superior_gravedad(cual_es_limite_con_una_gravedad_menor, lista, inicio, mid - 1)

    def insert(self, _paciente):
        try:
            num = -1
            try:
                num = _paciente.getGravedad()
            except cErrorGravedad("En el insert") as err:
                num = _paciente.setGravedadMayorPaciente()
            self.Lista_de_pacientes = self.InsertDyC(self.Lista_de_pacientes,_paciente)
        except cErrorTamanio("Error en el insert") as errorTam:
            print(cErrorTamanio)

    def InsertDyC(self,lista,_paciente):
        if not lista:
            return [_paciente]
        num = _paciente.getGravedad()
        mid = len(lista)//2

        if(len(lista)==1):
            if(num>=lista[0].getGravedad()):
                lista.append((_paciente))
                return lista
            else:
                lista_aux=[]
                lista_aux.append(_paciente)
                lista_aux.append(lista[0])
                return lista_aux
        if num>=lista[mid].getGravedad():
            return lista[:mid] + self.InsertDyC(lista[mid:],_paciente)
        else:
            return self.InsertDyC(lista[:mid],_paciente) + lista[mid:]

    def ObtenerProximo(self):
        if len(self.Lista_de_pacientes) > 0:
            return self.Lista_de_pacientes.pop(0)
        else:
            raise cErrorTamanio("No hay pacientes a atender")

    def DerivarProximo(self):
        """En este metodo guasrdamos en el archivo al paciente mas importante"""
        self.Handler.agregar_paciente(self.ObtenerProximo())

    def Reorganizar_greedy(self, p):

        if p.getGravedad() != 0:
            tiempo = p.getTiempoLlegada()
            fecha = dt.timedelta(0, 0, 0, 0, tiempo.minute, tiempo.hour, 0)
            hora = dt.datetime.now()
            ahora = dt.timedelta(0, 0, 0, 0, hora.minute, hora.hour, 0)
            diferencia = (ahora - fecha).total_seconds() / 60
            minutos = p.get_tiempo_gravedad()
            ola = minutos.total_seconds() / 60

            if (diferencia > ola):
                self.Cambiar_color_greedy(p)

    def Cambiar_color_greedy(self, p):

        p.set_gravedad(p.getGravedad() - 1)  # el paciente tiene un nuevo color
        self.Cambiar_Paciante_greedy(p)

    def Limite_Color_R(self):
        tam = len(self.Lista_de_pacientes) - 1
        if len(self.Lista_de_pacientes) == 0:
            raise cErrorTamanio("No hay pacientes a atender")
        if len(self.Lista_de_pacientes) == 1 and self.Lista_de_pacientes[0].getGravedad() == 0:
            return 0  # solo hay un paciente rojo
        if self.Lista_de_pacientes[tam + 1].getGravedad() == 0:
            return tam
        elif len(self.Lista_de_pacientes) > 1:
            for x in range(tam):
                if self.Lista_de_pacientes[x].getGravedad() == 0 and self.Lista_de_pacientes[x + 1].getGravedad() != 0:
                    return x
        else:
            raise cErrorTamanio("RARO")

    def Limite_Color_N(self):
        tam = len(self.Lista_de_pacientes) - 1
        if len(self.Lista_de_pacientes) == 0:
            raise cErrorTamanio("No hay pacientes a atender")
        if len(self.Lista_de_pacientes) == 1 and self.Lista_de_pacientes[0].getGravedad() == 1:
            return 0
        if self.Lista_de_pacientes[tam].getGravedad() == 1:
            return tam
        elif len(self.Lista_de_pacientes) > 1:
            for x in range(tam):
                if self.Lista_de_pacientes[x].getGravedad() == 1 and self.Lista_de_pacientes[x + 1].getGravedad() != 1:
                    return x
        else:
            raise cErrorTamanio("RARO")

    def Limite_Color_AM(self):
        tam = len(self.Lista_de_pacientes) - 1
        if len(self.Lista_de_pacientes) == 0:
            raise cErrorTamanio("No hay pacientes a atender")
        if len(self.Lista_de_pacientes) == 1 and self.Lista_de_pacientes[0].getGravedad() == 2:
            return 0  # solo hay un paciente rojo
        if self.Lista_de_pacientes[tam].getGravedad() == 2:
            return tam
        elif len(self.Lista_de_pacientes) > 1:
            for x in range(tam):
                if self.Lista_de_pacientes[x].getGravedad() == 2 and self.Lista_de_pacientes[x + 1].getGravedad() != 2:
                    return x
        else:
            raise cErrorTamanio("RARO")

    def Limite_Color_V(self):
        tam = len(self.Lista_de_pacientes) - 1
        if len(self.Lista_de_pacientes) == 0:
            raise cErrorTamanio("No hay pacientes a atender")
        if len(self.Lista_de_pacientes) == 1 and self.Lista_de_pacientes[0].getGravedad() == 3:
            return 0  # solo hay un paciente rojo
        if self.Lista_de_pacientes[tam].getGravedad() == 3:
            return tam
        elif len(self.Lista_de_pacientes) > 1:
            for x in range(tam):
                if self.Lista_de_pacientes[x].getGravedad() == 3 and self.Lista_de_pacientes[x + 1].getGravedad() != 3:
                    return x
        else:
            raise cErrorTamanio("RARO")

    def Cambiar_Paciante_greedy(self, p):
        if p.getGravedad() == 0:
            lim = self.Limite_Color_R()
            self.Lista_de_pacientes.insert(lim, p)
        if p.getGravedad() == 1:
            lim = self.Limite_Color_N()
            self.Lista_de_pacientes.insert(lim, p)
        if p.getGravedad() == 2:
            lim = self.Limite_Color_AM()
            self.Lista_de_pacientes.insert(lim, p)
        if p.getGravedad() == 3:
            lim = self.Limite_Color_V()
            self.Lista_de_pacientes.insert(lim, p)

    def Insertar_gr(self, p):
        if p.getGravedad() == 0:
            lim = self.Limite_Color_R()
            self.Lista_de_pacientes.insert(lim, p)
        if p.getGravedad() == 1:
            lim = self.Limite_Color_N()
            self.Lista_de_pacientes.insert(lim, p)
        if p.getGravedad() == 2:
            lim = self.Limite_Color_AM()
            self.Lista_de_pacientes.insert(lim, p)
        if p.getGravedad() == 3:
            lim = self.Limite_Color_V()
            self.Lista_de_pacientes.insert(lim, p)
        else:
            self.Lista_de_pacientes.append(p)  # es azul