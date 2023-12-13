class cErrorGravedad(BaseException):
    def __init__(self, lugar):
        self.txt = lugar

    def imprimir(self):
        print("Error cErrorGravedad en: " + self.txt)
