while True:
    number = int(input("Enter a positive integer: "))
    if number > 0:
        break

sum_number = 0
for sum in range(1,number + 1):
    if sum % 2 == 0:
        sum_number +=  sum
print(f"The sum of even numbers between 1 and {sum} is {sum_number}.")