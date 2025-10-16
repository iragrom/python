from main import gen_bin_tree
import unittest

class TestMySolution(unittest.TestCase):

    def test0(self):  # вводный тест
        self.assertEqual(gen_bin_tree(height=1, root=3), {3: [None, None]})

    def test1(self):  # проверка все ли переменные целочисленные (height не int)
        self.assertEqual(gen_bin_tree(height='invalid', root=3), "не верный тип данных")

    def test2(self):  # проверка все ли переменные целочисленные (root не int)
        self.assertEqual(gen_bin_tree(height=1, root=3.444), "не верный тип данных")

    def test3(self):  # проверка все ли переменные целочисленные (height и root не int)
        self.assertEqual(gen_bin_tree(height=[1], root={'one': 1}), "не верный тип данных")

    def test4(self):  # проверка все ли переменные целочисленные (height как float)
        self.assertEqual(gen_bin_tree(height=1.777, root=3), "не верный тип данных")

    def test5(self):  # проверка все ли переменные целочисленные (root как bool)
        self.assertEqual(gen_bin_tree(height=1, root=True), "не верный тип данных")

    def test6(self):  # проверка количества элементов (height < 0)
        self.assertEqual(gen_bin_tree(height=-1, root=3), "не верное количество элементов")

    def test7(self):  # проверка количества элементов (height < 0)
        self.assertEqual(gen_bin_tree(height=0, root=3), "не верное количество элементов")

    def test8(self):  # проверка целочисленный ли переменная root (tuple)
        self.assertEqual(gen_bin_tree(height=1, root=(3, 4)), "не верный тип данных")

    def test9(self):  # проверка целочисленный ли переменная root (string)
        self.assertEqual(gen_bin_tree(height=1, root='three'), "не верный тип данных")

    def test10(self):  # проверка целочисленный ли переменная root (list)
        self.assertEqual(gen_bin_tree(height=1, root=[3]), "не верный тип данных")

    def test11(self):
        """Тест для height=1: корень с двумя None."""
        result = gen_bin_tree(height=1, root=5)
        expected = {5: [None, None]}
        self.assertEqual(result, expected)

    def test12(self):
        """Тест для height=2: дерево с двумя уровнями."""
        result = gen_bin_tree(height=2, root=3)
        expected = {3: [5, 9], 5: [None, None], 9: [None, None]}
        self.assertEqual(result, expected)