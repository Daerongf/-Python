# n1 = 2
# n2 = n1
# print(n1, n2)
# n1 = 4
# # print(" n1 = ", n1, "n2 = ", n2)
# # exit(0)
# l1 = [1, 2, 3]
# l2 = l1
# l2.append(4)
# print("l1= ", l1, "l2= ", l2)

# Переменная в питон это лишь указатель на объект в памяти. Если несколько переменных указывают на один и тот же
# изменяемый !!! объект, то изменив объект по одной из ссылок, мы изменим его и по остальным:
# особенно важно при передаче в функцию и при изменении объекта в цикле фор
# def modify(list):
#         # лучше делать копию списка внутри функции
#     lst = lst[:] # ==  lst = lst.copy()  lst.deepcopy() - если в списке есть еще список, то .копи скопирует только ссылку на него
#     lst.append("new")
#     return lst
#
# my_list = [1, 2, 3]
# mod_list = modify(my_list)
# print(mod_list)
# print(my_list)
# exit()

# Оператор is возвращает Тру, если операнды указывают на один и тот же объект в памяти
a = 10
b = 10

a = "qwerty"
b = "qwerty"

c = [1, 2]
d = c
e = [1,2]

print(a is b) #Неизменяемые типы данных питон кэширует для экономии памяти. Он ищет в памяти, есть ли у него уже такой объект
 # и тогда считает их одинаковым объектом
# exit(0)
print(c is d) #указывают на один и тот же объект
print(d is e) #разные объекты
print(d == e) #разные объекты
# Так лучше, чем if a == None
print(a is None)

a = ("qwerty")
b = ("qwe" + "rty")
print(a is b) # TRUE!