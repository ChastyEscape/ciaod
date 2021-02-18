import numpy as np
import numpy.random as rand
import time

def switchsort(a,n,m):
    for l in range(n):
        for i in range(m-1):
            k=i
            j=i+1
            while j<m:
                if a[l][j]<a[l][k]:
                    k=j
                j+=1
            a[l][i], a[l][k] = a[l][k], a[l][i]
    return a,m,n

def pastesort(a,n,m):
    for l in range(n):
        for i in range(1,m):
            t = a[l][i]
            #print(a[l][i])
            j=i-1
            while(j >= 0 and t < a[l][j]):
                a[l][j + 1] = a[l][j]
                j=j-1
            a[l][j+1]=t
            #print(a[l][j])
    return a,m,n

def shellsort(a,n,m):
    for l in range(n):
        inc = m//2
        while inc>0:
            for i in range (inc,n):
                t=a[l][i]
                j=i
                while j>=inc and a[l][j-inc]>t:
                    a[l][j] = a[l][j-inc]
                    j=j-inc
                a[l][j]=t
            inc = inc//2
    return a

def switchsort(a,n,m):
    for l in range(n):
        k=m
        for k in range (m-1):
            for i in range(1,m):
                if(a[l][i-1]>a[l][i]):
                    a[l][i], a[l][i-1] = a[l][i-1], a[l][i]
            k-=1
    return a

def quicksort(a,n,m):
    for l in range(n):
        a[l]=quick2(a[l],m)
    return a
def quick2(a,m):
    if a.size <=1:
        return a
    else:
        q = rand.choice(a)
        s_nums = []
        m_nums = []
        e_nums = []
        for i in range(m):
            if a[i] < q:
                s_nums.append(a[i])
            elif a[i] > q:
               m_nums.append(a[i])
            else:
               e_nums.append(a[i])
        sm = np.array(s_nums)
        mm = np.array(m_nums)
        em = np.array(e_nums)
        #print(sm)
        b=np.append(quick2(sm,sm.size), em)
        b=np.append(b, quick2(mm,mm.size))
        return b

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап
        heapify(arr, n, largest)

def heapSort(arr,n):
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап
        heapify(arr, i, 0)
    return arr


def pityrsort(a,n,m):
    for l in range(n):
        a[l]=heapSort(a[l],m)
    return a

m = 50
n = 50
min_limit = -250
max_limit = 1013
matrix = rand.randint(min_limit,max_limit,(m,n))

#np.sort
mas=matrix
loop_start = time.perf_counter()
print(np.sort(mas, axis = 1))
now = time.perf_counter()
print(now-loop_start)

#Выбором
mas=matrix
loop_start = time.perf_counter()
print(switchsort(mas,n,m))
now = time.perf_counter()
print(now-loop_start)

#Вставкой
mas=matrix
loop_start = time.perf_counter()
print(pastesort(mas,n,m))
now = time.perf_counter()
print(now-loop_start)

#Обменом
mas=matrix
loop_start = time.perf_counter()
print(switchsort(mas,n,m))
now = time.perf_counter()
print(now-loop_start)

#Шелла
mas=matrix
loop_start = time.perf_counter()
print(shellsort(mas,n,m))
now = time.perf_counter()
print(now-loop_start)

#Турнирная и Пирамидальная
mas=matrix
loop_start = time.perf_counter()
print(pityrsort(mas,n,m))
now = time.perf_counter()
print(now-loop_start)

#Быстрая
mas=matrix
loop_start = time.perf_counter()
print(quicksort(mas,n,m))
now = time.perf_counter()
print(now-loop_start)
