from itertools import *


"""
    Тимонин БФИ1901
    «Шарики и стрелы»:
        Некоторые сферические шарики распределены по двухмерному пространству. Для каждого
    шарика даны x­координаты начала и конца его горизонтального диаметра. Так как пространство
    двумерно, то y­координаты не имеют значения в данной задаче. Координата xstart всегда меньше
    xend.
        Стрелу можно выстрелить строго вертикально (вдоль y­оси) из разных точек x­оси. Шарик
    с координатами xstart и xend уничтожается стрелой, если она была выпущена из такой позиции
    x, что xstart ⩽ x ⩽ xend. Когда стрела выпущена, она летит в пространстве бесконечное время
    (уничтожая все шарики на пути).
    Дан массив points, где points[i] = [xstart, xend]. 
    Напишите функцию, возвращающую минимальное количество стрел, которые нужно выпустить, чтобы уничтожить все шарики.
"""


def arrows(bubbles):
    counter = 0
    while len(bubbles) > 0:
        max_count = 0
        max_pop = []
        for i in permutations(bubbles):
            a = i[0][0]
            b = i[0][1]
            local_counter = 0
            to_pop = []
            pop_counter = 0
            for j in i:
                if (j[0] >= a and j[0] <= b) or (j[1] >= a and j[1] <= b):
                    a = max(a,j[0])
                    b = min(b, j[1])
                    local_counter += 1
                    to_pop.append(j)
                pop_counter += 1
            if local_counter > max_count:
                max_count = local_counter
                max_pop = to_pop
            elif local_counter == max_count:
                b = []
                for q in bubbles:
                    b.append(q)
                for i in max_pop:
                    b.remove(i)
                a1 = arrows(b)
                c1 = max_count + a1
                b = []
                for q in bubbles:
                    b.append(q)
                for i in to_pop:
                    b.remove(i)
                a2 = arrows(b)
                c2 = local_counter + a2
                if c1 < c2:
                    pass
                elif c1 == c2:
                    max_count = local_counter
                    max_pop = to_pop
                else:
                    max_count = local_counter
                    max_pop = to_pop
        print(max_pop, bubbles)
        for i in max_pop:
            bubbles.remove(i)
        counter += 1
    return counter

if __name__ == "__main__":
    print(arrows([[10,16],[2,8],[1,6],[7,12]]))
    print(arrows([[2,3],[2,3]]))
