# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m): 
    f1 = f2 = 1
    num_new = [f1, f2] 
    mm=m
    while m > 0:
        f1, f2 = f2, f1 + f2
        num_new.append(f2)
        m = m - 1
    return num_new[n-1:mm]
print(fibonacci(2, 15))  

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    ln = len(origin_list)
    for num in range(ln-1,0,-1):
        for i in range(num):
            if origin_list[i]>origin_list[i+1]:
                tmp = origin_list[i]
                origin_list[i] = origin_list[i+1]
                origin_list[i+1] = tmp
                
    return origin_list 
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(filter_param, list_param):
    filter_list = []
    for i in list_param : 
        if i != filter_param: 
            filter_list.append(i)
    return (filter_list)
 
print(my_filter(0, [-1, 0, 1, 0, 0, 1, 0, -1, 2, 5, ' ', '' , 9]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# Будут, если противоположные стороны попарно равны.
coor = {'a1_x1': {'question': 'x1', 'answer': None},
        'a1_y1': {'question': 'y1', 'answer': None},
        'a2_x2': {'question': 'x2', 'answer': None},
        'a2_y2': {'question': 'y2', 'answer': None},
        'a3_x3': {'question': 'x3', 'answer': None},
        'a3_y3': {'question': 'y3', 'answer': None}, 
        'a4_x4': {'question': 'x4', 'answer': None},
        'a4_y4': {'question': 'y4', 'answer': None}        
          }
for i in coor:
    temp = input(coor[i]['question'] + '= ')
    temp = int(temp)
    coor[i]['answer'] = temp

if (coor['a1_y1']['answer'] == coor['a4_y4']['answer'] 
    and (coor['a2_y2']['answer']==coor['a3_y3']['answer']))
    and abs(coor['a1_x1']['answer'] - coor['a2_x2']['answer']) == abs(coor['a3_x3']['answer'] - coor['a4_x4']['answer']):
   print('Точки являются вершинами параллелограмма')
else:
   print('Точки не являются вершинами параллелограмма');