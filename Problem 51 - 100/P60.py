#Merge two lists without using + operator.							

List_1 = [1,2,3,4,5]
List_2 = [6,7,8,9,10]
List_1, List_2 = set(List_1) ,set(List_2)
print(list(List_1.union(List_2)))