inp = input().rstrip()
dict = {}
for alpha in inp:
    dict.setdefault(alpha, 0)
    dict[alpha] += 1

ans, center = '', ''
for alpha, cnt in sorted(dict.items()):
    if cnt%2:
        if center != '':
            print("I'm Sorry Hansoo")
            break
        center = alpha
    ans += alpha * (cnt//2)
else:
    print(ans + center + ans[::-1])