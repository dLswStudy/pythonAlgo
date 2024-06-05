n = int(input())
cases = [input().split() for _ in range(n)]

# 풀이 1: [::-1] 사용 / 속도: 40 ms
# for i in range(n):
#     print(f"Case #{i+1}: {' '.join(cases[i][::-1])}")

# 풀이 2: 이중 for문 사용 / 속도: 40 ms
# for i in range(n):
#     stack = []
#     m = len(cases[i])
#     for j in range(m):
#         stack.append(cases[i][m-1-j])
#     print(f"Case #{i+1}: {' '.join(stack)}")

# 풀이 3: while, pop() 사용 / 속도: 40 ms
for i in range(n):
    reverse = ''
    while cases[i]:
        reverse += cases[i].pop()+' '
    print(f"Case #{i+1}: {reverse.rstrip()}")