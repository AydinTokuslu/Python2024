# Write a function called inter_section that takes two lists and
# finds the intersection (the elements that are present in both
# lists). The function should return a tuple of intersections. Use
# list comprehension in your solution. Use the lists below. Your
# function should return (30, 65, 80).
# list1 = [20, 30, 60, 65, 75, 80, 85]
# list2 = [ 42, 30, 80, 65, 68, 88, 95]

def inter_section(a,b):
    tupleList = []
    for i in a:
        for j in b:
            if i == j:
                tupleList.append(i)
    return tuple(tupleList)

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1,list2))