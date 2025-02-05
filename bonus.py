n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    even_sum = 0

for number in range(1, n +1):
    if number % 2 == 0:
        even_sum += number

        print(f"the sum of even numers between 1 and {n} is {even_sum}.")

