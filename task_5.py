
import uuid
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_tree():
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)
    return root


def dfs(root):
    """Обхід у глибину за допомогою стека."""
    if root is None:
        return []

    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return visited


def bfs(root):
    """Обхід у ширину за допомогою черги."""
    if root is None:
        return []

    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return visited


def add_edges(graph, root):
    """Додає вузли та ребра без рекурсії."""
    positions = {root.id: (0, 0)}
    stack = [(root, 0, 0, 1)]

    while stack:
        node, x, y, layer = stack.pop()
        graph.add_node(node.id, label=node.val)

        if node.left:
            left_x = x - 1 / 2 ** layer
            positions[node.left.id] = (left_x, y - 1)
            graph.add_edge(node.id, node.left.id)
            stack.append(
                (node.left, left_x, y - 1, layer + 1)
            )

        if node.right:
            right_x = x + 1 / 2 ** layer
            positions[node.right.id] = (right_x, y - 1)
            graph.add_edge(node.id, node.right.id)
            stack.append(
                (node.right, right_x, y - 1, layer + 1)
            )

    return positions



def visualize_traversal(root, order, title):
    graph = nx.DiGraph()
    positions = add_edges(graph, root)
    labels = nx.get_node_attributes(graph, "label")

    total = len(order)
    visited_colors = {}

    fig, ax = plt.subplots(figsize=(10, 6))

    for index, node in enumerate(order):
        intensity = index / max(total - 1, 1)

        red = int(20 + 170 * intensity)
        green = int(50 + 175 * intensity)
        blue = int(110 + 130 * intensity)

        node.color = f"#{red:02X}{green:02X}{blue:02X}"
        visited_colors[node.id] = node.color

        colors = [
            visited_colors.get(node_id, "#E0E0E0")
            for node_id in graph.nodes()
        ]

        ax.clear()

        nx.draw(
            graph,
            pos=positions,
            labels=labels,
            node_color=colors,
            node_size=2300,
            font_size=12,
            font_weight="bold",
            arrows=False,
            ax=ax
        )

        ax.set_title(
            f"{title}\n"
            f"Крок {index + 1}/{total}: "
            f"відвідано вузол {node.val}"
        )

        plt.pause(1.0)

    plt.show()



def main():
    root = build_tree()

    dfs_order = dfs(root)
    print("DFS:", [node.val for node in dfs_order])

    visualize_traversal(
        root,
        dfs_order,
        "DFS - Обхід дерева в глибину"
    )

    bfs_order = bfs(root)
    print("BFS:", [node.val for node in bfs_order])

    visualize_traversal(
        root,
        bfs_order,
        "BFS - Обхід дерева в ширину"
    )


if __name__ == "__main__":
    main()
