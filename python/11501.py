import sys

input = sys.stdin.readline

T = int(input())

get_money = 0
max_num = 0

'''
더 미래의 날짜부터 거꾸로 주식의 가격을 탐색한다.
앞에서부터 탐색한다면 미래에 어떤 가격이 있을지 모르기 때문이다.
현재의 주식 가격이 현재 기록되어 있는 최대 가격보다 작다면 차익을 실현한다.
그렇지 않다면 현재 최대 가격 기록을 현재의 가격으로 갱신한다.
'''

for i in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    max_num = price[-1]
    for j in range(N-2, -1, -1):
        if price[j] < max_num:
            get_money += max_num - price[j]
        elif max_num < price[j]:
            max_num = price[j]
    
    print(get_money)
    get_money = 0