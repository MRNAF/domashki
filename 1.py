#1
N = int(input())
f = [1, 1]
for i in range(2, N):
    f.append(f[i-1]+f[i-2])
print(f[N-1])

#2
n = int(input())
nn = []
for i in range(2, n):
    if n%i == 0 and n != i:
        nn.append(i)
        break
if len(nn) > 0:
    print('не простое')
else:
    print('простое')
print(nn)


#3
n = int(input())
d = 2
nn = []
for i in range(2, n):
    if n%i == 0 and n != i:
        while i%d != 0 and d<=i:
            d+=1
        if d == i:
            nn.append(i)
        d = 2
if len(nn)>0:
    print('Простые делители числа',n,':', *nn)
else:
    print(n, 'простое число')


#4
m = int(input())
n = int(input())
d = []
for i in range(1, abs(m-n)+1):
    if m%i == 0 and n%i == 0:
        d.append(i)
print(max(d))


#5
n = int(input())
for i in range(n):
    print('*'* n, '\t')

#6
a = int(input())
b = int(input())
for i in range(a):
    print('*'*b)

#7
a = int(input('Введите длину '))
b = int(input('Введите высоту '))
mx = [[0]*a for _ in range(b)]
i = 1
x = 0
y = 0
while i <= a*b:
    if y<b and x < a:
       mx[y][x] = i
       y += 1
       i += 1
    elif y>=b and x<a:
        x+=1
        while y!=0:
            y-=1
            mx[y][x] = i
            i+=1
        x+=1
for i in mx:
    print(*i)






