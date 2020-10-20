#Owen Coleman
#Write a Python function called counts that takes a list as input and returns a dictionary of unique items in the list as keys and the number of
#times each item appears as values.

def counts(lst):
    d = {}
    for i in lst:
        d[i] = d.get(i , 0) + 1

    return d

abc = ['A', 'A', 'B', 'C', 'A']

print(counts(abc))