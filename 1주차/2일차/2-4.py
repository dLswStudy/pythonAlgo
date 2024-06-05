# 1157번 문제
word = input().upper()

# 최대 10^6번 반복
cCnt_Dict = {} # Character Cnt 딕셔너리
for c in word:
    if c not in cCnt_Dict:
        cCnt_Dict[c] = 1
    else:
        cCnt_Dict[c] += 1

# !깨달은점: 효율을 위해 for문 사용을 최대한 줄여서 하나의 for문에 많은 로직을 처리하려던
# 사고를 자주 하곤 했었는데 아래처럼 반복횟수가 26번 정도는
# 위에 10^6(컴퓨터는 1초에 10^8번 연산을함)번에 비해 아주 뽀시래기 수준이기 때문에
# 개발편의를 위해 맘껏 사용해도 된다!!
maxCnt = max(cCnt_Dict.values())
maxChrt = ''
for c, cnt in cCnt_Dict.items():
    if cnt == maxCnt:
        # cnt 가 최대인 캐릭터가 2개 이상이면 '?'
        if maxChrt:
            maxChrt = '?'
            break

        maxChrt = c

print(maxChrt)

