def check_fila(fila):
    
    for list in fila:
        if len(list) != len(set(list)):
            return False
    return True


if __name__ == "__main__":
    assert check_fila([[2, 1, 3],
                        [2, 3, 1],
                        [3, 1, 2]]) is True
    assert check_fila([[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 2]]) is False