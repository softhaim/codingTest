# 8979

'''
1. 금메달 많은 나라
2. 금메달 같으면 은메달
3. 둘다 같으면 동메달

각 국가는 1부터 N 정수
두 나라가 금은동 같으면 등수 같음. 

각 순위는 자신보다 잘한 나라수 + 1

그래서 1번 국가 금메달 1
2번 3번 국가 은 1
4번 국가 동 1 이면

순위는 1등 1번 2등 2,3번 4등 4번 임.
'''

import sys

n, k = map(int, sys.stdin.readline().split())

score_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

score_list.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

#0부터 N-1 인덱스까지 medals[i][0], 즉 국가명을 확인하여 국가명이 'K'와 일치하는 인덱스를 찾아 idx에 저장한다.
idx = [score_list[i][0] for i in range(n)].index(k)

# 동점 국가 검사 -> 자기 일때도 인덱스니까 +1 해야함.
# 가장 상위에서 같은 등수를 기준으로 맞추는것.
for i in range(n):
    if score_list[idx][1:] == score_list[i][1:]:
        print(i+1)
        break