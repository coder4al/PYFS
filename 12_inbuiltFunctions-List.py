l = [1, 2, 3, 5, 2, 1, 4, 7, 9, 5]
print("Original List : ", l)
l.append(10)
print("Append\t:  ", l)
l.extend([20, 30])
print("Extend\t:  ", l)
l.insert(0, 40)
print("Insert\t:  ", l)
print(l.remove(40))
print("Remove\t:  ", l)
print(l.pop())
print("Pop\t:  ", l)
val = l.index(5)
print("Index\t:  ", val)
cnt = l.count(5)
print("Count\t:  ", cnt)
l.sort()
print("Sort\t:  ", l)
l.reverse()
print("Reverse\t:  ", l)
lc = l.copy()
print("Copy\t:  ", lc)
l.clear()
print("Clear\t:  ", l)