import timeit
import matplotlib.pyplot as plt
from typing import Dict, Optional, List, Tuple
from collections import deque


class TreeNode:
    """
    Класс для представления узла бинарного дерева.

    Атрибуты:
        value (int): Значение узла.
        left (Optional[TreeNode]): Левый потомок.
        right (Optional[TreeNode]): Правый потомок.
    """

    def __init__(self, value: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right


def build_tree_recursive(height: int) -> Optional[TreeNode]:
    """
    Рекурсивно строит бинарное дерево заданной высоты.

    Дерево строится с корневым значением 3. Левый потомок вычисляется как root + 2,
    правый - как root * 3. Высота определяет максимальную глубину дерева.

    Параметры:
        height (int): Высота дерева (целое положительное число).
    """

    if height <= 0:
        return None
    root_val = 3

    def _build(current_height: int, current_val: int) -> TreeNode:
        node = TreeNode(current_val)
        if current_height > 1:
            node.left = _build(current_height - 1, current_val + 2)
            node.right = _build(current_height - 1, current_val * 3)
        return node

    return _build(height, root_val)


def build_tree_iterative(height: int) -> Optional[TreeNode]:
    """
    Итеративно строит бинарное дерево заданной высоты с использованием очереди.

    Дерево строится с корневым значением 3. Левый потомок вычисляется как root + 2,
    правый - как root * 3. Высота определяет максимальную глубину дерева.

    Параметры:
        height (int): Высота дерева (целое положительное число).
    """
    if height <= 0:
        return None
    root_val = 3
    root = TreeNode(root_val)
    queue = deque([(root, 1)])  # (узел, текущая высота)

    while queue:
        node, current_height = queue.popleft()
        if current_height < height:
            node.left = TreeNode(node.value + 2)
            node.right = TreeNode(node.value * 3)
            queue.append((node.left, current_height + 1))
            queue.append((node.right, current_height + 1))

    return root


def benchmark_trees() -> Tuple[List[int], List[float], List[float]]:
    """
    Проводит бенчмарк рекурсивной и итеративной реализаций построения дерева.

    Измеряет среднее время выполнения для высот от 1 до 10 с использованием timeit.

    Возвращает:
        Tuple[List[int], List[float], List[float]]:
            - Список высот.
            - Средние времена для рекурсивной реализации.
            - Средние времена для итеративной реализации.
    """
    heights = list(range(1, 11))
    num_runs = 100
    recursive_times = []
    iterative_times = []

    for h in heights:
        recursive_time = timeit.timeit(
            stmt=f"build_tree_recursive({h})",
            setup="from __main__ import build_tree_recursive",
            number=num_runs
        ) / num_runs
        recursive_times.append(recursive_time)

        iterative_time = timeit.timeit(
            stmt=f"build_tree_iterative({h})",
            setup="from __main__ import build_tree_iterative",
            number=num_runs
        ) / num_runs
        iterative_times.append(iterative_time)

    return heights, recursive_times, iterative_times


def plot_results(heights: List[int], recursive_times: List[float], iterative_times: List[float]) -> None:
    """
    Строит график зависимости времени построения дерева от высоты.

    Параметры:
        heights (List[int]): Список высот дерева.
        recursive_times (List[float]): Средние времена для рекурсивной реализации.
        iterative_times (List[float]): Средние времена для итеративной реализации.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(heights, recursive_times, label='Рекурсивная', marker='o', color='red')
    plt.plot(heights, iterative_times, label='Итеративная', marker='s', color='blue')
    plt.xlabel('Высота дерева')
    plt.ylabel('Время построения (сек)')
    plt.title('Сравнение времени построения дерева')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    """
    Основная функция скрипта.

    Проводит бенчмарк, выводит результаты и строит график.
    """
    heights, recursive_times, iterative_times = benchmark_trees()

    print("Результаты бенчмарка:")
    print("Высота\tРекурсивная (сек)\tИтеративная (сек)")
    for h, rec, it in zip(heights, recursive_times, iterative_times):
        print(f"{h}\t{rec:.8f}\t\t{it:.8f}")

    print("\nВыводы:")
    print("- Рекурсивная реализация проста, но для больших высот может вызвать RecursionError и иметь overhead стека.")
    print("- Итеративная реализация эффективнее для глубоких деревьев, использует очередь для обхода уровней.")
    print("- В целом, итеративный подход предпочтительнее для предотвращения проблем с рекурсией.")

    plot_results(heights, recursive_times, iterative_times)