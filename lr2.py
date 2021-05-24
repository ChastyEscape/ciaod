import numpy as np
import random


"""
    Тимонин Григорий БФИ1901
    
    1) Реализовать:
        1. Бинарный поиск
        2. Бинарное дерево
        3. Фибоначчиев
        4. Интерполяционный
    2) Реализовать:
        1. Простое рехеширование
        2. Рехэширование с помощью псевдослучайных чисел
        3. Метод цепочек
    3) Решить задачу:
        Расставить на стандартной 64-клеточной шахматной доске 8 ферзей так, 
        чтобы ни один из них не находился под боем другого». 
        Подразумевается, что ферзь бьёт все клетки, 
        расположенные по вертикалям, горизонталям и обеим диагоналям
        Написать программу,  которая находит хотя бы один способ решения задач.

"""


def generate_m():
    min = 0
    max = 100
    k = 15
    mass = np.random.randint(min, max, k)
    mass.sort()
    return mass, mass[random.randint(0, k-1)]


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' v ')
            self._printTree(node.r)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)


def generate_tree(m,a):
    tree = Tree()
    for i in m:
        tree.add(i)
    return tree, a


def binary_find(mass, a):
    l = 0
    r = len(mass)
    index = int((l+r)/2)
    while mass[index] != a:
        if mass[index] < a:
            l = index
        else:
            r = index
        index = int((l+r)/2)
    return index


def fibonaci_num(n):
    if n == 1:
        return 1
    else:
        last=1
        current = 1
        while current+last < n:
            i = current
            current = current + last
            last = i
        return current+last


def fib2(n):
    arr = []
    arr.append(0)
    arr.append(1)
    arr.append(1)
    index = 3
    if n == 0 or n == 1:
        return 0
    else:
        k = fibonaci_num(2)
        while k != n:
            index += 1
            arr.append(k)
            k = fibonaci_num(k+1)
        return arr[index-2]


def fibonaci(m, a):
    f0 = fibonaci_num(len(m))
    ls=0
    while True:
        if m[fib2(f0)] == a:
            return ls+fib2(f0)
        elif m[fib2(f0)] > a:
            f0 = fib2(f0)
            m = m[:f0]
            f0 = fib2(f0)
        else:
            ls+=fib2(f0)
            m = m[fib2(f0):]
            f0 = fibonaci_num(len(m))


def interpolation_find(mas, val):
    low = 0
    high = (len(mas) - 1)
    while low <= high and val >= mas[low] and val <= mas[high]:
        index = low + int(((float(high - low) / ( mas[high] - mas[low])) * ( val - mas[low])))
        if mas[index] == val:
            return index
        if mas[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1


def simple(table, x, l):
    flag = False
    result = x
    while flag == False:
        place = x % l
        if table[1][place] == 0:
            table[1][place] = result
            flag = True
        else:
            x += 1
    return table


def randh(table, x, l):
    flag = False
    result = x
    while flag == False:
        place = x % l
        if table[1][place] == 0:
            table[1][place] = result
            flag = True
        else:
            x += random.randint(1, l - 1)
    return table


def reh(message, parm):
    table = np.array([range(len(message)) ,np.zeros(len(message))], int)
    l = len(message)
    while len(message) > 0:
        x = message[0]
        message = message[1:]
        if parm == 0:
            table = simple(table,x, l)
        else:
            table = randh(table,x, l)
    return table


def chain(message):
    ch = []
    l = len(message)
    for i in range(l):
        ch.append(0)
    while len(message) > 0:
        x = message[0]
        message = message[1:]
        place = x % l
        if ch[place] == 0:
            ch[place] = [x]
        else:
            ch[place].append(x)
    return ch
        

def chek(desk):
    clean = False
    cells = []
    line = 0
    column = 0
    for i in desk:
        column = 0
        for j in i:
            if j == 0:
                clean = True
                cells.append([line,column])
            column += 1
        line += 1
    return clean, cells


def set_diagonals(f):
    x = f[0]
    y = f[1]
    diagonal = []
    while (x >= 0 and x<=7) and (y >=0 and y <= 7):
        diagonal.append([x, y])
        x -= 1
        y -= 1
    x = f[0]
    y = f[1]
    while (x >= 0 and x<=7) and (y >=0 and y <= 7):
        diagonal.append([x, y])
        x += 1
        y += 1
    x = f[0]
    y = f[1]
    while (x >= 0 and x<=7) and (y >=0 and y <= 7):
        diagonal.append([x, y])
        x -= 1
        y += 1
    x = f[0]
    y = f[1]
    while (x >= 0 and x<=7) and (y >=0 and y <= 7):
        diagonal.append([x, y])
        x += 1
        y -= 1
    return diagonal

def queens_8():
    """
    codes:
        0 - пусто
        1 - стоит ферзь
        2 - сюда нельзя ставить
    """
    complete = False
    while complete == False:
        desk = np.zeros([8,8])
        for i in range(8):
            flag, variants = chek(desk)
            if flag == True and i == 7:
                desk[variants[0][0],variants[0][1]] = 1
                return desk
            else:
                if flag == True:
                    f = random.choice(variants)
                    x = f[0]
                    y = f[1]
                    diagonal = set_diagonals(f)
                    line = 0
                    for i in desk:
                        cell = 0
                        for j in i:
                            temp = [line,cell]
                            if line == x or cell == y or temp in diagonal:
                                desk[line,cell] = 2
                            cell += 1
                        line +=1
                    desk[x,y] = 1

if __name__ == "__main__":
    m, a = generate_m()
    print(m, a)
    print(binary_find(m, a),' - бинарный')
    t, a = generate_tree(m, a)
    print(a)
    print(t.find(a).v,' - ищем в дереве значение и выводим его (а как еще проверить?)')
    print(fibonaci(m,a),' - фибоначчи')
    print(interpolation_find(m,a),' - интерполяционный')


    print(reh([1,11,7,14,10], 0),' - простое рехеширование')
    print(reh([1,11,7,14,10], 1),' - рандомное рехеширование')
    print(chain([1,11,7,14,10]),' - метод цепочек')


    print(queens_8(),' - расстановка ферзей')