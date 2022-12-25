"""     Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    Пример:
    для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
 """


def fibonacci(var):
    if var >= 0:
        idx = range(var+1)
        fib_list = [0, 1]
        for i in idx[2:]:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[var]
    else:
        var = -(var-1)
        idx = range(var+1)
        fib_list = [1, 0]
        for i in idx[2:]:
            fib_list.append(fib_list[i-2] - fib_list[i-1])
        fib_list.reverse()
    return fib_list[0]

def print_fibonacci(var:int):
    my_list=[]
    for i in range(-var, var+1):
        my_list.append(fibonacci(i))
    print(my_list)

n = int(input('Введи число для вычисления ряда Фибоначчи: '))
print_fibonacci(n)
