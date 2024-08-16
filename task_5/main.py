import sys
import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def build_tree_from_heap(heap):
    """Build a binary tree from a heap represented as a list."""
    if not heap:
        return None

    nodes = [Node(key) for key in heap]

    for i, node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, ax=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    if ax is None:
        plt.figure(figsize=(8, 5))
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
            node_color=colors,
        )
        plt.show()
    else:
        ax.clear()
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
            node_color=colors,
            ax=ax,
        )
        ax.text(
            0.5,
            1.05,
            "Press SPACE to draw the next frame",
            transform=ax.transAxes,
            ha="center",
            fontsize=12,
        )
        plt.draw()


def color_gradient(n):
    # Генерує градієнт кольорів від темного до світлого
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "custom_cmap", ["#00008B", "#CDD8E6"]
    )
    return [cmap(i / n) for i in range(n)]


def dfs(root):
    """Iterative DFS using a stack."""
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            # Спочатку додаємо правого нащадка, щоб лівий оброблявся першим
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return visited


def bfs(root):
    visited = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


def visualize_traversal(root, traversal_func, ax=None):
    nodes_visited = traversal_func(root)
    colors = color_gradient(len(nodes_visited))

    for idx, node in enumerate(nodes_visited):
        node.color = colors[idx]
        draw_tree(root, ax=ax)
        yield  # Pause after each step


def reset_colors(root):
    if root:
        root.color = "skyblue"
        reset_colors(root.left)
        reset_colors(root.right)


def engine(root, ax):
    scenarios = [
        (visualize_traversal(root, dfs, ax), "DFS"),
        (lambda: reset_colors(root), "Reset colors"),
        (visualize_traversal(root, bfs, ax), "BFS"),
    ]

    for scenario, name in scenarios:
        print(f"Running: {name}")
        if callable(scenario):
            scenario()  # Call reset_colors directly
            draw_tree(root, ax=ax)
            yield
        else:
            yield from scenario  # Use yield from to play the generator


def on_key_press(event, frames):
    if event.key == " ":
        try:
            next(frames)
        except StopIteration:
            print("Scenario completed")
            sys.exit(0)


def main():
    """Main function."""

    arr = [1, 4, 5, 6, 2, 6, 7, 10, 51, 41, 3]  # Несортований масив

    # Перетворюємо масив на мін-купу
    heapq.heapify(arr)

    # Будуємо дерево з купи
    root = build_tree_from_heap(arr)

    fig, ax = plt.subplots(figsize=(8, 5))
    draw_tree(root, ax=ax)

    # Ініціалізація графічного двигуна
    frames = engine(root, ax)
    fig.canvas.mpl_connect("key_press_event", lambda event: on_key_press(event, frames))
    plt.show()


if __name__ == "__main__":
    main()
