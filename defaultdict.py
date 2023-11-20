from collections import defaultdict as DD
# Defining a dictionary.
dict_1 = DD(list)
for k in range(7, 12):
    dict_1[k].append(k)
print ("Dictionary with values as list:")
print (dict_1)