# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
print()
print('Задача1')

small = re.findall(r'[a-z|а-я]+', line)
print(small)

smalll = []
strr = ""
for el in line:
       if el.islower():
              strr += el
       elif strr:
              smalll.append(strr)
              strr = ""
if strr != "":
       smalll.append(strr)
print(smalll)



# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
print()
print('Задача2')
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

str2 = re.findall(r'[a-z|а-я]{2}([A-Z|А-Я]+)[A-Z|А-Я]{2}', line_2)
print(str2)
# print()
print("Если ровно два символа слева регулярным выражением:")

if line_2[0].isupper():
       str2 = re.findall(r'[A-Z|А-Я]+[a-z|а-я]{2}([A-Z|А-Я]+)[A-Z|А-Я]{2}', line_2)
else:
       str2 = re.findall(r'^[a-z|а-я]{2}([A-Z|А-Я]+)[A-Z|А-Я]{2}', line_2) + \
                     re.findall(r'[A-Z|А-Я]+[a-z|а-я]{2}([A-Z|А-Я]+)[A-Z|А-Я]{2}', line_2)
print(str2)
print()
print("Не понятно, почему не попадает символ Q из выражения ...HlmQKJn...\n "
       "Вообще должен, и в решении без регулярки он есть. Причем если применить это регулярное выражение только к части\n"
       "строки, например, HlmQKJndiA, символ Q в ответ выводится. Загадка!")
print()
task2 = []
task22 = []
str22 = ""
cnt = []
i = 0
# print(len(line_2))
print("Читаем задание как \"РОВНО две строчных буквы перед и РОВНО две заглавных после\" (регулярка работает не так):" )
for i in range(len(line_2)-2):
    if i == 0 and line_2[i].islower() and line_2[i+1].islower() and line_2[i+2].isupper():
        cnt.append(i + 2)
    elif line_2[i].isupper() and line_2[i+1].islower() and line_2[i+2].islower() and line_2[i+3].isupper():
        cnt.append(i + 3)
    # elif i == 0
# print(cnt)

j = 0
for j in cnt:
       try:
              while line_2[j].isupper():
                     str22 += line_2[j]
                     # print(str22)
                     j += 1
                     if j == cnt[-1]:
                            break
       except IndexError:
              pass
       if str22:
              task2.append(str22)
              str22 = ""


if str22 != "":
       task2.append(str22)
# print(task2)
k = 0
for k in range(len(task2)):
       if len(task2[k]) > 2:
              task2[k] = task2[k][:-2]
              task22.append(task2[k])



print(task22)



# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
print()
print('Задача3')
import os
import random

path = os.path.join('randomdigit.txt')
digitstr = ""
with open(path, 'w', encoding='UTF-8') as rnd:
       i = 0
       while i <= 2500:
            rnddigit = random.randint(0,9)
            digitstr += str(rnddigit)
            # rnd.write()
            i += 1
       rnd.write(digitstr)

with open(path, 'r', encoding='UTF-8') as rnd2:
       stroka = rnd2.read()
       print(stroka)
j = 0
item = 0
eqlist = []
equal = ""

# print(stroka)

if stroka[0] == stroka [1]:
       equal += str(stroka[0])
       if stroka[1] != stroka[2]:
              equal += str(stroka[1])
              eqlist.append(equal)
              equal = ""

for j in range(1, len(stroka)-1):
     if stroka[j] == stroka[j+1]:
            equal += str(stroka[j])
     elif stroka[j] == stroka[j-1] and j != 1:
            equal += str(stroka[j])
            eqlist.append(equal)
            equal = ""

if stroka[-1] == stroka[-2]:
       equal += str(stroka[-1])
       eqlist.append(equal)
       equal = ""

if equal:
       eqlist.append(equal)
print("Повторяющиеся последовательности: ", eqlist)

lenlist = list(map(len, eqlist))
print("Длины повторяющихся последовательностей: ", lenlist)
maxlen = max(lenlist)
print("Максимальное количество повторяющихся подряд символов: ", maxlen)

k = 0
l = 0
maxlenlist = []
for l in eqlist:
       if len(l) == maxlen:
              maxlenlist.append(l)
print('Самые длинные последовательности: ', maxlenlist)
q = 0
qq = ""
for q in maxlenlist:
      qq += q + " "

with open(path, 'a', encoding='UTF-8') as rnd3:
       rnd3.write("\n")
       rnd3.write("\n")
       rnd3.write(qq)





