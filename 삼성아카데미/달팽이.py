T = int(input())  # 테스트 케이스 개수

for t in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]  # N x N 0 배열 생성

    # 우, 하, 좌, 상 순서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, 0       # 시작 좌표
    dir_idx = 0       # 방향 인덱스
    num = 1           # 채울 숫자

    while num <= N*N:
        snail[x][y] = num
        num += 1

        # 다음 좌표 계산
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]

        # 범위 벗어나거나 이미 채워진 경우 방향 전환
        if nx < 0 or nx >= N or ny < 0 or ny >= N or snail[nx][ny] != 0:
            dir_idx = (dir_idx + 1) % 4
            nx = x + dx[dir_idx]
            ny = y + dy[dir_idx]

        x, y = nx, ny

    # 출력
    print(f"#{t}")
    for row in snail:
        print(" ".join(map(str, row)))
