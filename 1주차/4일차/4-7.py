# 풀이법: 인덱스를 비교
def find_illegal_car(in_cars, out_cars):
    cnt = 0
    for car in out_cars:
        if car == in_cars[0]:
            in_cars.nextPop(0)
            continue
        else:
            cnt += 1
            in_cars.remove(car)

    return cnt

# 입출력
in_cars = []
out_cars = []
n = int(input())
for _ in range(n):
    in_cars.append(input())
for _ in range(n):
    out_cars.append(input())
print(find_illegal_car(in_cars, out_cars))
