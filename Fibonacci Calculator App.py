inp = int(input("enter the number: "))


fib = [1,1]

for num in range(inp-2):
    new_fib = fib[num] + fib[num+1]
    fib.append(new_fib)

for num in fib:
    print(num)