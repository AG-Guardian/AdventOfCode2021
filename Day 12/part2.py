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
    duplicates = []

    def depth_first_search(map: dict, cave: str, special_cave: str, visited: list):
        visited.append(cave)
        for connected in map[cave]:
            if connected not in visited or connected.isupper():
                depth_first_search(map, connected, special_cave, visited.copy())
            elif connected == special_cave and visited.count(special_cave) < 2:
                depth_first_search(map, connected, special_cave, visited.copy())
        if cave == 'end' and visited not in duplicates:
            pathList.append(visited)
            if visited.count(special_cave) < 2:
                duplicates.append(visited)

    small_caves = list(filter(lambda cave: cave.islower() and not cave == 'start' and not cave == 'end', list(map.keys())))
    paths = 0

    for small_cave in small_caves:
        depth_first_search(map, 'start', small_cave, [])
        paths += len(pathList)
        pathList = []

    return paths


with open('in.txt', 'r') as file:
    map = build_graph(file.read().splitlines())

print(find_paths(map))
