from typing import Counter


class Stack:
    def __init__(self):
        self.list = []
    def addb(self, x):
        self.list.insert(0, x)
    def get(self):
        return self.list
    def out(self):
        o = self.list[0]
        self.list = self.list[1:]
        return o


class Deque(Stack):
    def __init__(self):
        super().__init__()
    def adde(self, x):
        self.list.append(x)
    def lout(self):
        o = self.list[-1]
        self.list = self.list[:len(self.list)-1]
        return o

def sort_names_daques(books):
    d0 = Deque()
    d1 = Deque()

    c = len(books)*len(books)*2 - len(books)
    flag = 0
    counter = 0
    lb = len(books)

    while len(books) > 0:
        d0.adde(books[0])
        books = books[1:]


    for i in range(c):
        if len(d1.get()) == lb:
            flag = 1
            counter +=1
            #print(counter, d0.get(), d1.get())
        if len(d0.get()) == lb:
            flag = 0
            counter +=1
            #print(counter, d0.get(), d1.get())
        if flag == 0:
            if len(d1.get()) == 0:
                d1.addb(d0.out())
            elif len(d1.get()) == 1:
                o = d0.out()
                temp = d1.out()
                if o < temp:
                    d1.addb(temp)
                    d1.addb(o)
                else:
                    d1.addb(o)
                    d1.addb(temp)
            else:
                start = d1.out()
                end = d1.lout()
                o = d0.out()
                if o < start:
                    d1.addb(start)
                    d1.addb(o)
                    d1.adde(end)
                else:
                    d1.addb(start)
                    d1.adde(end)
                    d1.adde(o)
        else:
            if len(d0.get()) == 0:
                d0.addb(d1.lout())
            elif len(d0.get()) == 1:
                o = d0.lout()
                temp = d1.out()
                if o < temp:
                    d0.addb(temp)
                    d0.addb(o)
                else:
                    d0.addb(o)
                    d0.addb(temp)
            else:
                start = d0.out()
                end = d0.lout()
                o = d1.out()
                if o > end:
                    d0.addb(start)
                    d0.adde(end)
                    d0.adde(o)
                else:
                    d0.addb(start)
                    d0.addb(o)
                    d0.adde(end)
    return d1.get()

         
def decoding(coding):
    message = ""
    l = len(coding)
    d = Deque()
    d.adde('a')
    d.adde('b')
    d.adde('c')
    d.adde('d')
    d.adde('e')
    d.adde('f')
    while len(message) < l:
        s = coding[0]
        coding = coding[1:]
        flag = False
        probel = False
        while flag == False:
            if s == ' ':
                flag = True
                probel = True
            else:
                cs = d.out()
                if cs == s:
                    flag = True
                d.adde(cs)
        if probel == True:
            message = message + ' '
        else:
            last = d.lout()
            prelast = d.lout()
            isk = d.lout()
            message = message + isk
            d.adde(isk)
            d.adde(prelast)
            d.adde(last)
    return message


def brackets(message):
    open = 0
    close = 0
    s = Stack()
    l = len(message)
    while len(message) != 0:
        s.addb(message[0])
        message = message[1:]
    for i in range(l):
        o = s.out()
        if o == '(':
            open+=1
        if o == ')':
            close +=1
    if open == close:
        return True
    else:
        return False


def square_brackets(message):
    open = 0
    close = 0
    s = Deque()
    l = len(message)
    while len(message) != 0:
        s.addb(message[0])
        message = message[1:]
    for i in range(l):
        o = s.out()
        if o == '[':
            open+=1
        if o == ']':
            close +=1
    if open == close:
        return True
    else:
        return False


def groupes(message):
    s = Stack()
    l = len(message)
    while len(message) != 0:
        s.addb(message[0])
        message = message[1:]
    nums = ""
    chars = ""
    symbs = ""
    for i in range(l):
        o = s.out()
        if o >= '0' and o <= '9':
            nums += o
        elif (o >= 'A' and o <= 'Z') or (o >= 'a' and o <= 'z'):
            chars += o
        else:
            symbs += o
    return nums[::-1], chars[::-1], symbs[::-1]


def groupenums(message):
    plus = ""
    minus = ""
    d = Deque()
    nums = message.split(' ')
    l = len(nums)
    for i in nums:
        d.adde(i)
    while len(d.get()) > 0:
        o = int(d.out())
        if o >= 0:
            plus += str(o) + ' '
        else:
            minus += str(o) + ' '
    return plus, minus


