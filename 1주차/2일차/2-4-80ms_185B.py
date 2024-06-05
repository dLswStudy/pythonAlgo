n = input().upper()
n_ = list(set(n))
print(n_)
cnt = []
for i in n_:
    num = n.count(i)
    cnt.append(num)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(n_[cnt.index(max(cnt))])

