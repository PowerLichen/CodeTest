#10830: 행렬 제곱
# 제곱 횟수를 분할정복하며, 이전에 계산된 결과값을 딕셔너리에 저장한다.

n, b = map(int, input().split())


def productMatrix(arr1, arr2):
    global n
    result = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += arr1[i][k] * arr2[k][j]
            result[i][j] %= 1000
    return result

def merge(matrixlog, num):
    if num in matrixlog:
        return matrixlog[num]

    mid = num // 2

    arr1 = merge(matrixlog, mid)
    arr2 = merge(matrixlog, num - mid)

    result_arr = productMatrix(arr1, arr2)
    matrixlog[num] = result_arr

    return result_arr


matrix = [list(map(int,input().split())) for _ in range(n)]

matrixlog = dict()

matrixlog[1] = matrix


for arr in merge(matrixlog, b):
    for num in arr:
        print(num % 1000, end=' ')
    print()
