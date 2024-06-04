# 행렬 matrix -> [최대값, 행 idx, 열 idx]
def findMax(matrix):
    max = 0
    n, m = 0, 0
    for i in range(9):
        for j in range(9):
            if matrix[i][j] > max:
                max = matrix[i][j]
                n, m = i, j
    return [max, n, m]

# 입력
matrix = []
for _ in range(9):
    matrix.append(list(map(int, input().split())))

# 출력
info = findMax(matrix)
print(info[0])
print(f'{info[1] + 1} {info[2] + 1}')