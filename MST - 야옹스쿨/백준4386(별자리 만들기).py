import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    parent[a] = b


N = int(input())

parent = [i for i in range(N)]
graph = []
for i in range(N):
    a, b = map(float, input().split())
    graph.append((i, a, b))  # 별의 번호, x좌표, y좌표

graph2 = graph[:]
distance = []
for i in range(N):
    for j in range(i + 1, N):
        a, b = graph[i][0], graph[j][0]
        d = ((graph[i][1] - graph[j][1]) ** 2 + (graph[i][2] - graph[j][2]) ** 2) ** 0.5
        distance.append((a, b, d))

distance.sort(key=lambda x: x[2])

ans = 0
for i in distance:
    a, b, cost = i

    if find(a) != find(b):
        union_(a, b)
        ans += cost

print(f'{ans:.2f}')
