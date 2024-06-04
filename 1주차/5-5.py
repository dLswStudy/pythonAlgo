# 1018번 체스판 다시 칠하기

# 풀이법:
# 1. 체스판의 유형은 2가지. (0, 0) 자리가 B 로 시작 하는 경우(B 타입), W로 시작하는 경우(W 타입)
# 2. 쭉 이중 루프 돌려서 B 타입, W 타입 어느 쪽이 더 우세한지 확인.
# 3. 8*8 정사각형 영역을 쭉 살펴보면서 우세타입이 가장 많이 잡힐 때를 찾기
# 4. 그 때의 비우세타입 갯수가 정답

def cntToFix(matrix, n, m):
    cntTypeW = 0
    cntTypeB = 0
    boolTypeW = lambda i,j: (((i+j)%2 == 0 and matrix[i][j] == 'W')
                             or ((i+j)%2 == 1 and matrix[i][j] == 'B'))
    typeWorB = ''

    # 우세 타입 검사 ( W 타입 VS B 타입 )
    for i in range(n):
        for j in range(m):
            if boolTypeW(i,j):
                cntTypeW += 1
                matrix[i][j] = 'tw'
            else:
                matrix[i][j] = 'tb'
    cntTypeB = n * m - cntTypeW
    typeWorB = 'W' if cntTypeW >= cntTypeB else 'B'

    # 우세 타입이 가장 많이 잡힐 때 우세 타입 갯수
    maxCnt = 0
    for i in range(0, n-7):
        for j in range(0, m-7):
            cnt88 = cnt8x8(matrix, i, j, typeWorB)
            if cnt88 > maxCnt:
                maxCnt = cnt88

    return 8*8-maxCnt

# i, j (8*8 정사각형의 기준점(top-left 꼭지점 위치)) -> 영역 안 cntType 모두 합산
def cnt8x8(matrix, ia, ja, typeWorB):
    typeOfCnt = 'tw' if typeWorB == 'W' else 'tb'
    return sum(line[ja:ja+8].count(typeOfCnt) for line in matrix[ia:ia+8])

# 입력
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

# 출력
print(cntToFix(matrix, n, m))

