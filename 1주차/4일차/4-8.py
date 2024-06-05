# 고찰
# 가장 단순하게 for문 중첩으로 진행할시 최대 N * 최대 M 으로 10^12 가 나옴. 시간복잡도 고려시 실패.
# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# 예제:
# OO(IOI)OIOIIOII
# OOIO(IOI)OIIOII
# OOIOIO(IOI)IOII
# OOIOIOIOI(IOI)I
# => !발견 : P3 엔 P1 이 3개가 보임.
# => 거꾸로 OOIOIOIOIIOII 에 최대로 들어갈수있는 P_N을 찾고
# 해당 N 이하로 for문을 돌리면 for 문 size 를 줄일수있겠다!

# 2N+1 -> M     (M-1)/2 -> N
# M:13 일 때 N은 6  -> P_6 이하로 for 문 일치하는게 있는지.
# -> 여러가지 경우 수 시뮬레이션
# OOIOIOIOIIOII 에는 P_3, P_1 이 있음.  OO(IOIOIOI)(IOI)I
# ...
# 여기서 나는 무슨 사고를 거쳤을까? 아래의 KEY 사고는 중요한 문제해결 과정인데.
#   위에 글까지 사고를 거쳐와서 바로 위에 오니 OO 와 I 가 거슬리는 느낌을 받았다.
#   -> 불필요해보이는데 처리좀 하면 .. 어?
# ...
# 그냥 제거도 해보고 2개짜리를 한개짜리로 바꿔보다가 이상한점. 매끄럽지않은점을 보고 콤마처리를 생각하게됨.
# ...
# KEY 사고까지 오게됨 : 연속된 OO, II 처리 : O+ -> , (콤마처리), II -> I, I 콤마로 분리
# 막 만든 예시: OOOIIOIIIIOIOIOOOIOOIIOO  -> 콤마처리 진행
# 00 처리 -> ,IIOIIIIOIOI,I,II,
# II 처리 -> ,I,IOI,I,I,IOIOI,I,I,I,
# I 제거 -> IOI, IOIOI   !! 뭔가 깔끔히 도출되었다.
# 검증: OOOI(IOI)II(IOIOI)OOOIOOIIOO  : 축약? 프로세스 검증완료

# 이번엔 코드로 실제 진행해본다.

def n_to_pn(n):
    return 'IO' * n + 'I'

# def handle_O(s):
#     return re.sub(r'O+', ',', s)

# OO 처리를 이렇게까지 해야되나? -> II 처리는 쉬운데. -> 아 OO 도 O,O로 바꾸면되겠구나.
# 이슈! O,OIOIOIOI,IOI,I
# I(O+)I 처리 : IOOI -> I,O,O,I / IOO -> I,O,O / OOI -> O,O,I

import re
def zip_str(_str):
    # return (_str.strip('O').replace('IOOI','I,O,O,I').replace('IOO','I,O,O').replace('OOI','O,O,I')
    #         .replace('OO','O,O').replace('II','I,I').replace('II','I,I'))
    _str = _str.strip('O')
    print(_str)
    _str = re.sub(r'O+', ',', _str)
    _str = re.sub(r'I+', 'I,I', _str)
    return _str

def ioicnt_in_iois(iois, n_of_ioi):
    n_of_iois = (len(iois)-1)/2
    return n_of_iois - n_of_ioi + 1 if n_of_iois >= n_of_ioi else 0

def cnt_pn(n, m, _str):
    cnt = 0
    _str = zip_str(_str)
    print(_str)
    # _str_listed = _str.split(',')
    # print(_str_listed)
    iois_list = _str.split(',')
    print(iois_list)
    # iois_list = [x for x in _str_listed if x != 'O' and x != 'I'] # 예: ['IOIOIOI', 'IOI']
    for iois in iois_list:
        cnt += ioicnt_in_iois(iois, n)
    return int(cnt)

print(cnt_pn(int(input()), int(input()), input()))