# 1927

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    num = int(input())

    if num == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, num)
