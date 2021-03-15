import math
import numpy as np
import numpy.random as rand

def main():
    #print(triangle([1,2,1]))
    #print(maxnum([3,30,34,5,9]))
    m = 3
    n = 4
    min_limit = 1
    max_limit = 100
    matrix = rand.randint(min_limit,max_limit,(m,n))
    print(matrix)

#Треугольник с максимальным периметром
def triangle(nums):
    if(len(nums)<3):
        return 0
    last = 2
    middle = 1
    first = 0
    num_last = len(nums)-1
    num_middle = num_last-1
    num_first = num_middle-1
    sum=0
    while first<=num_first:
        if nums[last]+nums[first]+nums[middle] > sum:
            if (nums[last]<nums[first]+nums[middle]) and (nums[first]<nums[last]+nums[middle]) and (nums[middle]<nums[last]+nums[first]):
                #проверка условия что каждая сторона меньше суммы двух других
                sum = nums[last]+nums[first]+nums[middle]
        if last<num_last:
            last+=1
        else:
            if middle<num_middle:
                middle+=1
                last=middle+1
            else:
                first+=1
    return sum

#Максимальное число
def maxnum(nums):
    strums = []
    for i in nums:
        strums.append(str(i))
    result = []
    startlen = len(strums)
    while len(result)<startlen:
        max='0'
        for i in strums:
            if len(i)<len(max):
                if int(max)<int(i)*10**(len(max)-len(i)):
                    max=i
            elif len(i)>len(max):
                if int(i)>int(max)*10**(len(i)-len(max)):
                    max=i
            else:
                if int(i)>int(max):
                    max=i
        result.append(max)
        strums.remove(max)
    resstr=''
    for i in result:
        resstr=resstr+i
    return resstr       

#сортировка по дмагонали
def diagonalsort(matrix,m,n):
    k=abs(m-n)
    start_coll
    if(n>m):
        while k>=0:

            for i in range (m):


if __name__ == "__main__":
	main()