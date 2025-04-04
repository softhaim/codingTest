#19367 if 문 좀 대신 써줘

'''
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

status_dic = [input().split() for i in range(N)]
status_dic.sort(key=lambda x: int(x[1])) # 오름차순 정렬

nums = [int(input().strip()) for i in range(M)]

# 시간 초과나서 이진 탐색 해야함 

for num in nums:
    left = 0
    right = N
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if int(status_dic[mid][1]) >= num:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    print(status_dic[result][0])
            

