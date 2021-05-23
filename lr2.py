import numpy as np
import numpy.random as rand
import time

maschess = [0, 1, 2, 3, 4, 5, 6, 7]

def proverka(mas):
    k = 1
    for i in range(len(mas) - 1):
        for j in range(i + 1,len(mas)):
            if mas[i] + k == mas[j] or mas[i] - k == mas[j]:
                return False
            k += 1
        k = 1
    return True
    pass

def BinarySearch(mas, val):
    first = 0
    last = len(mas) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last) // 2
        if mas[mid] == val:
            index = mid
        else:
            if val < mas[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def FibonacciSearch(mas, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(mas)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(mas)-1))
        if (mas[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (mas[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(mas)-1) and mas[index+1] == val):
        return index+1;
    return -1

def InterpolationSearch(mas, val):
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

def random():
    list = []
    listhelp = [0,1,2,3,4,5,6,7]
    for i in range(0,8):
        mindex = rand.randint(0,len(listhelp))
        list.append(listhelp[mindex])
        listhelp.remove(listhelp[mindex])
    return list

def proverka(mas):
    k = 1
    for i in range(0,6):
        for j in range(i + 1,7):
            if (mas[i] + k == mas[j]) or (mas[i] - k == mas[j]):
                return False
            k = k + 1
        k = 1
    return True

maschess = [0] * 8
while (proverka(maschess) == False or maschess[0] == 0 and maschess[1] == 0):
    maschess = random()
    print(maschess)
    
mas = [6, 12, 17, 22, 32, 33, 35, 37, 41, 48]
x = ""


print("Бинарный " + str(BinarySearch(mas,37)))
print("Фибоначчи " + str(FibonacciSearch(mas,37)))
print("Интерполяционный " + str(InterpolationSearch(mas,37)))