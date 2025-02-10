# 2607

'''
입력으로 여러 개의 서로 다른 단어가 주어질 때, 첫 번째 단어와 
비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.
'''

import sys 

input = sys.stdin.readline

'''
입력
첫째 줄에는 단어의 개수가 주어지고 둘째 줄부터는 한 줄에 하나씩 단어가 주어진다. 
모든 단어는 영문 알파벳 대문자로 이루어져 있다. 단어의 개수는 100개 이하이며, 
각 단어의 길이는 10 이하이다.

출력
입력으로 주어진 첫 번째 단어와 비슷한 단어가 몇 개인지 첫째 줄에 출력한다.
'''

N = int(input())
target = list(input().strip()) # 비교 대상 단어(첫 단어)
answer = 0

for _ in range(N-1):
    compare = target[:] 
    word = input().strip() # 새로운 단어
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else: # 차이 나는 것을 카운트
            cnt += 1
    # 1개 이하로 차이나는 것은 교체 및 추가, 삭제 하면 그만.
    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
