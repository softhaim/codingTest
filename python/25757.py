# 25757

'''
입력
첫 번째 줄에는 사람들이 임스와 같이 플레이하기를 신청한 횟수 
N과 같이 플레이할 게임의 종류가 주어진다. 
(1 <= N <= 100,000)

두 번째 줄부터 
$N$개의 줄에는 같이 플레이하고자 하는 사람들의 이름이 문자열로 주어진다. 
(1 <= 문자열 길이 <= 20)

사람들의 이름은 숫자 또는 영문 대소문자로 구성되어 있다.

출력
임스가 최대로 몇 번이나 게임을 플레이할 수 있는지 구하시오.

'''

import sys 

input = sys.stdin.readline

n , game = input().split()

name_set = set()

for i in range(int(n)): 
    name = input()
    name_set.add(name)

if game == 'Y':
    print(len(name_set))
elif game == 'F':
    print(len(name_set)//2)
elif game == 'O':
    print(len(name_set)//3)