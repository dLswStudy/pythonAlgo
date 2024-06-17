n = int(input())
k = int(input())
numStrs = [input() for _ in range(n)]
visited = [False] * n

numSet = set()
def recur(stack):
    if len(stack) == k:
        numSet.add(int(''.join(stack[:])))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack.append(numStrs[i])
            recur(stack)
            stack.pop()
            visited[i] = False
recur([])
print(len(numSet))