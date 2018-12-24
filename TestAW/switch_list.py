#coding=utf-8
import itertools


def switch_list(list1,list2):
    '''
    将输入的两个List交换元素，使得两个list的元素和的差值最小
    :param list1:
    :param list2:
    :return:
    '''

    c_list = list1 + list2
    all_combine = list(itertools.combinations(c_list,len(c_list)//2))
    list1 = list(min(all_combine,key=lambda x:abs(sum(x)-sum(c_list)/2)))
    list2 = c_list
    for ele in list1:
        list2.remove(ele)
    return list1,list2