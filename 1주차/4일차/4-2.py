word = input()
cnt = 0
res = ''
for c in word:
    cnt += 1
    res += c
    if cnt%10 == 0:
        res += '\n'
print(res)