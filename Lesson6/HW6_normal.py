# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import copy
print("Задача1")

class School:
    def __init__(self, class_list, teacher_dict, science_list):
        self.class_name = class_list
        self.teacher = teacher_dict
        self.science = science_list

# class_list_1 = ['1А', '1Б', '2А', '2Б', '3А', '3Б', '3В']
# teacher_dict_1 = {
#     'Иванов А. П.':'Математика',
#     'Карпов М. И.':'Литература',
#     'Харитонов Е. В.':'Физкультура',
#     'Щукина О. А.':'Природоведение',
#     'Карпенко В. Ю.':'Основы религии',
#     'Зубалевич К. М.':'ОБЖ'
# }
class_list = []
pupil_list = []


class Pupil:
    def __init__(self, pupil_name, papa, mama, his_class):
        self.pupil_name: str = pupil_name
        # self.pupil_surname: str = pupil_surname
        # self.pupil_fathersname: str = pupil_fathersname
        self.papa: str = papa
        self.mama: str = mama
        self.his_class: str = his_class
        # self.class_list = ""

    def registration(self):
        class_list.append(self.his_class)
        # print(self.his_class)
        # school1 = School()
        pupils_in_classes = {class_list[j]: [] for j in range(len(class_list))}

        for k in pupils_in_classes:
            if self.his_class == k:
                pupils_in_classes[k].append(self.pupil_name)


        print(pupils_in_classes)


class Teacher:
    def __init__(self, teacher_name, science):
        self.teacher_name = teacher_name
        self.science = science


teacher1 = Teacher('Иванов А. П.', 'Математика')
teacher2 = Teacher('Карпов М. И.', 'Литература')
teacher3 = Teacher('Харитонов Е. В.', 'Физкультура')
teacher4 = Teacher('Щукина О. А.', 'Природоведение')
teacher5 = Teacher('Карпенко В. Ю.', 'Основы религии')
teacher6 = Teacher('Зубалевич К. М.', 'ОБЖ')

pupil1 = Pupil('Черненко Сергей Вадимович', 'Черненко Вадим Алексеевич', 'Черненко Елена Анатольевна', '1Б')
pupil1.registration()
pupil2 = Pupil('Усольцев Анатолий Сергеевич', 'Усольцев Сергей Геннадьевич', 'Усольцева Анна Алексеевна', '2А')
pupil2.registration()
pupil3 = Pupil('Лукина Алиса Дмитриевна', 'Лукин Дмитрий Иванович', 'Лукина Полина Андреевна', '2А')
pupil3.registration()
pupil4 = Pupil('Самойлов Илья Вячеславович', 'Самойлов Вячеслав Михайлович', 'Самойлова Ирина Валерьевна', '2А')
pupil4.registration()
pupil5 = Pupil('Котова Екатерина Олеговна', 'Котов Олег Владимирович', 'Котова Светлана игоревна', '1Б')
pupil5.registration()
pupil6 = Pupil('Шнайдер Галина Генриховна', 'Шнайдер Генрих Вольфович', 'Шнайдер Татьяна Петровна', '1А')
pupil6.registration()
pupil7 = Pupil('Ильиных Дарья Тимофеевна', 'Ильиных Тимофей Константинович', 'Ильиных Олеся Алексеевна', '1А')
pupil7.registration()
pupil8 = Pupil('Дмитриев Валентин Константинович', 'Дмитриев Константин Дмитриевич', 'Дмитриева Валентина Ивановна', '1А')
pupil8.registration()

n = []
for i in class_list:
    if i not in n:
        n.append(i)
class_list = n

print('1. Список классов: {}'.format(class_list))

# pupils_in_classes = []
# for i in range(len(class_list)):

pupils_in_classes1 = {class_list[j]:[] for j in range(len(class_list))}
pupils_in_classes1

# for k in pupils_in_classes:
#     if "1Б" == pupils_in_classes[k]:
#         print('Bingo!')
#
# print(pupils_in_classes)
