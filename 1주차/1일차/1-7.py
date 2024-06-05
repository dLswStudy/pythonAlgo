# 25206 너의 평점은

# 입력 --------------------------------
datas = [input().split() for _ in range(20)]

# 풀이 --------------------------------
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값

# 등급에 따른 과목평점
def subjectGrade(rank):
    ranks = ['A+','A0','B+','B0','C+','C0','D+','D0']
    return 0.0 if rank == 'F' else 4.5 - 0.5 * ranks.index(rank)

sum0 = 0 # (학점 × 과목평점)의 합
sum1 = 0 # 학점의 총합
for data in datas:
    if data[2] == 'P':
        continue
    sum0 += float(data[1]) * subjectGrade(data[2])
    sum1 += float(data[1])

# 출력 --------------------------------
print(round(sum0/sum1, 6))