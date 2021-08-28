#using numpy library
import numpy as np

def merge(lst):
    arr = np.array(lst)
    return arr.T.tolist()

lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]
print(merge(lst))