# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
lst_g = [random.randint(-10, 10) for _ in range(10)]
lst_g_sqr = [el**2 for el in lst_g ]
print('Список = ', lst_g)
print('Список в квадрате = ', lst_g_sqr)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
f_lst_1  = ['Orange', 'Apple', 'Watermelon', 'Lime', 'Pineapple', 'Strawberry', 'Cherry']
f_lst_2  = ['Strawberry', 'Cherry', 'Pineapple', 'Mango', 'Lemon', 'Watermelon']
f_lst_3  = [el for el in f_lst_1 if el in f_lst_2]
print('Список = ', f_lst_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
lst_g = [random.randint(-10, 10) for _ in range(10)]
lst_g_new = [el for el in lst_g if el%3 == 0 and el>0 and el%4 != 0]
print('Список = ', lst_g)
print('Список c условиями = ', lst_g_new)