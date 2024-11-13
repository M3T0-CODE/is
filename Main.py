from queue import PriorityQueue


def GBFS(graph, start, goal, heuristic):
    global current
    front = PriorityQueue()
    front.put((heuristic[start], start))
    curr = {}
    curr[start] = None

    while not front.empty():
        _, current = front.get()
        if current == goal:
            break
        for neighbor in graph[current]:
            if neighbor not in curr:
                front.put((heuristic[neighbor], neighbor))
                curr[neighbor] = current

    path = []
    while current is not None:
        path.append(current)
        current = curr[current]
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
path = GBFS(graph, start, goal, heuristic)
print("Path from start to goal:", path)
