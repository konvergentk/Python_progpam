print('Hello human')
a = int(input('введите число '))
c = int(input('введите систему счисления '))
s = str()
i = 0
j = 10
d = {10: 'A',
     11: 'B',
     12: 'C',
     13: 'D',
     14: 'E',
     15: 'F'}
while a > 0:
    if a % c > 0:
        i = a % c
        if i > 9:
            while j < 17:
                if i == j:
                    i = d[j]
                j += 1
        a //= c
        s += str(i)
    else:
        a //= c
        s += '0'
s = s[::-1]
print(s)
