n = input()
a = [int(x) for x in input().strip().split()]

import random


def qsorting(array, left, right):
    if left < right:
        random_index = partition(array, left, right)
        qsorting(array, left, random_index)
        qsorting(array, random_index + 1, right)


def partition(array, left, right):
    pivot = array[random.randint(left, right)]
    i = left
    j = right
    
    while True:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]
        
qsorting(a, 0, len(a) - 1)
print(" ".join([str(x) for x in a]))