def reverse(str_list):
    s = Stack()
    l = len(str_list)
    for i in str_list:
        s.addb(i)
    reverse_list = []
    for i in range(l):
        reverse_list.append(s.out())
    return reverse_list


def reverse_stack(s):
    new = Stack()
    while len(s.get()) > 0:
        new.addb(s.out())
    return new


def notv(v):
    if v == 'T':
        return 'F'
    else:
        return 'T'


def transl(v):
    if v == 'T':
        return True
    else:
        return False


def retransl(v):
    if v == True:
        return 'T'
    else:
        return 'F'


def logstack(message):
    message = message[1:-1]
    s = Stack()
    brack = False
    nested = "("
    for i in message:
        if brack == False:
            if (i == 'T') or (i == 'F') or (i == 'N') or (i == 'O') or (i == 'A') or (i == 'X'):
                s.addb(i)
            else:
                brack = True
        else:
            if i == ')':
                nested += i
                r = logstack(nested)
                s.addb(r)
                brack = False
                nested = "("
            else:
                nested += i
    s = reverse_stack(s)
    result = s.out()
    while len(s.get()) > 0:
        if result == 'N':
            result = notv(s.out())
        else:
            v = s.out()
            if v == 'A':
                first = transl(result)
                last = transl(s.out())
                locres = first and last
                result = retransl(locres)
            elif v == 'O':
                first = transl(result)
                last = transl(s.out())
                locres = first or last
                result = retransl(locres)
            else:
                first = transl(result)
                last = transl(s.out())
                locres = (first and not last) or (not first and last)
                result = retransl(locres)
    return result


def formul_stack(message):
    if message[0] != 'M' and message[0] != 'N':
        return message
    else:
        do = message[0]
        message = message[2:-1]
        s = Stack()
        brack = False
        nested = ""
        for i in message:
            if brack == False:
                if i >= '0' and i <= '9':
                    s.addb(i)
                else:
                    nested += i
                    brack = True
            else:
                if i == ')':
                    nested += i
                    r = formul_stack(nested)
                    s.addb(str(r))
                    brack = False
                    nested = "("
                else:
                    nested += i
        s = reverse_stack(s)
        result = s.out()
        if do == 'M':
            max = int(result)
            while len(s.get()) > 0:
                v = int(s.out())
                if v > max:
                    max = v
            return max
        else:
            min = int(result)
            while len(s.get()) > 0:
                v = int(s.out())
                if v < min:
                    min = v
            return min


def term_stack(message):
    if len(message) == 2 or len(message) == 0:
        return False
    if len(message) == 1:
        if message == 'x' or message == 'y' or message == 'z':
            return True
        else:
            return False
    if brackets(message) == False:
        return False
    s = Stack()
    for i in message:
        s.addb(i)
    s = reverse_stack(s)
    last = s.out()
    if last != 'x' and last != 'y' and last != 'z' and last != '(':
        return False
    while len(s.get()) > 0:
        current = s.out()
        if len(s.get()) == 0 and current != 'x' and current != 'y' and current != 'z':
            return False
        if last == 'x' or last == 'y' or last == 'z' or last == ')':
            if current != '+' and current != '-' and current != ')':
                return False
        elif last == '+' or last == '-' or last == '(':
            if current != 'x' and current != 'y' and current != 'z' and current != '(':
                return False
        last = current
    return True


def hanoi_towers(n, afrom, to, middle):
    if n == 1:
        to.addb(afrom.out())
        print (afrom.get(),middle.get(),to.get())
        return
    hanoi_towers(n-1, afrom, middle, to)
    to.addb(afrom.out())
    print (afrom.get(),middle.get(),to.get())
    hanoi_towers(n-1, middle, to, afrom)


print(sort_names_daques(["aac", "ca", "bbbb", "bbbba","bbc"]))
print(decoding("abbae cbdf"))
print(brackets("1 * 7 ((5-3) - (23/3) ) )"))
print(square_brackets("1 * 7 [[5-3] - [23/3] ] "))
print(groupes("abcd 12bd)< 9fdf67?6j"))
print(groupenums("-7 8 14 -67 85 34 -86 99 93 21 -3 -123 67"))
print(reverse(["gsfsgfsdgf", "gdfhgdgf", "gdsfgdfgf", "qreqrewewr"]))
print(logstack("(TO(FAT))"))
print(formul_stack("M(1N(967)25)"))
print(term_stack("x+(y-z)+y"))
a = Stack()
b = Stack()
c = Stack()
a.addb(3)
a.addb(2)
a.addb(1)
print(a.get(),b.get(),c.get())
hanoi_towers(len(a.get()), a, c, b)
