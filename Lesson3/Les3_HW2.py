max_lengh_fruit = len(max(fruits, key =len))

for idx, fruit in enumerate(fruits, start=1):
    print("{}.{}".format(idx,fruit.rjust(max_lengh_fruit))) # Вот так надо! ПОгуглить

# Про удаление из списка:
l = [1, 2, 3, 4, 5]
for el in l.copy():
    print(el)
    l.remove(el)
print(l)