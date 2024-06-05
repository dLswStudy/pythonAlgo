# 입력 -----------------------------------------------
from collections import deque

caseCnt = int(input())
caseList = []
for _ in range(caseCnt):
    # 케이스 별 정보 입력 ----
    docCnt, qIdx = map(int, input().split())
    docMap = map(int, input().split())
    docList = list(docMap) # 인덱싱용으로 중요도 내림차순 정렬 리스트 필요
    docQueue = deque(docList)
    # 케이스 리스트에 케이스 정보 추가 ----
    caseList.append((docCnt, qIdx, docList, docQueue))

# 풀이 -----------------------------------------------
# 이전사고:
# 추적문서보다 작은 중요도의 문서는 다 지워도됨.
# 추적문서보다 2 이상 큰 수도 카운팅만 하고 다 지워도 됨.
# 수정된 사고
# ==> but 덱에서 중간 원소의 접근 및 수정은 시간복잡도(n) 이다.
#   원래 전체 순회하면서 불필요원소들을 삭제하고 시작하려했는데
#   시간복잡도가 n이란걸 알아서 그럴필요 없어졌다.
#   큐로 만들고 인큐, 디큐를 사용해서 전체프로세스를 동시에 처리하며 진행해야곘다.
def chkNthTime_byCase(case):
    docCnt, qIdx, docList, docQueue = case
    qDoc = docList[qIdx] # 추적 문서 중요도
    isPrint_qDoc = False # 추적 문서 프린트 여부
    whatNth = 1 # 몇 번째 출력
    moveCnt = 0 # 원소 자리 이동 횟수


    docList.sort(reverse=True) # [8,6,6,3,1,1,1]
    idxToPrint = 0 # 프린트 할 문서중요도의 인덱스

    if docCnt > 1:
        while True:
            # 디큐
            deQueued = docQueue.popleft()
            moveCnt += 1

            # 1회전 내에 추적할 문서 마킹
            if moveCnt - 1 == qIdx:
                deQueued = str(deQueued)

            # 디큐 -> [정답출력 or 프린트 or 인큐] 정하기
            # 마킹된 문서 & 프린트 할 차례 -> 정답 출력
            if isinstance(deQueued, str) and int(deQueued) == docList[idxToPrint]:
                return whatNth
            # if 중요도 최상 문서
            elif deQueued == docList[idxToPrint]:
                # 프린트! (인큐X)
                idxToPrint += 1
                whatNth += 1
            else:
                # 인큐
                docQueue.append(deQueued)
    else:
        return 1


# 출력 -----------------------------------------------
for case in caseList:
    print(chkNthTime_byCase(case))
