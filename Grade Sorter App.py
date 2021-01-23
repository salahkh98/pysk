print("welcom to the grade sorter app.")

grade_store = []

grade_store.append(int(input("what is your first grade (0-100): ")))
grade_store.append(int(input("what is your second grade (0-100): ")))
grade_store.append(int(input("what is your third grade (0-100): ")))
grade_store.append(int(input("what is your fourth grade (0-100): ")))

print("\nyour grades is: ",grade_store)

grade_store.sort(reverse=True)

print("\nyour grades from highest to lowest are: ", grade_store)


print("\nthe lowest two grades will now be dropped.")

print("removed grade: ",grade_store[2])
print("removed grade: ",grade_store[3])

del grade_store[2]
del grade_store[-1]

print("\nyour remaining grades are: ",grade_store)

print("\nnice work your highest grade is ",grade_store[0])