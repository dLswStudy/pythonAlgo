import time
n = int(input())
start_time = time.process_time()

# (n-2)*((n-2)+1)/2+(n-3)((n-3)+1)/2+...+1*(1+1)/2
# -> 풀이법 case 1. ChatGPT(수학,, 시그마....엄청...) : (n-2)(n-1)n/6
# -> 풀이법 case 2. for문 이용방법 : m <- 2 to n-1  : sum (1/2)*[(n-m)*(n-m+1)]

sum = 0
for m in range(2, n-1+1):
    sum += int(0.5*(n-m)*(n-m+1))
print(sum)
print(3)
end_time = time.process_time()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")