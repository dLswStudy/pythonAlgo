sumPrev = 0
sumNext = 0
for _ in range(10):
    sumNext = sumPrev + int(input())
    if sumNext >= 100:
        break
    sumPrev = sumNext
if abs(100-sumNext) > abs(100-sumPrev):
    print(sumPrev)
else:
    print(sumNext)

