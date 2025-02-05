 
n = int(input("Enter a positive integer: "))


sum_even = 0


for i in range(2, n + 1, 2):  
    sum_even += i


print(f"The sum of even numbers between 1 and {n} is {sum_even}.")
