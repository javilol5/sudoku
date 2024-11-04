def check_columna(columna):
    longitud = len(columna)
    for i in range(longitud):
        for j in range(i + 1, longitud):  # Comparar con las listas posteriores
            if columna[i] == columna[j]:  # Si son iguales en todas las posiciones
                return False # Se encontró un duplicado en la misma posición
    return True

if __name__ == '__main__':
    assert check_columna([[1, 3, 2], 
                         [2, 1, 3], 
                         [2, 2, 1]]) is False
    