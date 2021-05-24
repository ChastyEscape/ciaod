"""
    Тимонин БФИ1901
    «Задачи на строки»:
            1) Даны две строки: s1 и s2 с одинаковым размером, проверьте, может ли
        некоторая перестановка строки s1 “победить” некоторую перестановку
        строки s2 или наоборот.
        Строка x может “победить” строку y (обе имеют размер n), если x[i]> = y
        [i] (в алфавитном порядке) для всех i от 0 до n-1. 
	
	- def win_str(s1,s2):
	

            2) Дана строка s, вернуть самую длинную полиндромную подстроку в s.
	    
	- def polistr(s):

            3)Вернуть количество отдельных непустых подстрок текста, которые могут
        быть записаны как конкатенация некоторой строки с самой собой (т.е. она
        может быть записана, как a + a, где a - некоторая строка).
	
	- def substr(s):
"""


def win_str(s1,s2):
    sort1 = []
    sort2 = []
    for i in s1:
        sort1.append(ord(i))
    for i in s2:
        sort2.append(ord(i))
    sort1.sort()
    sort2.sort()
    l = len(sort1)
    count1 = 0
    count2 = 0
    for i in range(l):
        if sort2[i] < sort1[i]:
            count1 += 1
        elif sort1[i] < sort2[i]:
            count2 += 1
    if count1 != 0 and count2 == 0:
        return True
    elif count2 != 0 and count1 == 0:
        return True
    else:
        return False

def find(s,current):
    l = 0
    last = current - 1
    pol = ''
    while (last != -1) and (current != len(s)):
        if s[last] == s[current]:
            pol = s[last] + pol + s[current]
            l += 1
        else:
            return l,pol
        last -= 1
        current +=1
    return l,pol

def findn(s,current):
    l = 0
    last = current - 1
    pol = s[current]
    current += 1
    while (last != -1) and (current != len(s)):
        if s[last] == s[current]:
            pol = s[last] + pol + s[current]
            l += 1
        else:
            if l != 0:
                return l,pol
            else:
                return l,''
        last -= 1
        current +=1
        l+=1
    return l,pol


def polistr(s):
    l = 0
    pol = ''
    if len(s) == 1:
        return s
    for i in range(1,len(s)):
        now_l, now_pol = find(s,i)
        if now_l > l:
            l = now_l
            pol = now_pol
    for i in range(1,len(s)):
        now_l, now_pol = findn(s,i)
        if now_l > l:
            l = now_l
            pol = now_pol
    return pol


def substr(s):
    l = len(s)/2
    counter = 0
    part_list = []
    for i in range(1,int(l)+1):
        st = s
        while len(st) > 1:
            if st[:i] == st[i:2*i]:
                if st[:i] in part_list:
                    pass
                else:
                    part_list.append(st[:i])
                    counter += 1
            st = st[1:]
    return counter


def main():
    print(win_str("abe", "acd"))
    print(polistr('c'))
    print(substr('abcabcabc'))


if __name__ == "__main__":
	main()
