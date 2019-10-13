import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print("Задача 1:")
i = 0
dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
# print(dir_path)

for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
    # print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Директории уже созданы')
print(os.listdir(os.getcwd()))

antwoort = input('А теперь удалим? Y = Yes: ')
i = 0
if antwoort == 'Y':
    for i in range(1,10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        # os.rmdir(dir_path)
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print('Директории уже были удалены или не созданы')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print()
print('Задача 2:')
print(os.listdir(os.getcwd()))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print()
print('Задача 3:')
path3 = os.path.join(os.getcwd(), 'HW5_Easy_Copy.py')
my_path = os.path.join(os.getcwd(), 'HW5_Easy.py')
with open(my_path, 'r', encoding='UTF-8') as me:
        contents = me.read()
with open(path3, 'w', encoding='UTF-8') as my_copy:
        my_copy.write(contents)

