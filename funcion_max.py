#Función "custom_max" compara dos parámetros y retorna el mayor

def custom_max(num_1: float, num_2: float):
    """
    Dados dos números devuelve el mayor.

    Params:
        num_1: float
        num_2: float

    Si alguno de los parametros no es numérico da el aviso de que es un error.
    """
    try:
        if num_1 == num_2:
            max_num = "No hay un numero maximo"
        elif num_1 > num_2:
            max_num = "Numero maximo es " + str(num_1)
        else: 
            max_num = "Numero maximo es " + str(num_2)
    except:
        max_num = TypeError("Algo salió mal")
    return max_num
maxcustom = custom_max(1667,277)
print(maxcustom)