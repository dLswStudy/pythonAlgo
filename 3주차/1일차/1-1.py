from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for three in combinations(cards, 3):
    _sum = sum(three)
    if _sum <= m:
        result = max(result, _sum)
print(result)