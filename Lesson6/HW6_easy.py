import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print("Задача1")
class Triangle:
    def __init__(self, a1, a2, b1, b2, c1, c2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2
        self.ab = 0
        self.ac = 0
        self.bc = 0
        self.perimetr = 0
        self.side = None
        self.alfa = 0
        self.h = 0
        self.sqwr = 0
        self.m_square = 0

    def sidelen(self):
        self.ab = math.sqrt((self.b1 - self.a1)**2 + (self.b2-self.a2)**2)
        self.ac = math.sqrt((self.c1 - self.a1)**2 + (self.c2-self.a2)**2)
        self.bc = math.sqrt((self.c1 - self.b1)**2 + (self.c2-self.b2)**2)

    def perim(self):
        self.sidelen()
        self.perimetr = self.ab + self.ac + self.bc

    def height(self, side):
        self.side = side.upper()
        print("Считаем высоту к стороне {}:".format(self.side))
        if self.side == "AC" or self.side == "ac": # можно уже не проверять на равенство нижнему регистру, т.к. все upper
            self.alfa = math.acos((self.bc**2+self.ac**2-self.ab**2)/(2*self.bc*self.ac))
            self.h = math.sin(self.alfa)*self.bc

        elif self.side == "AB" or self.side == "ab":
            self.alfa = math.acos((self.ab ** 2 + self.ac ** 2 - self.bc ** 2) / (2 * self.ab * self.ac))
            self.h = math.sin(self.alfa) * self.ac

        elif self.side == "BC" or self.side == "bc":
            self.alfa = math.acos((self.bc ** 2 + self.ac ** 2 - self.ab ** 2) / (2 * self.bc * self.ac))
            self.h = math.sin(self.alfa) * self.ac

        else:
            print('Неверно указано название стороны. Укажите AB, BC или AC в латинской раскладке')


    def msquare(self):
        self.height('ab')
        self.sqwr = round(0.5 * self.h * self.ab, 4)


tr1 = Triangle(0, 0, 0, 3, 4, 0)

tr1.perim()
print('Периметр: ', tr1.perimetr)
print()
tr1.height('ab')
print("Высота:", round(tr1.h, 4))
tr1.height('ac')
print("Высота:", round(tr1.h, 4))
tr1.height('bc')
print("Высота:", round(tr1.h, 4))
print()
tr1.msquare()
print("Площадь равна: ", tr1.sqwr)



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print()
print("Задача2")  #============= Упростим задачу: будем считать BC и AD основаниями.==============

class Trapeze_ravno(Triangle):
    def __init__(self, a1, a2, b1, b2, c1, c2, d1, d2):
        Triangle.__init__(self, a1, a2, b1, b2, c1, c2)
        self.d1 = d1
        self.d2 = d2
        self.cd = 0
        self.ad = 0
        self.ravnob = False

    def sidelen(self):
        super().sidelen()
        self.cd = math.sqrt((self.d1 - self.c1) ** 2 + (self.d2 - self.c2) ** 2)
        self.ad = math.sqrt((self.d1 - self.a1) ** 2 + (self.d2 - self.a2) ** 2)

    def perim(self):
        super().perim()
        self.perimetr = self.ab + self.ad + self.bc + self.cd

    def msquare(self):
        self.checkk()
        if self.ravnob == True:
            self.h = math.sqrt(self.ab**2 - ((self.ad - self.bc)/2)**2)
            self.sqwr = 0.5 * self.h * (self.bc + self.ad)
        else:
            pass

    def checkk(self):
        # if (self.c1-self.b1)/(self.c2-self.b2) == (self.d1-self.a1)/(self.d2-self.a2) and\
        if (self.d1-self.a1) * (self.c2-self.b2) == (self.c1-self.b1) * (self.d2-self.a2) and \
        (self.b1-self.a1)**2 + (self.b2-self.a2)**2 == (self.d1-self.c1)**2 + (self.d2-self.c2)**2:
            self.ravnob = True
            print("Это равнобочная трапеция")
        else:
            self.ravnob = False
            print("Фигура не является равнобочной трапецией")



trap = Trapeze_ravno(0, 0, 3, 4, 7, 4, 10, 0)
trap1 = Trapeze_ravno(0, 0, 3, 4, 7, 4, 10, 2)
trap2 = Trapeze_ravno(0, 0, 3, 4, 7, 4, 12, 0)

trap.sidelen()
trap.perim()
# trap.checkk()
trap.msquare()
print("Стороны трапеции: AB={}, BC={}, CD={}, AD={}".format(trap.ab, trap.bc, trap.cd, trap.ad))
print("Периметр трапеции: {}".format(trap.perimetr))
print("Площадь трапеции: {}".format(trap.sqwr))
trap1.checkk()
trap2.checkk()

