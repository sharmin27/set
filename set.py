#set.convert the list into sets
list1 =[1,2,3,4]
sample_set=set(list1)
print(sample_set)

setA=set([1,2,3,4,56])
setB=set([3,4,20,22,26])

#union
print(setA.union(setB))
print(setA|setB)     # | is used to show union

#intersection
print(setA.intersection(setB))
print(setA&setB)

#Difference
print(setA.difference(setB))
print(setB.difference(setA))
var=setA-setB
print(var)
var1=setB-setA
print(var1)
#symmetric difference
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))