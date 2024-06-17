'''
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고
거스름돈 개수가 가장 적게 잔돈을 준다.

required: 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수
'''
coins = [500, 100, 50, 10, 5, 1]
toPayMoney = int(input())
handOver = 1000
takeCoinCnt = 0

takeAmount = handOver - toPayMoney
for coin in coins:
    if takeAmount == 0:
        break
    takeCoinCnt += takeAmount // coin
    takeAmount %= coin

print(takeCoinCnt)