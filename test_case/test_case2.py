#coding=utf-8
import unittest
from TestAW.switch_list import switch_list

class switchlist(unittest.TestCase):

    def setUp(self):
        self.a = []
        self.b = []

    def tearDown(self):
        pass

    def test1(self):
        list1 = [2,3,4,5]
        list2 = [1,3,2,1]
        self.a,self.b =switch_list(list1,list2)
        self.assertEqual(abs(sum(self.a)-sum(self.b)),1)

    def test2(self):
        list1 = [1,2]
        list2 = [3,4]
        self.a,self.b =switch_list(list1,list2)
        self.assertEqual(abs(sum(self.a)-sum(self.b)),0)