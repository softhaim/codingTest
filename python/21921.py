# 21921

'''
찬솔이는 
$X$일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.

찬솔이를 대신해서 
$X$일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.
'''

import sys
from collections import defaultdict

N, X = map(int, input().split())
sonnim = list(map(int, input().split()))

visitor_count = defaultdict(int)

# 초기 X일간 방문자 수 계산
current_sum = sum(sonnim[:X])
visitor_count[current_sum] = 1  # 처음 등장한 방문자 합 저장
max_visitors = current_sum

# 슬라이딩 윈도우 적용
for i in range(X, N):
    current_sum += sonnim[i] - sonnim[i - X]  # 새로운 날 추가, 가장 오래된 날 제거

    # 딕셔너리에 현재 방문자 수 개수 갱신
    visitor_count[current_sum] += 1

# 가장 큰 key 값 (최대 방문자 수) 찾기
max_visitors = max(visitor_count.keys())

# 결과 출력
if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(visitor_count[max_visitors])  # 해당 방문자 수가 나온 기간 개수 출력