"""
    Juego de la Vida para consola en Python
    
    Autor: Julian Ariel Campana
"""
import os
import random
import time

#Constantes
DELAY = 0.5
STEPS = 100

def start_grid_from_file():
        """
        Lee el archivo de texto generacion_inicial.txt y extrae los
        datos para crear una grilla.
        El archivo debe contener solo asteriscos y puntos:
            -Celulas Vivas: "*"
            -Celulas Muertas:"."
        Por cuestiones de diseño, la primera se debe crear un borde
        con cualquiera de los carateres alrededor de la grilla en el
        archivo para poder crear un borde en el programa. 
        """
        array = []
        with open("generacion_inicial.txt", "r") as f:
            for line in f:
                temp = []
                for char in line:
                    if char == "*":
                        temp.append(1)
                    elif char == ".":
                        temp.append(0)
                array += [temp]

        # Añade los bordes que no se encuentran inicialmente en el archivo, a la grilla
        for i in range(len(array)):
            for j in range(len(array[0])):
                if (i == 0 or j == 0 or (i == len(array) - 1) or (j == len(array[0]) - 1)):
                    array[i][j] = -1

        return array

def start_empty_grid(filas, cols):
    """
    Crea una grilla vacia para utilizar de auxiliar en el calculo
    de las proximas generaciones de celulas
    """
    array = []

    for i in range(filas):
        single_row = []
        for j in range(cols):
            single_row.append(0)
        array.append(single_row)
    return array

def start_random_grid(filas, cols):
    """
    Crea una grilla en base al tamaño elegido e inicia sus valores 
    aleatoriamente.
    """
    array = []

    for i in range(filas):
        single_row = []
        for j in range(cols):
            if(i == 0 or j == 0 or i == filas - 1 or j == cols - 1 ):
                single_row.append(-1)
            else:
                ran = random.randint(0,3)
                if ran == 0:
                    single_row.append(1)
                else:
                    single_row.append(0)
        array.append(single_row)

    return array

def check_neighbors(fila, col, cur_gen):
    """
    Esta funcion itera por sobre todas las celulas y cuenta la cantidad
    de celulas vecinas que se encuentran vivas. En base a esto comprueba
    las reglas del juego de la vida:
        -Una celda viviente sobrevive únicamente si tiene 2 o 3 celdas vecinas vivas
        -El nacimiento de una nueva celda se da si esta tiene exactamente 3 celdas vivas vecinas
    Devuelve el valor de la celula correspondiente.
    """
    neighbor_count = 0

    for i in range(fila-1, fila+2):
        for j in range(col-1, col+2):
            if not(i == fila and j == col):
                if cur_gen[i][j] != -1:
                    neighbor_count += cur_gen[i][j]

    if cur_gen[fila][col] == 1 and neighbor_count < 2:
        return 0
    if cur_gen[fila][col] == 1 and neighbor_count > 3:
        return 0
    if cur_gen[fila][col] == 0 and neighbor_count == 3:
        return 1
    else:
        return cur_gen[fila][col]

def process_next_gen(filas, cols, cur_gen, next_gen):
    """
    Itera sobre todas las celulas de la generacion actual chequeando
    en cada una de ellas el proximo estado de la grilla.
    """
    for i in range(0, filas-1):
        for j in range(0, cols-1):
            next_gen[i][j] = check_neighbors(i, j, cur_gen)

def print_gen(filas, cols, cur_gen, step):
    """
    Itera sobre la generación actual y representa:
        1 (Celula Viva): Cuadrado negro
        0 (Celula Muerta): Espacio en blanco
    """
    clear_screen()
    print("Simulación del Juego de la Vida. Generación : " + str(step + 1))

    for i in range(filas):
        for j in range(cols):
            if cur_gen[i][j] == -1:
                print("#", end = " ")
            elif cur_gen[i][j] == 1:
                print(u"\u25A0", end = " ")
            elif cur_gen[i][j] == 0:
                print(" ", end = " ")
        print("\n")

def clear_screen():
    """
    Función para limpiar la consola en función del SO
    """
    os.system("cls" if os.name == "nt" else "clear")

def start_simulation(filas, cols, cur_gen, steps, delay):
    """
    Esta funcion crea un grilla vacia del mismo tamaño que la
    inicial para utlizar de auxiliar y comienza a calcular las
    proximas generaciones hasta la cantidad de steps seteado
    previamente.
    """
    next_gen = start_empty_grid(filas, cols)

    for step in range(steps):
        print_gen(filas, cols, cur_gen, step)
        process_next_gen(filas, cols, cur_gen, next_gen)
        time.sleep(delay)

        cur_gen, next_gen = next_gen, cur_gen
    input("Simulación finalizada. Presione cualquier tecla para salir del programa...")

if __name__ == '__main__':
    print("Elije una opción: ")
    print("1: Leer estado inicial desde grilla 'grid.txt'")
    print("2: Generate random grind of size 10X10")

    choice = int(input("Opción: "))

    if choice == 1:
        this_gen = start_grid_from_file()
        
        filas = len(this_gen)
        cols = len(this_gen[0])

        start_simulation(filas, cols, this_gen, STEPS, DELAY)
    elif choice == 2:
        filas = 12
        cols = 12

        this_gen = start_random_grid(filas, cols)

        start_simulation(filas, cols, this_gen, STEPS, DELAY)