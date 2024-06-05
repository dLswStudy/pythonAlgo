# 행렬 가로세로 반전시키기
def rvsMatrix(matrix):
    return [list(val) for val in zip(*matrix)]

# ..XX...X.X.... -> 4
def cnt2orMore(row, char):
    cnt = 0
    n = len(row)
    i = 0

    while i < n:
        if char == row[i]:
            # 연속된 . 개수 구하기
            pointNum = 0
            while i+pointNum < n and char == row[i+pointNum]:
                pointNum += 1
            # .이 2번 이상 연속한 상태면 카운팅
            if pointNum >= 2:
                cnt += 1
            # 다음 문자로 넘어가기
            i += pointNum
        else:
            i += 1

    return cnt

# matrix(행렬)  -> [{가로로 누울 수 있는 자리수} {세로로 누울 수 있는 자리수}]
def howManyILieDown(matrix):
    horzCnt, vertCnt = 0, 0
    cnts = [horzCnt, vertCnt]
    matrixs = [matrix, rvsMatrix(matrix)]

    for idx, cnt in enumerate(cnts):
        for line in matrixs[idx]:
            cnts[idx] += cnt2orMore(line, '.')
    return cnts

# 입력
n = int(input())
matrix = [list(input()) for _ in range(n)]

# 출력
lieCnt = howManyILieDown(matrix)
print(f'{lieCnt[0]} {lieCnt[1]}')
