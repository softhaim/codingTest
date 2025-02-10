# 1515

'''
세준이는 수를 방금 전과 똑같이 쓰려고 한다. 하지만, N이 기억이 나지 않는다.

남은 수를 이어 붙인 수가 주어질 때, N의 최솟값을 구하는 프로그램을 작성하시오. 
아무것도 지우지 않을 수도 있다.

입력
첫째 줄에 지우고 남은 수를 한 줄로 이어 붙인 수가 주어진다. 이 수는 최대 3,000자리다.

출력
가능한 N 중에 최솟값을 출력한다.
'''

import sys 

input = sys.stdin.readline

N = input().strip()

idx = 0

while(True):
    idx +=1
    num = str(idx)
    while (len(num) > 0 and (len(N) > 0)):
        if num[0] == N[0]:
            N = N[1:]
        num = num[1:]
    if N == '':
        print(idx)
        break