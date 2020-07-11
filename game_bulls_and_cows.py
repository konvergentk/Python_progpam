#Быки и коровы(комп загадывает)


#записываем рандом
n = int(input())


a = [0] * 3
b = [0] * 3
i = 2
man = 0
cow = 0

while n > 0:
    a[i] = n % 10
    n //= 10
    i -= 1

while True:
    x = int(input('введите число = '))
    i = 2
    while x > 0:
        b[i] = x % 10
        x //= 10
        i -= 1
    for j in range(3):
        if a[j] == b[j]:
            man += 1
        else:
            if b[j] in a:
                cow += 1
    if man == 3:
        print('You win!!!')
        break
    else:
        print('Быков у нас = ', man)
        man = 0
        print('Коров у нас = ', cow)
        cow = 0
