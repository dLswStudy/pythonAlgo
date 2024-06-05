# 8979번 올림픽
# 입력 ----------------------------------------------------------------
n, k = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

# 풀이 ----------------------------------------------------------------
# 정렬
infos.sort(key=lambda x:(-x[1],-x[2],-x[3]))
# 중복 제거
rank = 1
for i in range(n):
    if infos[i][0] == k:
        break
    if infos[i][1:] != infos[i+1][1:]:
        rank += 1

# 출력 ----------------------------------------------------------------
print(rank)
