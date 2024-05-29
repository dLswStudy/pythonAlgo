# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.


dices = input().split()  # 주사위 눈 배열
prize = 0  # 상금
cntDict = {}  # 주사위 눈별로 카운트를 기록하는 dictionary
for d in dices:
    d = int(d)
    if d not in cntDict:
        cntDict[d] = 1
    else:
        cntDict[d] += 1

isSpots3kind = False # 모두 다른 눈인지
maxSpots = 0 # 가장 큰 눈

# [key, value] = [spots, cnt] (눈, 카운트)
for spots, cnt in cntDict.items():
    # 같은 눈이 3개 나왔을 때
    if cnt == 3:
        prize = 10000 + spots * 1000
        isSpots3kind = True
    # 같은 눈이 2개 나왔을 때
    elif cnt == 2:
        prize = 1000 + spots * 100
        isSpots3kind = True
        break
    # 가장 큰 눈 계산
    else:
        maxSpots = max(maxSpots, spots)

# 모두 다른 눈일 때
if not isSpots3kind:
    prize = maxSpots * 100

# 상금 출력
print(f"상금: {prize}원")


