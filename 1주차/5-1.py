# 행렬 a + 행렬 b => 행렬 c 리턴
def matrixAdd(n, m, a, b):
    c = []
    for i in range(n):
        c.append([])
        for j in range(m):
            c[i].append(a[i][j] + b[i][j])
    return c

# 입력
n, m= map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

# 출력
c = matrixAdd(n, m, a, b)
for i in range(n):
    print(' '.join(list(map(str, c[i]))))

