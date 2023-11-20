from collections import OrderedDict

# creating a simple dict
my_dict = {'kiwi': 4, 'apple': 5, 'cat': 3}

# creating empty ordered dict
ordered_dict = OrderedDict()
print(ordered_dict)

# creating ordered dict from dict
ordered_dict = OrderedDict(my_dict)
print(ordered_dict)
