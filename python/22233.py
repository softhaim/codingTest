# 22233 가희와 키워드

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keywords = set()

for i in range(N):
    keywords.add(input().strip())

for i in range(M):
    blog = input().strip().split(',')
    for keyword in blog:
        if keyword in keywords:
            keywords.remove(keyword)

    print(len(keywords))


