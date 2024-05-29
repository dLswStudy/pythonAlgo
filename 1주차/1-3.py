# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.
#
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

inputArr = []
T = int(input("테스트 케이스 개수: ")) # 테스트 케이스 개수
for n in range(T):
    R, S = input(f"{n+1}번째 테스트 케이스(반복횟수 문자열): ").split()
    row = (int(R), S)
    inputArr.append(row)

for row in inputArr:
    rowOutput = ''
    for c in row[1]:
        rowOutput += c * row[0]
    print(rowOutput)