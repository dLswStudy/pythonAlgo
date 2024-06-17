k, l = map(int, input().split())

_1stFactor = -1
for num in range(2, l):
    if k % num == 0:
        _1stFactor = num
        break

if _1stFactor == -1:
    print('GOOD')
else:
    print('BAD', _1stFactor)