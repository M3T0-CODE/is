import heapq

class Node:
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def ucs(start, goal, neighbors):
    frontier = []
    explored = set()
    heapq.heappush(frontier, Node(start, None, 0))

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        if current_node.state not in explored:
            explored.add(current_node.state)
            for neighbor, cost in neighbors(current_node.state):
                if neighbor not in explored:
                    heapq.heappush(frontier, Node(neighbor, current_node, current_node.cost + cost))

    return None

def neighbors(state):

    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)]
    }
    return graph.get(state, [])

start_state = "A"
goal_state = "D"

path = ucs(start_state, goal_state, neighbors)

if path:
    print("Path found:", path)
else:
    print("No path found")
