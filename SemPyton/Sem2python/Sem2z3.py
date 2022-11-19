#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

print('Введите число')
n = int(input())
print('[', end = '')
 
for i in range (1, n + 1):
    res = round((1 + 1 / n)**n, 3)
    sum = int(sum([res for res in range(i + 1)]))
    if i < (n + 1) -1: 
        print(f'{sum}', end = ', ')
    else: print(f'{sum}', end = '')
print(']', end = '')
1