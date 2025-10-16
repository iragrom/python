from collections import deque
from typing import Dict, Callable, Optional, Union

def gen_bin_tree(
    height: Optional[int] = None,
    root: Optional[Union[int, float]] = None,
    left_branch: Optional[Callable[[Union[int, float]], Union[int, float]]] = None,
    right_branch: Optional[Callable[[Union[int, float]], Union[int, float]]] = None
) -> Dict[Union[int, float], list]:

    if type(root) != int or type(
            height) != int:  # исправляем ошибки тестов 1-5, в которых ошибка возникает из-за нецелочисленных типов переменных root и height
        return 'не верный тип данных'

    if height <= 0:  # исправляем ошибку теста 6-7, в котором ошибка возникает из-за не верного количества переменных в массиве
        return 'не верное количество элементов'

    """
    Генерирует бинарное дерево нерекурсивным способом и возвращает его в виде словаря.

    Дерево строится уровень за уровнем с использованием очереди. Каждый узел в словаре
    является ключом со значением в виде списка [левый_потомок, правый_потомок], где None
    указывает на отсутствие потомка.

    Аргументы:
        height (Optional[int]): Высота дерева (число уровней, включая корень).
        root (Optional[Union[int, float]]): Значение корневого узла.
        left_branch (Optional[Callable[[Union[int, float]], Union[int, float]]]):
            Функция для вычисления значения левого потомка от значения родителя.
        right_branch (Optional[Callable[[Union[int, float]], Union[int, float]]]):
            Функция для вычисления значения правого потомка от значения родителя.

    """
    # Устанавливаем значения по умолчанию
    if height is None:
        height = 5
    if root is None:
        root = 4
    if left_branch is None:
        left_branch = lambda r: r + 2
    if right_branch is None:
        right_branch = lambda r: r * 3

    if height < 1:
        raise ValueError("Высота должна быть не менее 1")

    tree: Dict[Union[int, float], list] = {}
    queue = deque([(root, 0)])  # (значение_узла, текущий_уровень)

    while queue:
        node, level = queue.popleft()
        if level >= height:
            continue  # Нет потомков за пределами высоты
        left = left_branch(node) if level + 1 < height else None
        right = right_branch(node) if level + 1 < height else None
        tree[node] = [left, right]
        if left is not None:
            queue.append((left, level + 1))
        if right is not None:
            queue.append((right, level + 1))

    return tree

# Вызов функции с указанными параметрами: root=5, height=6, left_branch=lambda r: r**2, right_branch=lambda r: r-2
if __name__ == "__main__":
    tree_dict = gen_bin_tree()
    print(tree_dict)
