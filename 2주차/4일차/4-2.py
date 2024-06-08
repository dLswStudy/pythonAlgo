# 1 2 2 3 3 3 4 4 4  4 ...
# 1 2 3 4 5 6 7 8 9 10 ...
#     3   ~   7 => 2 3 3 3 4
# 1+2+3+4+...+n >= 1000   ->    n(n+1) >= 2000    ->    n=45
# 1 2 2 3 3 3 ... 45 45 ... 45

a, b = map(int, (input().split()))
arr = []
cnt = 0
for i in range(46):
    n = i+1
    for _ in range(n):
        if cnt == b:
            break
        arr.append(n)
        cnt += 1

print(sum(arr[a-1:]))