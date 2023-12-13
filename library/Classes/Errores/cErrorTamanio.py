class cErrorTamanio(BaseException):
    def __init__(self, lugar):
        self.txt = lugar

    def print(self):
        print("Error en el tamaño en: " + self.txt)
