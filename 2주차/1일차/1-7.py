# 입력 -----------------------------------------------
T = int(input())
testList = [list(input()) for _ in range(T)]
# 풀이 -----------------------------------------------
def isVPS(test):
    if test[-1] == '(':
        return False
    stack = []
    while len(test) > 0:
        pop = test.pop()
        if stack and pop == '(' and stack[-1] == ')':
            stack.pop()
        else:
            stack.append(pop)
    return False if stack else True
# 출력 -----------------------------------------------
for test in testList:
    print('YES' if isVPS(test) else 'NO')