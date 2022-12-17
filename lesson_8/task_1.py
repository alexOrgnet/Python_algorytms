"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по
одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


def counter_handshakes(graph, is_double_handshake=True):
    counter = 0
    length = len(graph)
    is_visited = [False] * length

    for i in range(length):
        for j in range(length):
            if is_double_handshake:
                if graph[i][j] == 1:
                    counter += 1
            else:
                if graph[i][j] == 1 and not is_visited[j]:
                    counter += 1

        is_visited[i] = True
    return counter


# Решение с использованием матрицы смежности
friends = int(input(f"Сколько друзей встретилось на улице? "))
in_graph = [[0 if j == i else 1 for j in range(friends)] for i in range(friends)]

print("Граф")
print(*in_graph, sep="\n")
print()
print(f"Было {counter_handshakes(in_graph)} рукопожатий \n"
      f"(если учитывать двойные рукопожатия)")
print('-' * 50)
print(f"Было {counter_handshakes(in_graph, False)} рукопожатий\n"
      f"(если НЕ учитывать двойные рукопожатия)")
