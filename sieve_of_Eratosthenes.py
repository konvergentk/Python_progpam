#sieve of Eratosthenes

n = int(input("вывод простых чисел до"))
a = [0] * n
b = []

for i in range(2, n):
    a[i] = i
 
m = 2
while m < n:
    if a[m] != 0:
        j = m * 2
        while j < n:
            a[j] = 0
            j = j + m
    m += 1
 
for i in a:
    if a[i] != 0:
        b.append(a[i])
 
del a
print(b)
