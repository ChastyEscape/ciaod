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

def sort_names_daques():
    books = ["aac", "ca", "bbbb", "bbbba","bbc"]

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

         
print(sort_names_daques())