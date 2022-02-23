# DFS 메서드 정의
def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],  # 1부터 시작하기 위해 0인덱스는 빈리스트
    [2, 3, 8],  # 1번과 인접한 노드
    [1, 7],  # 2번과 인접한 노드
    [1, 4, 5],  # 3번과 인접한 노드
    [3, 5],  # 4번과 인접한 노드
    [3, 4],  # 5번과 인접한 노드
    [7],  # 6번과 인접한 노드
    [2, 6, 8],  # 7번과 인접한 노드
    [1, 7]  # 8번과 인접한 노드
]
# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9  # 8번까지 노드밖에없지만 0번을 안쓰기 때문에 9열로 초기화

# 정의된 DFS 함수 호출
dfs(1)
