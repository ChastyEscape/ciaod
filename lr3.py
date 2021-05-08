def prefics(s):
    p = []
    j = 0
    i = 1
    p.append(0)
    while len(p) != len(s):
        if s[i] == s[j]:
            p.append(j+1)
            j += 1
            i += 1
        else:
            if j == 0:
                p.append(0)
                i += 1
            else:
                j = p[j-1]
    return p


def kmp(s, f):
    p = prefics(s)
    l = len(f)
    counter = 0
    k=len(s)
    i=0
    j=0
    while len(s) > 0:
        if s[i] == f [i]:
            i += 1
        else:
            if i != 0:
                s = s[1+p[i-1]:]
                counter += 1+p[i-1]
            else:
                s = s[1:]
                counter+=1
            print(i, s, f)
            i = 0

        if i == l:
            return counter - 1
    return -1

def gen_table(s):
    r = s[::-1]
    index_list = []
    use_list = []
    box = r
    r = r[1:]
    counter = 0
    for i in r:
        counter += 1
        res = simple_find (use_list,i)
        if res == -1:
            index_list.append(counter)
            use_list.append(i)
        else:
            index_list.append(res+1)

    index_list = index_list[::-1]
    res = simple_find (use_list,box[0])

    if res == -1:
        index_list.append(len(r)+1)
        use_list = use_list[::-1]
        use_list.append(box[0])
        use_list = use_list[::-1]
    else:
        index_list.append(res+1)

    return index_list, use_list


def bm(s, f):
    index_list,use_list = gen_table(f)
    last = len(f) - 1
    global_counter = 0
    while len(s) > 0:
        #print(f, s)
        if len(s) < len(f):
            return -1
        if f[last] != s[last]:
            print("stage1", f, s)
            res = simple_find(f, s[last])
            if res == -1:
                s = s[index_list[-1]:]
                global_counter += index_list[-1]
            else:
                print(index_list[res], s[last])
                s = s[index_list[res]:]
                global_counter += index_list[res]
                
        else:
            counter = 0
            for i in range(len(f)):
                print("stage2", f[i], s[i])
                if f[i] == s[i]:
                    counter += 1
                else:
                    counter = 0
                    s = s[index_list[i]:]
                    global_counter += index_list[i]
                    break
                if counter == last + 1 :
                    print(counter, last + 1)
                    return global_counter - 1
    return -1

        
def simple_find(l, k):
    index = -1
    counter = 0
    for i in l:
        if i == k:
            index = counter
        counter += 1
    return index        


print(kmp("abcabeabcabcabd","abcabd"))
print(bm("abcabeabcabcabd","abcabd"))

