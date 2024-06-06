import sys
input = sys.stdin.readline
from heapq import *

heap = []
N = int(input())
xList = [int(input()) for _ in range(N)]
for x in xList:
    if x > 0:
        heappush(heap, x)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)
