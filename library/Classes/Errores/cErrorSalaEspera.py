class cErrorSalaEspera(BaseException):
    def __init__(self, lugar):
        self.txt = lugar

    def print(self):
        print("Error Sala de Espera en: " + self.txt)