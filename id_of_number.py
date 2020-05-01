objects = [1, 3, 5, 3, 3]
a = 0
s = 0
for i in range(len(objects)):
    for j in range(i + 1, len(objects)):
        if objects[i] is objects[j]:
            a += 1
    if a == 0:
        s += 1
    a = 0
print(s)
