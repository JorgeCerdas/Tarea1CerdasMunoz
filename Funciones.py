# Joseph Muñoz Cascante y Jorge Cerdas Solórzano
# Python1.py: Funciones

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
# Validación: los parámetros de entrada deben ser números (int)
def verify_array_op(array):
    array_n = []
    try:
        # Este try verifica que el valor introducido sea un entero
        # Si lo es realiza las operaciones
        for num in array:
            int(num)
            array_n.append(multiple_op(num))
            # Esta recursión crea un array con las operaciones necesarias
            # A partir del array previamente generado
        return array_n
    # Este comando retorna los arrays resultantes
    except ValueError:
        # en caso de que no se introduzca un entero
        # el programa devuelve un código de error único
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
            # esta condicion se encarga del caso
            # en el que el array contenga un 0
            return d
        else:
            a = int(x)*int(x)
            b = 2**int(x)
            # estas variables realizan las operaciones que
            # se requieren de los valores introducido
            c = 1
            c = fac(x)
            d = [a, b, c]
            # retorna el array con los 3 resultados
            return d
    except ValueError:
        # en caso de que no se introduzca un entero
        # el programa devuelve un código de error único
        return ValueError
