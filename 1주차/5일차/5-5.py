# 1018번 체스판 다시 칠하기

# 입력 ----------------------
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

# 풀이 ----------------------
def cntToFix(matrix, n, m):
    boolTypeW = lambda i,j: (((i+j)%2 == 0 and matrix[i][j] == 'W') or
                             ((i+j)%2 == 1 and matrix[i][j] == 'B'))

    for i in range(n):
        for j in range(m):
            if boolTypeW(i,j):
                matrix[i][j] = 'TW'
            else:
                matrix[i][j] = 'TB'
    count = []
    for startI in range(0, n-7):
        for startJ in range(0, m-7):
            cntTypeW = 0
            for i in range(startI, startI + 8):
                for j in range(startJ, startJ + 8):
                    if matrix[i][j] == 'TW':
                        cntTypeW += 1
            count.append(min(cntTypeW, 64-cntTypeW))

    return min(count)

# 출력 ----------------------
print(cntToFix(matrix, n, m))