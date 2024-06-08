brackets = list(input())
stack = []
cnt = 0

for _ in range(len(brackets)):
    pop = brackets.pop()
    # 세트 완성 -> 제거
    if stack and pop == '(' and stack[-1] == ')':
        stack.pop()
    # 스택으로 옮기기
    else:
        stack.append(pop)
print(len(stack))