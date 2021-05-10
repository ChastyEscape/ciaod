import numpy as np


def multip(m):
    m = m.transpose()
    flag = 0
    nums_list = []
    k = 0
    for i in m:
        flag = check(i)
        if flag == 0:
            nums_list.append(k)
        else:
            flag = 0
        k += 1
    if len(nums_list) != 0:
        return nums_list
    else:
        return "Таких столбцов нет"


def check(n):
    for j in n:
        if j % 7 != 0 and j % 5 != 0:
            return 1
    return 0


def tests():
    m = np.array([[5, 7],
                 [14, 4],
                 [25, 15]])
    print(multip(m))

    m = np.array([[5, 7],
                 [11, 4],
                 [25, 15]])
    print(multip(m))

    m = np.array([[5, 7, 21],
                 [14, 14, 25],
                 [25, 15, 34]])
    print(multip(m))


tests()
