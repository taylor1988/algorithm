# -*-coding:utf-8-*-
import random
import math

def insertsort(data):
    #插入排序
    originallen = len(data)
    index = 0
    while index < originallen -1:
        i = index
        while i >= 0:
            if data[i] > data[i+1]:
                temp = data[i+1]
                data[i + 1] = data[i]
                data[i] = temp
            else:
                break
            i -= 1
        index += 1

def bubblesort(data):
    # 冒泡排序
    originallen = len(data)
    index = 0
    while index < (originallen-1):
        i = 0
        while i < (originallen-index-1):
            if data[i]>data[i+1]:
                temp = data[i+1]
                data[i + 1] = data[i]
                data[i] = temp
            i += 1
        index += 1

def shellsort(data):
    pass

data = [random.randint(0,100) for i in range(10)]
# data = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
print('排序前 --- ', data)
bubblesort(data)
print('排序后 --- ', data)

