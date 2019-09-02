﻿# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Директория уже существует")

print('Директории созданы')
try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Директории удалены")
	
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
list = os.listdir()
for i in list:
    print(i)	
	
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
import os
def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(current_file_copy())