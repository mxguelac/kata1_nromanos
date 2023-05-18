simbolos = {
    1: 'I',
    5: 'V',
    10: 'X'
}

def entero_a_romano(n_int):
    if n_int in simbolos:
        return simbolos[n_int]
    
    if n_int < 4:
        return n_int * simbolos[1]
    elif n_int == 4:
        return simbolos[1] + simbolos[5]
    else:
        return simbolos[5] + (n_int - 5) * simbolos[1]
  
    


