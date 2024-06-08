from heapq import heapify, heappop
import sys
input = sys.stdin.readline

n = int(input())
# [4 1 2 7 8] or [7 8 9] or [2] or [1] ...
soldsHeap = list(map(int, input().split()))
heapify(soldsHeap)
prevPop = heappop(soldsHeap)
# 첫 heappop 이 1보다 큰 경우
if prevPop > 1:
    print(1)
# 첫 heappop 이 1 인 경우
else:
    while soldsHeap:
        nextPop = heappop(soldsHeap)
        # 다음 heappop 과 이전 heappop
        #   -> 연속적
        if nextPop - prevPop == 1:
            prevPop = nextPop
        #   -> 불연속적
        else:
            break
    print(prevPop + 1)
