#using List comprehension and zip
def merge(lst):
    return [list(ele) for ele in list(zip(*lst))] #review my codes from 006 to 012 to understand this line


lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]
print(merge(lst))