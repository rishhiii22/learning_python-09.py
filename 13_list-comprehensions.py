myList = [1,2,5,7,9]

# General Way :-  

#squaredList = []
#for item in myList:
#    squaredList.append(item*item)

# Using List Comprehensions...

squaredList = [i*i for i in myList]
print(squaredList)