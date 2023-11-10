from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters
from string import digits
#1
txt = input()
def upp(txt):
    TXT = ''
    for i in txt:
        if i in ascii_lowercase:
            index = ascii_lowercase.index(i)
            i = ascii_uppercase[index]
        TXT += i
    print(TXT)
upp(txt)

#2
txt = input()
def mirror(txt):
    TXT = ''
    for i in txt:
        if i in ascii_letters:
            index = ascii_letters.index(i)
            n = index - len(ascii_letters)//2
            i = ascii_letters[n]
        TXT += i
    print(TXT)
mirror(txt)

#3
a = input()
b = input()
base1=int(input())
base2=int(input())
def sum_convert(a, b, base1, base2):
    s = digits + ascii_uppercase
    def convert10(x):
        ten = 0
        p = len(x) - 1
        for i in x:
            ten += s.index(i) * (base1 ** p)
            p -= 1
        return(ten)
    ten = convert10(a)+convert10(b)
    d = 1
    x = ''
    while ten >= base2:
        d = s[ten % base2]
        ten = ten // base2
        x += str(d)
    print(str(ten)+x[::-1])
sum_convert(a, b, base1, base2)