#На складе лежат разные фрукты в разном количестве. Нужно написать функцию, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе

total_fruits = {'banana': 5, 'mango': 7, 'apple': 8}
total = 0
 
for item in total_fruits.values():
    total += item
print(total)