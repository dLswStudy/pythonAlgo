# maxLen(단어 최대 길이) , matrix(5 * maxLen 행렬) -> 세로로 쭉 붙여서 읽은 문자열
def readVertically(maxLen, matrix):
    res = ''
    for j in range(maxLen):
        vtcLine = ''
        for i in range(5):
            if matrix[i][j]:
                vtcLine += matrix[i][j]
        res += vtcLine
    return res

# 입력
matrix = []
maxLen = 0
for _ in range(5):
    l = list(input())
    matrix.append(l)
    if len(l) > maxLen:
        maxLen = len(l)
for i in range(5):
    lenOfi = len(matrix[i])
    if lenOfi < maxLen:
        matrix[i].extend([''] * (maxLen - lenOfi))

# 출력
print(readVertically(maxLen, matrix))
