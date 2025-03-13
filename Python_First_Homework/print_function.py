n = int(input())
string = str(n)
for i in range(n-1, 0, -1):
    string = str(i) + string

print(string)