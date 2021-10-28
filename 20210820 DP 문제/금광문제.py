# 테스트 케이스 입력
t = int(input())

for _ in range(t):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp = []
    index = 0
    result = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):  # 열
        for i in range(n):  # 행
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            # 2번째 열부터 전 열에서 온 값 + 왼쪽위,왼쪽아래,왼쪽 중 가장 큰값을 더한다.
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
