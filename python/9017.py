# 9017 

'''
입력
입력 데이터는 표준입력을 사용한다. 
입력은 T 개의 테스트 케이스로 주어진다. 
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 나타내는 정수 T 가 주어진다. 
두 번째 줄부터는 두 줄에 하나의 테스트 케이스에 해당하는 데이터가 주어진다. 
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (6 ≤ N ≤ 1,000)이 주어진다. 
두 번째 줄에는 팀 번호를 나타내는 N 개의 정수 t1, t2, …, tN 이 공백을 사이에 두고 주어진다. 
각 팀은 1 과 M(1 ≤ M ≤ 200)사이의 정수로 표현된다.

출력
출력은 표준출력을 사용한다. 
하나의 테스트 케이스에 대한 우승팀의 번호를 한 줄에 출력한다. 
'''

'''
한 팀은 여섯 명의 선수로 구성되며, 팀 점수는 상위 네 명의 주자의 점수를 합하여 계산
결승점을 통과한 순서대로 점수를 받는다
이 점수를 더하여 가장 낮은 점수를 얻는 팀이 우승을 하게 된다. 
여섯 명의 주자가 참가하지 못한 팀은 점수 계산에서 제외된다. 
동점의 경우에는 다섯 번째 주자가 가장 빨리 들어온 팀이 우승하게 된다.
'''

import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    team_num = list(map(int, input().split()))
    team_count = defaultdict(int)
    for num in team_num :
        team_count[num] += 1
    team_num = [ x for x in team_num if team_count[x] == 6 ]

    num_dict = defaultdict(list)
    
    # print(f'team_num : {team_num}')
    for idx, num in enumerate(team_num):
        num_dict[num].append(idx+1)
    # print(num_dict)
    sort_reslut = sorted(num_dict.keys(), key=lambda x:(sum(num_dict[x][:4]),num_dict[x][4]))
    print(sort_reslut[0])