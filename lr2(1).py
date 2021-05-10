import numpy as np
import random


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


m, a = generate_m()
print(m, a)
print(binary_find(m, a))

t, a = generate_tree(m, a)
print(a)
print(t.find(a).v)

print(fibonaci(m,a))
