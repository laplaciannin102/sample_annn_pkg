# -*- coding: utf-8 -*-

# 参考: [Python標準のunittestの使い方メモ](https://qiita.com/aomidro/items/3e3449fde924893f18ca)

# from .context import sample_annn_pkg as sap
from context import sample_annn_pkg as sap
import unittest


class TestMainModule(unittest.TestCase):
    """
    test sample_annn_pkg.sample_main_module
    """

    def setUp(self):
        """
        最初に実行されるメソッド
        """
        print('*' * 80)
        print('test start!!')
        print()

        print('set up test main module')

        # poyo class object
        self.pc = sap.PoyoClass()

    def test_func02(self):
        """
        test method
        """
        actual = sap.func02()
        expected = 12345

        self.assertEqual(expected, actual)

    def test_load_sample_data1(self):
        """
        test method
        """
        df1 = sap.datasets.load_sample_data1()
        print(df1)

        actual = df1.shape
        expected = (4, 3)

        del df1

        self.assertEqual(expected, actual)


    def tearDown(self):
        """
        最後に実行されるメソッド
        """
        print('tear down main module')

        # delete poyo class object
        del self.pc

        print('test end!!')
        print('*' * 80)
        print()


if __name__ == '__main__':
    unittest.main()
