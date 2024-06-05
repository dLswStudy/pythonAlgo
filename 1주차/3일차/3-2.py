n = int(input())
# print(int(n*(n-1)*0.5))
cnt = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        cnt += 1
print(cnt)
print(2)
