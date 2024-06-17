'''
맨 처음에는 딸기우유를 한 팩
마신 후에는 초코우유를 한 팩
마신 후에는 바나나우유를 한 팩
마신 후에는 딸기우유를 한 팩
0 1 2
가게는 한 종류의 우유만
각각의 우유 가게 앞에서, 영학이는 우유를 사마시거나, 사마시지 않는다.
딸 초 바 0 1 2
'''
n = int(input())
stores = list(map(int, input().split()))
milk = [0,1,2]

cnt = 0
for i in range(n):
    if stores[i] == milk[(cnt+3) % 3]:
        cnt += 1

print(cnt)