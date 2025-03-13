N = int(input())
arr = []
for i in range(N):
    time = list(map(int, input().split()))
    if time[0] > time[1]:
        print("error")
        exit()
    arr.append(time)

T = int(input())

count_passengers = sum(1 for a, b in arr if a <= T <= b)
print(count_passengers)