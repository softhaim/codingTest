# 1244

'''
남학생은 스위치 번호가 자기가 받은 수의 배수이면, 
그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. 
<그림 1>과 같은 상태에서 남학생이 3을 받았다면, 
이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 
가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
'''

'''
입력
첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다. 
둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 
꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다. 
셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다. 
넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 
남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다.
학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.

출력
스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다. 
예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다. 
켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.

'''

import sys

input = sys.stdin.readline

num_switch = int(input())

switch_status = list(map(int, input().split()))

num_student = int(input())

for i in range(num_student):
    student_gender, given_number = map(int, input().split())
    
    if student_gender == 1:
        for _ in range(given_number-1, num_switch, given_number):
            if switch_status[_]:
                switch_status[_] = 0
            else:
                switch_status[_] = 1
    else:
        search_idx_num = min(num_switch-given_number, given_number-1)
        change_idx_point = list()
        
        for _ in range(1, search_idx_num+1):
            if switch_status[given_number-1-_] == switch_status[given_number-1+_]:
                change_idx_point.clear()
                change_idx_point.append(given_number-1-_)
                change_idx_point.append(given_number-1+_)
            else:
                break
        if 0 == len(change_idx_point):
            switch_status[given_number-1] = 0 if switch_status[given_number-1] else 1              

        else:
            for idx in range(change_idx_point[0], change_idx_point[1]+1):
                if switch_status[idx]:
                    switch_status[idx] = 0
                else:
                    switch_status[idx] = 1
    
for i in range(1,num_switch+1):
    print(switch_status[i-1], end = " ")
    if not i == 1 and i % 20 == 0:
        print()