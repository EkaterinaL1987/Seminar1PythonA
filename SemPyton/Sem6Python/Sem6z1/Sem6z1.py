#N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i включительно. Определите, какие палки остались стоять на месте.

sticks = int(input('Количество палок: '))
throws = int(input('Количество бросков: '))
 
row = ['I'] * sticks
 
for i in range(throws):
    query = 'Бросок ' + str(i + 1) + '. Сбиты палки с номера '
    while True:
        start = int(input(query)) - 1
        if (start >= 0) and (start <= sticks):
            break
    while True:
        end = int(input('по номер ')) - 1
        if (end >= start) and (end <= sticks):
            break
    for j in range(start, end + 1):
        row[j] = '.'
 
print('Результат: ', *row, sep='')
