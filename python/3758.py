# 3758
'''
입력

입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 
입력의 첫 번째 줄에는 테스트 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터의 첫 번째 줄에는 팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 
로그 엔트리의 개수 m을 나타내는 4 개의 정수가 주어진다. 
여기서, 3 ≤ n, k ≤ 100, 1 ≤ t ≤ n, 3 ≤ m ≤ 10,000이다. 
그 다음 m개의 줄에는 각 풀이에 대한 정보가 제출되는 순서대로 주어진다. 
각 줄에는 팀 ID i, 문제 번호 j, 획득한 점수 s를 나타내는 세 개의 정수가 주어진다. 
여기서 1 ≤ i ≤ n, 1 ≤ j ≤ k, 0 ≤ s ≤ 100이다. 


출력

출력은 표준출력을 사용한다. 
주어진 각 테스트 데이터에 대해 당신 팀의 순위를 한 줄에 출력하여야 한다
'''
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    
    scores = [[0] * (k + 1) for _ in range(n + 1)]
    last_submit = [0] * (n + 1)  # 마지막 제출 시간 저장
    submit_count = [0] * (n + 1)  # 제출 횟수 저장
    
    for time in range(m):
        i, j, s = map(int, input().split())
        scores[i][j] = max(scores[i][j], s)  # 해당 문제의 최고 점수만 반영
        last_submit[i] = time  # 마지막 제출 시간 업데이트
        submit_count[i] += 1  # 제출 횟수 증가

    ranking = []

    for i in range(1, n + 1):
        total_score = sum(scores[i][1:])  # 1번 문제부터 k번 문제까지 합산
        ranking.append((total_score, submit_count[i], last_submit[i], i))

    # 정렬 기준:
    # 1. 총점 내림차순
    # 2. 제출 횟수 오름차순
    # 3. 마지막 제출 시간 오름차순
    ranking.sort(key=lambda x: (-x[0], x[1], x[2]))

    # t팀의 순위 찾기
    for rank, (_, _, _, team_id) in enumerate(ranking, start=1):
        if team_id == t:
            print(rank)
            break
