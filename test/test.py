import json
import time

from collections import deque

'''d = 0 with open("data.txt", "r") as f:
    data = tuple(map(lambda x: x.split(), f.readlines()))'''

with open("../data/time_graph.json", "r") as f:
    time_graph = json.load(f)

with open("../data/dist_graph.json", "r") as f:
    dist_graph = json.load(f)

with open("../data/matrix_time_minimal_graph.json") as f:
    matrix_distance = json.load(f)


def address_processing(url: str) -> tuple:
    left_index, right_index = url.find("rtext="), url.rfind("&rtt=pd")

    lat_str, lon_str = url[left_index+6:right_index].split("~")

    lat_start, lon_start = lat_str.split("%2C")
    lat_end, lon_end = lon_str.split("%2C")

    return lat_start, lon_start, lat_end, lon_end


def append_path_json(v1, v2, time_, dist):
    if v1 in time_graph:
        time_graph[v1][v2] = time_
        dist_graph[v1][v2] = dist
    else:
        time_graph[v1] = {v2: time_}
        dist_graph[v1] = {v2: dist}

    if v2 in time_graph:
        time_graph[v2][v1] = time_
        dist_graph[v2][v1] = dist
    else:
        time_graph[v2] = {v1: time_}
        dist_graph[v2] = {v1: dist}


def create_matrix_distance():
    matrix_dist = {str(v): {str(w): 10 ** 9 for w in range(1, 27)} for v in range(1, 27)}

    for v1 in time_graph:
        for v2 in time_graph[v1]:
            if v1 == v2:
                matrix_dist[v1][v2] = 0
            else:
                matrix_dist[v1][v2] = time_graph[v1][v2]

    for v in matrix_dist:
        for a in matrix_dist:
            for b in matrix_dist:
                if matrix_dist[a][v] != 10**9 and matrix_dist[v][b] != 10**9:
                    if matrix_dist[a][b] > matrix_dist[a][v] + matrix_dist[v][b]:
                        matrix_dist[a][b] = matrix_dist[a][v] + matrix_dist[v][b]

    with open("../data/matrix_time_minimal_graph.json", "w") as file:
        json.dump(matrix_dist, file)


if __name__ == "__main__":
    d = {}

    with open("data.txt", "r") as f:
        data = tuple(map(lambda x: x.split(), f.readlines()))

    for v in data:
        a, b, url = v[0], v[1], v[4]

        print(a, b)

        lat1, lon1, lat2, lon2 = address_processing(url)

        if a in d:
            if d[a]["lat"] != lat1 or d[a]["lon"] != lon1:
                print(a, "Error a", d[a]["lat"], lat1, d[a]["lon"], lon1)

                break
        else:
            d[a] = {"lat": lat1, "lon": lon1}

        if b in d:
            if d[b]["lat"] != lat2 or d[b]["lon"] != lon2:
                print(b, "Error b", d[b]["lat"], lat2, d[b]["lon"], lon2)

                break
        else:
            d[b] = {"lat": lat2, "lon": lon2}

    with open("../data/points_position.json", "w") as file:
        json.dump(d, file)
