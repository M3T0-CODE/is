from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 5), ('G', 1)],
    'D': [],
    'E': [('H', 1)],
    'F': [],
    'G': [('H', 2)],
    'H': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 7,
    'E': 2,
    'F': 6,
    'G': 1,
    'H': 0
}

def greedy_best_first_search(start, goal):
    open_list = PriorityQueue()
    open_list.put((heuristic[start], start))
    came_from = {start: None}

    while not open_list.empty():
        _, current = open_list.get()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor, _ in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                open_list.put((heuristic[neighbor], neighbor))

    return None

start_node = 'A'
goal_node = 'H'
path = greedy_best_first_search(start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", path)
