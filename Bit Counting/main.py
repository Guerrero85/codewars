def count_bits(n):
#Devuelve el número de unos en representación binaria de un número
    return bin(n).split('b')[1].count('1')