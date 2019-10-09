 Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print('Задача 1')
def my_round(number, ndigits):

    nmb = int(number * (10**(ndigits+1)))

    if nmb % 10 > 4:
        nmb = nmb // 10 + 1
    else :
        nmb = nmb // 10
    nmb /= 10 ** ndigits
    return nmb

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print()
print('Задача 2')
def lucky_ticket(ticket_number):
    str_ticket = str(ticket_number)
    if len(str_ticket) == 6:
        sp = [int(str_ticket[0]), int(str_ticket[1]), int(str_ticket[2]), int(str_ticket[3]), int(str_ticket[4]), int(str_ticket[5])]
        if sp[0] + sp [1] + sp[2] == sp [3] + sp[4] + sp[5]:
            luck = "Билет счастливый"
        else:
            luck = "Билет не счастливый"

    else:
        luck = "Билет не счастливый"
    return (luck)

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
