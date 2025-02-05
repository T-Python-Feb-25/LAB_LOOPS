while True:
    n = int(input("Enter a positive number: "))
    if n > 0:
        print("You entered a positive number")
        break
    if n < 0:
        print("You entered a negative number")
Evensum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        Evensum += i
print(f"The sum of even numbers between 1 and {n} is {Evensum}")