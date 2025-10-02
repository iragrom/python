from main import bin_tree
import unittest

class TestMySolution(unittest.TestCase):

    def test0(self):  # вводный тест
        self.assertEqual(bin_tree(height=1, root=3), {'value': 3, 'left': None, 'right': None})

    def test1(self):  # проверка все ли переменные целочисленные (height не int)
        self.assertEqual(bin_tree(height='invalid', root=3), "не верный тип данных")

    def test2(self):  # проверка все ли переменные целочисленные (root не int)
        self.assertEqual(bin_tree(height=1, root=3.444), "не верный тип данных")

    def test3(self):  # проверка все ли переменные целочисленные (height и root не int)
        self.assertEqual(bin_tree(height=[1], root={'one': 1}), "не верный тип данных")

    def test4(self):  # проверка все ли переменные целочисленные (height как float)
        self.assertEqual(bin_tree(height=1.777, root=3), "не верный тип данных")

    def test5(self):  # проверка все ли переменные целочисленные (root как bool)
        self.assertEqual(bin_tree(height=1, root=True), "не верный тип данных")

    def test6(self):  # проверка количества элементов (height < 0)
        self.assertEqual(bin_tree(height=-1, root=3), "не верное количество элементов")

    def test7(self):  # проверка количества элементов (height < 0)
        self.assertEqual(bin_tree(height=0, root=3), "не верное количество элементов")

    def test8(self):  # проверка целочисленный ли переменная root (tuple)
        self.assertEqual(bin_tree(height=1, root=(3, 4)), "не верный тип данных")

    def test9(self):  # проверка целочисленный ли переменная root (string)
        self.assertEqual(bin_tree(height=1, root='three'), "не верный тип данных")

    def test10(self):  # проверка целочисленный ли переменная root (list)
        self.assertEqual(bin_tree(height=1, root=[3]), "не верный тип данных")

    def test11(self):
        """Тест для height=1: корень с двумя None."""
        result = bin_tree(height=1, root=5)
        expected = {'value': 5, 'left': None, 'right': None}
        self.assertEqual(result, expected)

    def test12(self):
        """Тест для height=2: дерево с двумя уровнями."""
        result = bin_tree(height=2, root=3)
        expected = {
            'value': 3,
            'left': {'value': 5, 'left': None, 'right': None},
            'right': {'value': 9, 'left': None, 'right': None}
        }
        self.assertEqual(result, expected)