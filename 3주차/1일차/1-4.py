import math
import sys
input = sys.stdin.readline

t = int(input())
lecTimes = [int(input()) for _ in range(t)]
def maxDelay(lt):
    for delay in range(math.floor(lt**0.5), -1, -1):
        if delay+delay**2 <= lt:
            return delay

for lt in lecTimes:
    print(maxDelay(lt))