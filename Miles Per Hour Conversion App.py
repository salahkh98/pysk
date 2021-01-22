print("welcom to the MPH to MPS converter app ")

mil_inp = float(input("what is your speed miles per hour : "))

count_meters = mil_inp * 1609.344


count_second = count_meters / 3600

print("your speed in meters per second" , count_second)