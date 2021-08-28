from threading import Thread
import math
import time
import timeit
import argparse
# los comandos anteriores importan módulos para realizar operaciones
# Declaración de variable global


def square_numbers(lista):
    for i in range(len(lista)):
        lista[i] = math.pow(lista[i], 2.0)
        time.sleep(0.01)
# esta función combierte a los elementos del array que recibe
# en sus cuadraados


def array(x):
    a = []
    n = 0
    # declaración de variables necesaria para realizar el array
    while(n <= x):
        a.append(n)
        n = n + 1
# esta función crea una lista con x elementos
# siendo la entrada que el usuario define
    return a


if __name__ == "__main__":
    # Aquí empieza el main
    parser = argparse.ArgumentParser(description="Elementos al cuadrado")
    parser.add_argument("X", type=int, help="Número de elementos del array")
    parser.add_argument("-t", type=str, help="En terminal o en .txt")
    argument = parser.parse_args()
    # los comandos anteriores permiten que el usuario defina
    # la entrada en el Shell
    value = argument.X
    shared_array = array(value-1)
    hilos = shared_array[:]
    thread1 = Thread(target=square_numbers, args=(shared_array,))
    starttime = timeit.default_timer()
    thread1.start()
    thread1.join()
    finaltime1 = timeit.default_timer() - starttime
    # Los comandos anteriores declaran el hilo 1
    # y le miden el tiempo de ejecucion del calculo
    tamañoentre4 = int(len(hilos)/4)
    if len(hilos) >= 4:
        array1 = hilos[0:tamañoentre4]
        array2 = hilos[tamañoentre4:tamañoentre4*2]
        array3 = hilos[tamañoentre4*2:tamañoentre4*3]
        array4 = hilos[tamañoentre4*3:len(hilos)]
        thread2 = Thread(target=square_numbers, args=(array1,))
        thread3 = Thread(target=square_numbers, args=(array2,))
        thread4 = Thread(target=square_numbers, args=(array3,))
        thread5 = Thread(target=square_numbers, args=(array4,))
    else:
        thread2 = Thread(target=square_numbers, args=(hilos,))
        thread3 = Thread(target=square_numbers, args=([],))
        thread4 = Thread(target=square_numbers, args=([],))
        thread5 = Thread(target=square_numbers, args=([],))
    starttime = timeit.default_timer()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    if len(hilos) >= 4:
        hilos = array1+array2+array3+array4
        finaltime4 = timeit.default_timer() - starttime
# los comandos anteriores declaran los 4 hilos,
# miden el tiempo de ejecucion del calculo
# crean el array con los resultados
    if argument.t == "t":
        print("Tiempo 1 hilo: ", finaltime1)
        print("Tiempo 4 hilo: ", finaltime4)
    elif argument.t == "txt":
        f = open("Tiempos.txt", "w")
        f.write("Tiempo 1 hilo: " + str(finaltime1) + "\n")
        f.write("Tiempo 4 hilos: " + str(finaltime4))
        f.close()
    else:
        print("Tiempo 1 hilo: ", finaltime1)
        print("Tiempo 4 hilo: ", finaltime4)
# estas condiciones se encargan de mostrar
# el formato de impresion de resultados
