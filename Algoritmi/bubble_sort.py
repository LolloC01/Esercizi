
def swap(s1, s2):
    return s2, s1

import time

def bubble_sort(a: list) -> None:
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = swap(a[j],a[j+1])



def bubble_sort_1(a: list) -> None:
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = swap(a[j],a[j+1])



def bubble_sort_2(a: list) -> None:
    for i in range(len(a)):
        swap_flag: bool = False
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                swap_flag = True
                a[j], a[j+1] = swap(a[j],a[j+1])
        if swap_flag is False:
            break

a: list = [i for i in range(10000,0,-1)]
'''b = a
t: float = time.time()
bubble_sort_2(a)
t1: float = time.time()
print(f"{t1-t}: NON OTTIMIZZATA")
'''
x: float = time.time()
bubble_sort_1(a)
x1: float = time.time()
print(f"{x1-x} PRIMA OTTIMIZZAZIONE")
