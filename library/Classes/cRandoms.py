import random

# Listas de nombres y edades ficticias
nombres = ["Juan", "María", "José", "Ana", "Carlos", "Sofía", "Diego", "Luis", "Valentina", "Andrés", "Camila", "Miguel", "Isabella", "Javier", "Fernanda", "Manuel", "Valeria", "Alejandro", "Renata", "Gustavo", "Catalina", "Santiago", "Lucía", "Lorenzo", "Victoria", "Rafael", "Adriana", "Gabriel", "Antonella"]
edades = list(range(18, 71))  # Edades entre 18 y 70 años
colores = ["azul", "amarillo", "naranja", "verde", "rojo"]

def obtener_randoms_nombre():
    return random.choice(nombres)

def obtener_random_edad():
    return random.choice(edades)

def color_aleatorio():
    color_aleatorio = random.choice(colores)
    return color_aleatorio