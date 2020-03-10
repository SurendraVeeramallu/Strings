friends = {"A", "B", "C"}

# To add for the lists
friends.add("D")

print(friends)

# To remove from the lists
# In print the out come will not be in the order
friends.remove("A")

print(friends)


set1 = {"A", "B", "C"}
set2 = {"D", "E", "C"}

# difference
diff = set1.difference(set2)
print(diff)

diff1 = set2.difference(set1)
print(diff1)

# symmetric difference
sys_dif = set1.symmetric_difference(set2)
print(sys_dif)

# Intersection - common on both
inter = set1.intersection(set2)
print(inter)

# Union - evry item but nit duplicated

union = set2.union(set1)
print(union)










