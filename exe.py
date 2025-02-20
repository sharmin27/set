#Write a python program to provide list of numbers and remove duplicates from it using se

def remove_dublicate(lst):
    return list(set(lst))

numbers = [1,2,3,4,5,6,7,6,7,8,1,2]

print(remove_dublicate(numbers))
           

#Write a function that takes two sets and returns a new set containing only the common elements.

def union2(set1,set2):
    return set1&set2

set1= {1,2,3,4,5}
set2 ={2,4,5,6,8}
print(union2(set1,set2))

#Write a function that checks if one set is a subset of another.
def is_subset(small_set, large_set):
    return small_set.issubset(large_set)
set1={1,2,3}
set2= {1,2,3,4,5}

print(is_subset(set1,set2))
