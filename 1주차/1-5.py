# 오늘은 2007년 1월 1일 월요일이다.
# 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다.
# 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지,
# 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
#
# 출력
# 첫째 줄에 x월 y일이 무슨 요일인지에 따라
# SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.


import sys
input = sys.stdin.readline

x, y = map(int, input().split())
lastDates = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']

totDays = 0
for idx, date in enumerate(lastDates):
    month = idx+1

    # (idx+1)월의 일 수 더하기
    if x != month:
        totDays += date
        continue
    # y 일 더하기
    else:
        totDays += y
        break

# 요일 구하기
dayNum = totDays % 7
print(days[dayNum-1])




