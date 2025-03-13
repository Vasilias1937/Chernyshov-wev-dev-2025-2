def calculate_happiness(arr, a_set, b_set):
    happiness = 0
    for num in arr:
        if num in a_set:
            happiness += 1
        elif num in b_set:
            happiness -= 1
    return happiness

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a_set = set(map(int, input().split()))
    b_set = set(map(int, input().split()))

    print(calculate_happiness(arr, a_set, b_set))
