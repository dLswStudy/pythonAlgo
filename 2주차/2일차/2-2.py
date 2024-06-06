import sys
input = sys.stdin.readline

SX_Dict = {'STRAWBERRY':0, 'BANANA':0, 'LIME':0, 'PLUM':0}
for _ in range(int(input())):
    S, X = input().split()
    SX_Dict[S] += int(X)
if 5 in SX_Dict.values():
    print('YES')
else:
    print('NO')