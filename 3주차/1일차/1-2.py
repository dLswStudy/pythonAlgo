nums = list(map(int, input().split(':')))
def timeMachine():
    cntAbleHour = 0
    for num in nums:
        if 1 <= num <= 12:
            cntAbleHour += 1
        if num < 0 or 59 < num:
            print(0)
            return
    print(cntAbleHour * 2 if cntAbleHour > 0 else 0)
timeMachine()