class cErrorPaciente(BaseException):
    def __init__(self, lugar):
        self.txt = lugar

    def imprimir(self):
        print("Error cErrorPaciente en: " + self.txt)
