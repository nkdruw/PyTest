#coding=utf-8
import unittest
from TestAW.yanghui import yanghui

class Test_switchlist(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        val = yanghui(0,0)
        self.assertEqual(val,1)

    def test2(self):
        val = yanghui(1,0)
        self.assertEqual(val,1)

    def test3(self):
        val = yanghui(2,1)
        self.assertEqual(val,2)

    def test4(self):
        val = yanghui(4,2)
        self.assertEqual(val,6)