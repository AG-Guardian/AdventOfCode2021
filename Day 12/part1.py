def build_graph(lines: list):
    graph = {}
    for line in lines:
        node_a = line.split('-')[0]
        node_b = line.split('-')[1]
        if node_a not in graph.keys():
            graph[node_a] = [node_b]
        else:
            graph[node_a].append(node_b)
        if node_b not in graph.keys():
            graph[node_b] = [node_a]
        else:
            graph[node_b].append(node_a)
    return graph


def find_paths(map: dict):
    pathList = []

    def depth_first_search(map: dict, cave: str, visited: list):
        visited.append(cave)
        for connected in map[cave]:
            if connected not in visited or connected.isupper():
                depth_first_search(map, connected, visited.copy())
        if cave == 'end':
            pathList.append(visited)

    depth_first_search(map, 'start', [])
    return pathList


with open('in.txt', 'r') as file:
    map = build_graph(file.read().splitlines())

print(len(find_paths(map)))
