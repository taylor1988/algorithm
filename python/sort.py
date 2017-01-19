# -*-coding:utf-8-*-
import random
import math
import time
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
    #希尔排序
    originallen = len(data)
    step = int(originallen/2)
    while step > 0:
        i = 0
        while i < step:
            last = i
            while (last+step) < originallen:
                index = last
                while index >= i:
                    if data[index+step] < data[index]:
                        temp = data[index+step]
                        data[index + step] = data[index]
                        data[index] = temp
                    else:
                        break
                    index -= step
                last += step
            i += 1
        step = int(step/2)

def resultValidate(data):
    #验证排序结果
    l = len(data)
    for i in range(1, l):
        if data[i] < data[i-1]:
            return False
    return True

data = [random.randint(0,100) for i in range(20000)]
# data = [80, 93, 60, 12, 42, 30, 68, 85, 10]
starttime = time.time()
print('排序前 --- ',  time.time())
shellsort(data)
endtime = time.time()
print('排序后 --- ', time.time())
print('耗时 --- ', endtime-starttime, '验证 -- ',resultValidate(data))