# 2512

'''
모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 
그 이상인 예산요청에는 모두 상한액을 배정한다.
상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

전체 예산 485이고
4개 지방 예산 요청이 120 110 140 150 이라면
상한액 127 잡으면 120 110 127 127 배정하고 그 합 484로 가능한 최대 됨.

이진 탐색 문제인듯?
'''

import sys

input = sys.stdin.readline

# 입력 처리
N = int(input())  # 지방의 수
request_credit = list(map(int, input().split()))  # 예산 요청 리스트
total_money = int(input())  # 총 예산

# 이진 탐색을 위한 범위 설정
low, high = 0, max(request_credit)
result = 0  # 최적의 상한액 저장

while low <= high:
    mid = (low + high) // 2  # 현재 상한액 설정
    allocated_budget = sum(min(mid, i) for i in request_credit)  # 상한액 적용된 총 예산 계산

    if allocated_budget <= total_money:  # 예산이 허용 범위 내라면
        result = mid  # 상한액 갱신
        low = mid + 1  # 더 큰 상한액을 탐색
    else:
        high = mid - 1  # 예산 초과 시 상한액 낮춤

print(result)  # 가능한 최대 상한액 출력