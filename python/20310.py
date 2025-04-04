# 20310

import sys

input = sys.stdin.readline

'''
갑자기 심술이 난 타노스는 
S를 구성하는 문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열 
S'를 만들고자 한다. 
S'로 가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.

제한
S의 길이는 
2 이상 500 이하이다.
S는 짝수 개의 0과 짝수 개의 1로 이루어져 있다.

S의 길이는 4의 배수이다.
S의 홀수 번째 문자는 1, 짝수 번째 문자는 0이다.
'''

S = input().strip()

# 0과 1의 개수 세기
count_0 = S.count('0')  # 전체 0의 개수
count_1 = S.count('1')  # 전체 1의 개수

remove_0 = count_0 // 2  # 제거할 0의 개수
remove_1 = count_1 // 2  # 제거할 1의 개수

# 1을 왼쪽부터 제거
new_S = []
removed_1 = 0
for c in S:
    if c == '1' and removed_1 < remove_1:
        removed_1 += 1
    else:
        new_S.append(c)

# 0을 오른쪽부터 제거
result = []
removed_0 = 0
for c in reversed(new_S):  # 뒤에서부터 순회
    if c == '0' and removed_0 < remove_0:
        removed_0 += 1
    else:
        result.append(c)

# 결과 출력 (뒤집어서 원래 순서대로 출력)
print(''.join(result[::-1]))
