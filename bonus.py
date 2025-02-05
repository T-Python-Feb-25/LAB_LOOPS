#  Bonus Task

n = int(input("Enter a positive integer: "))
sum = 0

while n <= 0:
    n = int(input("Not valid! Enter a positive number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i  

print(f"The sum of even numbers between 1 and {n} is {sum}.")