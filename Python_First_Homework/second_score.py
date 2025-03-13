n = int(input())
a = list(input())

last_max = max(a)
a.remove(max(a))

while (last_max == max(a)):
    last_max = max(a)
    a.remove(max(a))

if (last_max != max(a)):
    print(max(a))