# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

N = int(input("숫자 N(1 ≤ N ≤ 100)을 입력하세요: "))
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