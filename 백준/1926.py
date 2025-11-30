# 1을 만났을 때 => 상,하,좌,우 재귀로 뻗어나가며 살피기, 0만나면 break, 끝나면 count +1

# 입력 읽기
n, m = map(int, input().split())   # n: 행수, m: 열수
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
