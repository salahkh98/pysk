print("\t\tsummary table".title())


list_str = ['15','100','55','42']
list_ints = [15,100,55,42]  
list_floats = [15.76,100.21,55.5,42.3]
list_list = [[1,2,3],[4,5,6],[7,8,9]]


print("---------------------------------------")

print("\nThe Variable num_strings is a",type(list_str))
print("It contains the elements:",list_str)
print("the element",list_str[0],"is",type(list_str[0]))
print("---------------------------------------")


print("\nThe Variable num_ints is a",type(list_ints))
print("It contains the elements:",list_str)
print("the element",list_ints[0],"is",type(list_ints[0]))
print("---------------------------------------")


print("\nThe Variable num_strings is a",type(list_floats))
print("It contains the elements:",list_floats)
print("the element",list_floats[0],"is",type(list_floats[0]))
print("---------------------------------------")


print("\nThe Variable num_strings is a",type(list_list))
print("It contains the elements:",list_str)
print("the element",list_list[0],"is",type(list_list[0]))
print("---------------------------------------")

print("now sorting num_stings and num_ints")


print("sorted num_ints" , sorted(list_ints))
print("sorted num_str", sorted(list_str))