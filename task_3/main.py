"""Module contains function for finding the shortest path in a graph using Dijkstra's algorithm."""

import heapq


def dijkstra(graph, start):
    """Function for finding the shortest path in a graph using Dijkstra's algorithm."""

    # Ініціалізація відстаней
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    # Ініціалізація бінарної купи
    path_tracker = [(0, start)]  # (відстань, вершина)

    print(f"Початкові відстані: {distances}")
    print(f"Стартова вершина: {start}\n")

    while path_tracker:
        current_distance, current_vertex = heapq.heappop(path_tracker)
        print(f"Вийняли вершину '{current_vertex}' з відстанню {current_distance} з купи")

        # Якщо поточна відстань більше ніж збережена, пропускаємо
        if current_distance > distances[current_vertex]:
            print(f"Відстань {current_distance} більше збереженої {distances[current_vertex]}. Пропускаємо.\n")
            continue

        # Оновлюємо відстані до сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            print(f"Розглядаємо сусіда '{neighbor}' з вагою ребра {weight}. Загальна відстань: {distance}")

            # Якщо знайдено коротший шлях, оновлюємо
            if distance < distances[neighbor]:
                print(f"Знайдено коротший шлях до '{neighbor}': {distance} (було {distances[neighbor]})")
                distances[neighbor] = distance
                heapq.heappush(path_tracker, (distance, neighbor))
                print(f"Додаємо '{neighbor}' з відстанню {distance} до купи\n")
            else:
                print(f"Відстань {distance} більше збереженої {distances[neighbor]}. Пропускаємо.\n")

        print(f"Поточні відстані: {distances}\n")

    return distances


def main():
    """Main function for testing the dijkstra function."""

    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4},
    }

    # Виклик функції для вершини A
    distances = dijkstra(graph, "B")
    print("Найкоротші відстані від вершини B:", distances)


if __name__ == "__main__":
    main()
