"""     Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов, отличной от 0.
    Пример:
    [1.1, 1.2, 3.1, 5, 10.01] => 0.19
 """

def max_min_diff(var:str):
    a=[float(s) for s in s.split()]
    max,min=a[0]%1,a[0]%1
    for i in range(len(a)):
        if a[i]%1>max:
            max=a[i]%1
        elif a[i]%1<min and a[i]%1!=0:
            min=a[i]%1
            print(min)
    return max-min

s=input('Введи несколько чисел, разделяя пробелом: ')
print(round(max_min_diff(s),2))