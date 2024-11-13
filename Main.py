def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = [(start, heuristic[start])]
    explored = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current, _ = frontier.pop(0)

        if current == goal:
            break

        explored.add(current)

        for neighbor in graph[current]:
            if neighbor not in explored and neighbor not in [node[0] for node in frontier]:
                frontier.append((neighbor, heuristic[neighbor]))
                came_from[neighbor] = current

    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 3, 'D': 5,
    'E': 2, 'F': 1, 'G': 0
}

start = 'A'
goal = 'G'
path = greedy_best_first_search(graph, start, goal, heuristic)
print("Path from start to goal:", path)
