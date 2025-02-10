# 17484

import sys

# 표준 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N: 행의 개수, M: 열의 개수 입력 받기
N, M = map(int, input().split())

# 행렬 정보를 저장할 리스트
map_mat = list()

# N개의 행을 입력받아 리스트로 저장
for i in range(N):
    map_mat.append(list(map(int, input().split())))

# 가능한 이동 방향 (좌, 정면, 우)
direction = [-1, 0, 1]

def dfs(col, row, d, low, answer):
    """
    깊이 우선 탐색(DFS)을 이용하여 최소 연료 소비량을 구하는 함수

    col: 현재 탐색 중인 행의 위치
    row: 현재 탐색 중인 열의 위치
    d: 이전에 이동했던 방향 (-1: 왼쪽, 0: 직진, 1: 오른쪽)
    low: 현재까지 발견된 최소 연료 소비량
    answer: 현재 경로에서의 총 연료 소비량
    """

    # 마지막 행(N-1)에 도달하면 현재까지의 연료 소비량 중 최소값 반환
    if col == N - 1:
        return min(low, answer)

    # 다음 행으로 이동하면서 가능한 방향 탐색
    for i in direction:
        if i != d:  # 같은 방향으로 연속 이동 불가능한 조건
            if 0 <= col + 1 < N and 0 <= row + i < M:  # 유효한 범위 내에 있을 경우 이동
                low = dfs(col + 1, row + i, i, low, answer + map_mat[col + 1][row + i])

    return low

# 초기 최소 연료 소비량을 큰 값으로 설정 (sys.maxsize 활용)
low = int(sys.maxsize)

# 첫 번째 행에서 모든 열을 출발점으로 설정하여 DFS 실행
for i in range(M):
    low = min(dfs(0, i, 2, low, map_mat[0][i]), low)  # 2는 초기값으로 의미 없음 (어떤 방향도 아닐 때)

# 최소 연료 소비량 출력
print(low)
