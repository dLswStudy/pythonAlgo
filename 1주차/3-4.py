import time
start_time = time.process_time()

n = int(input())
fList = [0, 1, 1]
for m in range(3, 41):
    fList.append(fList[m-1] + fList[m-2])
print(fList[n], n-2)

def fib(n):
    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    f = [0]*(n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n):
        f[i] = f[i-1]+f[i-2]
    return f[n]

end_time = time.process_time()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")