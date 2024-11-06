import heapq

class UCS:
    def __init__(self):
        self.priority_queue = []
        self.explored = set()

    def uniform_cost_search(self, start, goal, graph):
        heapq.heappush(self.priority_queue, (0, start, [start]))

        while self.priority_queue:
            cost, node, path = heapq.heappop(self.priority_queue)

            if node == goal:
                return path, cost

            if node in self.explored:
                continue

            self.explored.add(node)

            for neighbor, edge_cost in graph.get(node, []):
                if neighbor not in self.explored:
                    total_cost = cost + edge_cost
                    heapq.heappush(self.priority_queue, (total_cost, neighbor, path + [neighbor]))

        return None

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2), ('G', 1)],
        'E': [('B', 5), ('G', 2)],
        'F': [('C', 3), ('G', 1)],
        'G': [('D', 1), ('E', 2), ('F', 1)]
    }

    ucs = UCS()
    start_node = 'A'
    goal_node = 'G'
    result = ucs.uniform_cost_search(start_node, goal_node, graph)

    if result:
        path, total_cost = result
        print(f"Path from {start_node} to {goal_node}: {path} with total cost: {total_cost}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")
