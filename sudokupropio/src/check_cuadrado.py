def check_cuadrado(cuadrado): 
    assert isinstance(cuadrado, list)
    
    longitud = len(cuadrado)

    for fila in cuadrado:     
        #longitud == len(fila)
        if longitud == len(fila):
            return True
        elif longitud != len(fila):
            return False
if __name__ == "__main__":
    assert check_cuadrado([[1, 2,],
                           [2, 3, 1],
                           [3, 1, 2]]) is False
    assert check_cuadrado([[1, 2, 3, 4],
                           [2, 3, 1, 3],
                           [3, 1, 2, 3],
                            [4, 4, 4, 2]]) is True