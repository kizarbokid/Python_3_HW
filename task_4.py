"""     Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    Пример:
    45 -> 101101
    3 -> 11
    2 -> 10 """

def dec_to_bin(var:str):
    dec=int(s)
    bin:str=''
    while dec>0:
        bin+=str(dec%2)
        dec= dec//2
    return bin[::-1]

s=input('Введи целое число: ')
print(dec_to_bin(s))