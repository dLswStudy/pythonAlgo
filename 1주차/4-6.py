alpha = ['A','B','C','D','E','F','G','H','I'
    ,'J','K','L','M','N','O','P','Q','R'
    ,'S','T','U','V','W','X','Y','Z']
def palindrome(name):
    global alpha
    cntList = [0]*26
    isNameOdd = len(name) % 2 == 1 # 입력문자열 길이가 홀수인지
    oddC_cnt = 0 # 홀수개인 알파벳 갯수
    oddC_idx = None # 홀수개인 알파벳 인덱스
    resHalf = ''
    res = ''

    # 알파벳 카운팅
    for o in name:
        cntList[alpha.index(o)] += 1

    # 홀수개인 알파벳 갯수,인덱스 구하기
    # cnt 개수 모두 절반으로 나누기
    for idx, cnt in enumerate(cntList):
        if cnt == 0:
            continue
        if cnt%2 == 1:
            oddC_cnt += 1
            if oddC_cnt == 2:
                return "I'm Sorry Hansoo"
            oddC_idx = idx
            cntList[idx] -= 1
        cntList[idx] = int(cntList[idx]/2)

    # 유효성 검사, 출력 문자열 절반 생성
    for idx, cnt in enumerate(cntList):
        # < 유효성 검사 >
        # 입력 문자열 길이
        # -> 홀수 -> 알파벳 홀수개짜리 1개 있어야함
        # -> 짝수 -> 알파벳 홀수개짜리 없어야함
        if not (
                (isNameOdd and oddC_cnt == 1) or
                (not isNameOdd and oddC_cnt == 0)
        ):
            return "I'm Sorry Hansoo"

        # 출력 문자열 절반 생성
        for _ in range(cnt):
            resHalf += alpha[idx]

    # 함수 종료
    return resHalf + (alpha[oddC_idx] if isNameOdd else '') + resHalf[::-1]

#입출력
print(palindrome(input()))


