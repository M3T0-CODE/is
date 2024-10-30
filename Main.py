def dfs(graph, start, visited):
    if visited[start]:
        return

    visited[start] = True
    print(start, end=' ')

    for neighbor in graph[start]:
        dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

visited = [False] * len(graph)
print("DFS Traversal:")
dfs(graph, 0, visited)

print("\n")

print("BFS Traversal:")
bfs(graph, 0)
