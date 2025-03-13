def matrix_multiply(A, B, n):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

if __name__ == "__main__":
    n = int(input().strip())

    A = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        A.append(row)


    B = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        B.append(row)

    result = matrix_multiply(A, B, n)

    for row in result:
        print(" ".join(map(str, row)))
