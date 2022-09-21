
from typing import List


list1 = [2,0,1,0]

# 1 
print(len(list1)) # number of elements in list

# 2 
print(list[0])  #  2 

# 3
print(list1.count(0))  # in the list two 0

# 4
# print(list[4]) # list does not contain elements in index 4

# 5
print(2 in list1) # number 2 in the list 
 
 # 6
list2 = list1+['A']

# 7
list3 = list1.copy()
list3.sort()

# 8
list4 =list(set(list1))

# 9
list5 = list1[1:3]

# 10
list6 = list1.copy()
list6.reverse()

