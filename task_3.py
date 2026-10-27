
import heapq


def dijkstra(graph, start):
    # Початкові відстані до всіх вершин
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    # Бінарна купа: (відстань, вершина)
    priority_queue = [(0, start)]

    # Зберігаємо попередні вершини для відновлення шляху
    previous = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            if weight < 0:
                raise ValueError("Вага ребра не може бути від'ємною")

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances, previous


def restore_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path


# Неорієнтований зважений граф
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 5)],
    "C": [("A", 2), ("D", 1), ("E", 8)],
    "D": [("B", 5), ("C", 1), ("E", 3)],
    "E": [("C", 8), ("D", 3)]
}

start_vertex = "A"

distances, previous = dijkstra(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")

for vertex in graph:
    path = restore_path(previous, start_vertex, vertex)

    print(
        f"До {vertex}: "
        f"відстань = {distances[vertex]}, "
        f"шлях = {' -> '.join(path)}"
    )
