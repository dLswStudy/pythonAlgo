a = input()
b = input()
def zigzag(a, b):
    result = ''
    for i in range(8):
        result += a[i] + b[i]
    return result

koonghap = list(map(int, zigzag(a, b)))
while len(koonghap) > 2:
    next = []
    for i in range(len(koonghap)-1):
        next.append((koonghap[i] + koonghap[i+1]) % 10)
    koonghap = next

print(str(koonghap[0]) + str(koonghap[1]))
