import sys
input = sys.stdin.readline

N = int(input())

SX_Dict = {}
for _ in range(N):
    S, X = input().split()
    X = int(X)
    if S not in SX_Dict:
        SX_Dict[S] = X
    else:
        SX_Dict[S] += X

if 5 in SX_Dict.values():
    print('YES')
else:
    print('NO')
   