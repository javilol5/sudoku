def check_num(valido):

    for lista in valido:
        for num in lista:
            if num == int and num > 0:
                return True
            else:
                return False

if __name__ == "__main__": 
    assert check_num([[1, 2, 3, 4, 5]]) is True
#                      ,
#              [2, 3, 1, 5, 6],
#              [4, 5, 2, 1, 3],
#              [3, 4, 5, 2, 1],
#              [5, 6, 4, 3, 2]]) is True

    assert check_num([['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]) is False