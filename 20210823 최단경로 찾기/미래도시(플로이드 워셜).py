INF = (1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드의 개수 및 간선의 개수를 입력 받기
n, m = map(int, input().split())

# 2차원 리스트를 만들고, 무한으로 초기화
graph = [[INF] * (10) for _ in range(10)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, 10):
    for b in range(1, 10):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = 1  # 도로가 양방향이고 거리가 1이라고 했기에
    graph[b][a] = 1

# 거쳐 갈 노드 k와 최종 목적지 노드x를 입력받기
k, x = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for j in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][j] + graph[j][b])

# 수행된 결과를 출력
distance = graph[1][k] + [k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달할  수 있다면, 최단 거리를 출력
else:
    print(distance)
