def bin_tree(height=4, root=3):

    if type (root) != int or type(height) != int:    # исправляем ошибки тестов 1-5, в которых ошибка возникает из-за нецелочисленных типов переменных root и height
        return 'не верный тип данных'

    if height <= 0:  # исправляем ошибку теста 6-7, в котором ошибка возникает из-за не верного количества переменных в массиве
        return 'не верное количество элементов'

    """
    Рекурсивная функция для создания бинарного дерева в виде вложенного словаря.
    Параметры:
    - height: высота дерева (по умолчанию 4)
    - root: значение корня (по умолчанию 3)
    Левый потомок: root + 2
    Правый потомок: root * 3
    """
    if height == 0:
        return None
    left_root = root + 2
    right_root = root * 3
    return {
        'value': root,
        'left': bin_tree(height - 1, left_root),
        'right': bin_tree(height - 1, right_root)
    }

custom_tree = bin_tree(height=2, root=5)
print("\nПользовательское дерево:")
print(custom_tree)
