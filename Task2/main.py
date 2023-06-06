'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
from random import sample

#Генерируем список случайных чисел от 0 до 100 состоящий из 25 элементов
random_list = sample(range(100), 25)
print(random_list)

def read_float(text):
    while(True):
        try:
            read_float_number = float(input(text))
        except:
            print('Введено не число!')
            continue
        return read_float_number
#Запрашиваем ввод значений и проверяем корректность ввода
while(True):
    min_number = read_float('Введите минимальное значение: ')
    max_number = read_float('Введите максимальное значение: ')
    if(min_number >= max_number):
        print('Минимальное значение должно быть меньше максимального')
        continue
    break
#Ищем необходимые элементы и выводим их индексы
for i in range(len(random_list)):
    if max_number >= random_list[i] >= min_number:
        print(i)
