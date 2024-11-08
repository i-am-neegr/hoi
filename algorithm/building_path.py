import json

from algorithm.dijkstra_algorithm import dijkstra

with open("data\\points_position.json") as file:
    points_position = json.load(file)


def building_path(start_point, end_point, time_path):
    response = dijkstra(start_point, end_point, time_path)

    with open("data\\piska.txt", "w") as file:
        file.write(response)


    answer_path = [[float(points_position[value]["lat"]), float(points_position[value]["lon"])] for value in response.split(".")]

    return answer_path, response
