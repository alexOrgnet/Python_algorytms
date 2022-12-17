"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без
петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First
Search). Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход
число вершин.
"""


# Генерация невзвешенного ориентированного графа без петель по количеству его вершин
def gen_graph(num_vertex: int):
    graph = {}

    for i in range(num_vertex):
        graph.setdefault(i)
        if i < 2 * num_vertex // 3:
            graph[i] = tuple(
                j for j in range(num_vertex) if j != i and (graph[j].count(i) == 0 if j in graph.keys() else True)
            )
        else:
            graph[i] = tuple(
                j for j in range(num_vertex) if j != i and (graph[j].count(i - 1) == 0 if j in graph.keys() else True)
            )
    return graph

# Алгоритм обхода графа в его глубину
# Находится первый попавшийся путь до целевой вершины или возвращается False
def deep_search(graph, start, end, is_visited=None, path=None):
    # Создание переменных в начале рекурсии
    if is_visited is None:
        is_visited = [False] * len(graph)
    if path is None:
        path = [start]

    # Проверка условий возврата
    if start == end:
        return True, path
    elif is_visited[start]:
        path.pop()
        return False, path

    is_visited[start] = True

    # Перебор соседних вершин
    for neigbours in graph[start]:
        if not is_visited[neigbours]:
            path.append(neigbours)
            return deep_search(graph, neigbours, end, is_visited, path)


numb_graphs = int(input("Введите общее число графов = "))
first_graph = int(input("Введите первый граф = "))
last_graph = int(input("Введите последний граф = "))

g = gen_graph(numb_graphs)

print(f"Исходный граф: {numb_graphs}")
print(f"Стартовый граф: {first_graph}")
print(f"Финальный граф: {last_graph}")

for i, k in g.items():
    print(i, ':', *k)

print('*' * 50)
print(deep_search(g, first_graph, last_graph))
