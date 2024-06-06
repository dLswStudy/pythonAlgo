import sys
input = sys.stdin.readline

_I_know = {} # KEY: 첫 세 음, VALUE: 노래 제목
n, m = map(int,input().split())
for _ in range(n):
    infos = input().split() # ['11', 'TwinkleStar', 'C', 'C', 'G', 'G', 'A', 'A', 'G']
    _3notes = ''.join(infos[2:5])
    _I_know[_3notes] = '?' if _3notes in _I_know else infos[1]
tests = [input().rstrip().replace(' ','') for _ in range(m)]
for test_3notes in tests:
    print(_I_know.get(test_3notes, '!'))