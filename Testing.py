# Joseph Muñoz Cascante y Jorge Cerdas Solórzano
# Python2.py: Testeo

# este comando importa la libreria para usar números aleatorios
from random import randrange
# ERR8 -5


# Función fac
# Recibe un número y retorna su valor factorial
# Entrada: una variable int. Salida: una variable int
def fac(y):
    c = 1
    for i in range(1, int(y) + 1):
        c = c*i
    return c


# Función verify_array_op
# Recibe un array de números y verifica que cada miembro sea un número
# Si uno de los miembros no es un número, retorna un código de error único
# Se le realiza a cada número del array de entrada la función multiple_op
# El array resultado de multiple_op lo introduce en un nuevo array
# Retorna el array de arrays, cuyos miembros son números
# Entrada: un array con todos los miembros int
# Salida: un array de arrays con todos los miembros int
# Validación: los parametros de entrada deben ser números (int)
def verify_array_op(array):
    array_n = []
    try:
        # este try verifica que el valor introducido sea un entero
        for num in array:
            int(num)
            array_n.append(multiple_op(num))
            # Esta recursion crea un array con las operaciones necesarias
            # a partir del array previamente generado
        return array_n  # Este comando retorna los arrays resultantes
    except ValueError:
        # en caso de que no se introduzca un entero el programa
        # devuelve un codigo de error unico
        return ValueError


# Función multiple_op
# Recibe un parámetro y verifica que sea un número
# Si no es un número, retorna un código de error único
# Al número x se le realizan 3 operaciones: x*x, 2^x y factorial de x
# Los resultados los ingresa en un array y retorna el array
# Entrada: un parametro int
# Salida: un array con todos los miembros int
# Validación: el parámetro de entrada debe ser un número (int)
def multiple_op(x):
    try:
        int(x)
        if x == 0:
            d = [0, 1, 0]
            # la condicion ve el caso en el que el array contenga un 0
            return d
        else:
            a = int(x)*int(x)
            b = 2**int(x)
            # estas variables realizan las operaciones
            # que se requieren de los valores introducido
            c = 1
            c = fac(x)
            d = [a, b, c]
            # retorna el array con los 3 resultados
            return d
    except ValueError:
        # en caso de que no se introduzca un entero el programa
        # devuelve un código de error único
        return ValueError


# Función testeo
# Se encarga de probar las funciones creadas con assert y pytets
# Realiza los siguientes casos:
# Un caso de éxito para multiple_op
# Un caso de éxito para verify_array_op
# Un caso negativo del método multiple_op
# Un caso negativo del método verify_array_op
def testeo():
    random = randrange(21)  # primero se obtiene un valor random
    # se prueba el caso de exito para multiple_op con entrada random
    assert multiple_op(random) == [random*random, 2**random, fac(random)]
    # se obtienen tres valores random
    u = randrange(21)
    v = randrange(21)
    w = randrange(21)
    # se hace un array de arrays con las operaciones de los números random
    test = [[u*u, 2**u, fac(u)], [v*v, 2**v, fac(v)], [w*w, 2**w, fac(w)]]
    # se prueba el caso de exito para verify_array_op con entradas random
    assert verify_array_op([u, v, w]) == test
    # se prueba el caso negativo para multiple_op
    assert multiple_op("xnw") == ValueError
    # se prueba el caso negativo para verify_array_op
    assert verify_array_op(["asda", 25, 1]) == ValueError


testeo()
