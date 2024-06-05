# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# 풀이법:
# 1. 가운데 한줄을 mid, 그 위 줄들을 top, 아래 줄들을 bot 으로 설정
# 2. N-1 회 반복문 진행하면서 top, bot 을 같이 만들기
# 3. top 의 가장 윗줄, bot 의 가장 윗줄 부터 동시에 만들기
# 4. top, bot 의 각 줄은 왼쪽, 오른쪽 나누고 줄의 왼쪽을 먼저 만들기
# 5. 줄의 오른쪽은 줄의 왼쪽을 뒤집어서 만들고 합치면 한 줄 완성

N = int(input())
top = ''
mid = "*" * N * 2 +'\n'
bot = ''
for i in range(N-1):
    n = i+1
    topRow = ''
    botRow = ''
    topLeft = '*' * n + ' ' * (N-n)
    botLeft = '*' * (N-n) + ' ' * n
    topRow += topLeft + topLeft[::-1] + '\n'
    botRow += botLeft + botLeft[::-1] + '\n'
    top += topRow
    bot += botRow

print(top+mid+bot)