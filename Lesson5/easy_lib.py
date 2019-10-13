import os

def mknwdir():
    dir_input = input('Введите название папки: ')
    dir_path = os.path.join(os.getcwd(), '{}'.format(dir_input))
    # print(dir_path)
    try:
        os.mkdir(dir_path)
        print('Папка {} успешно создана'.format(dir_input))
    except FileExistsError:
        print('Папка с таким именем уже есть!')
    # print(os.listdir(os.getcwd()))

def deldir():
    dir_input2 = input('Введите название папки для удаления: ')
    dir_path = os.path.join(os.getcwd(), '{}'.format(dir_input2))
        # os.rmdir(dir_path)
    try:
        os.rmdir(dir_path)
        print('Папка {} удалена успешно'.format(dir_input2))
    except FileNotFoundError:
        print('Директории с таким названием в текущей папке нет')