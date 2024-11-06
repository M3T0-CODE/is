import heapq


def uniform_cost_search(goal, start):
    global graph, cost
    answer = [float('inf')] * len(goal)
    queue = [(0, start)]
    visited = set()
    count = 0

    while queue:
        queue.sort()
        current_cost, current_node = queue.pop(0)

        if current_node in goal:
            index = goal.index(current_node)
            if answer[index] == float('inf'):
                count += 1
            answer[index] = min(answer[index], current_cost)

            if count == len(goal):
                return answer

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                new_cost = current_cost + cost.get((current_node, neighbor), float('inf'))
                heapq.heappush(queue, (new_cost, neighbor))

    return answer


if __name__ == '__main__':
    graph = [[] for _ in range(8)]
    cost = {}

    graph[0] = [1, 3]
    graph[3] = [1, 6, 4]
    graph[1] = [6]
    graph[4] = [2, 5]
    graph[2] = [1]
    graph[5] = [2, 6]
    graph[6] = [4]

    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    goal = [6]
    answer = uniform_cost_search(goal, 0)
    print("Minimum cost from 0 to 6 is =", answer[0])
