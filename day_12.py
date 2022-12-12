# -*- coding: utf-8 -*-
import utils

input = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

input = utils.get_input(12)

input = utils.get_multiline_str(input)

input2 = []
for line in input:
    input2.append([*line])
input = input2

rows = len(input)
cols = len(input[0])


def first():
    graph = {}
    start = ''
    end = ''
    for i in range(0, rows):
        for j in range(0, cols):
            if input[i][j] == 'S':
                start = '{}-{}'.format(i, j)
                input[i][j] = 'a'
            elif input[i][j] == 'E':
                end = '{}-{}'.format(i, j)
                input[i][j] = 'z'

    for i in range(0, rows):
        for j in range(0, cols):
            neighbours = []
            if i > 0 and ord(input[i-1][j]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i - 1, j))
            if i < rows - 1 and ord(input[i + 1][j]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i + 1, j))
            if j > 0 and ord(input[i][j - 1]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i, j - 1))
            if j < cols - 1 and ord(input[i][j + 1]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i, j + 1))

            graph['{}-{}'.format(i, j)] = neighbours

    print('Start: ', start)
    print('End: ', end)
    # path = BFS_SP(graph, start, end)
    path = shortest_path(graph, start, end)

    # for k, v in graph.items():
    #     print('{}: {}'.format(k, v))
    print(*path)
    return len(path) - 1


def second():
    graph = {}
    starts = []
    end = ''
    for i in range(0, rows):
        for j in range(0, cols):
            if input[i][j] == 'S' or input[i][j] == 'a':
                starts.append('{}-{}'.format(i, j))
                input[i][j] = 'a'
            elif input[i][j] == 'E':
                end = '{}-{}'.format(i, j)
                input[i][j] = 'z'

    for i in range(0, rows):
        for j in range(0, cols):
            neighbours = []
            if i > 0 and ord(input[i-1][j]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i - 1, j))
            if i < rows - 1 and ord(input[i + 1][j]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i + 1, j))
            if j > 0 and ord(input[i][j - 1]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i, j - 1))
            if j < cols - 1 and ord(input[i][j + 1]) - ord(input[i][j]) <= 1:
                neighbours.append('{}-{}'.format(i, j + 1))

            graph['{}-{}'.format(i, j)] = neighbours

    shortest = [0]*1000
    for start in starts:
        path = shortest_path(graph, start, end)
        if path and len(path) < len(shortest):
            shortest = path

    return len(shortest) - 1


# Credit: https://onestepcode.com/graph-shortest-path-python/
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


# Credit: https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return None

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return new_path
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting path doesn't exist :(")
    return None


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
