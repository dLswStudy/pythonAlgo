def returnAnswer(words, whatAns):
    qMarkIdx = words.index('?')
    prevLastC = words[qMarkIdx-1][-1] if qMarkIdx != 0 else ''
    next1stC = words[qMarkIdx+1][0] if qMarkIdx != len(words)-1 else ''

    for what in whatAns:
        if (
                (prevLastC == what[0] if prevLastC else True)
                and (what[-1] == next1stC if next1stC else True)
                and what not in words):
            return what

words = []
whatAns = []
for _ in range(int(input())):
    words.append(input())
for _ in range(int(input())):
    whatAns.append(input())
print(returnAnswer(words, whatAns))



