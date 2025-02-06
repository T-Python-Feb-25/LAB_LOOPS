## Bonus (Sum of Even Numbers)

number= int (input("Enter positive number: "))
i=2
even_numbers=0
for i in range(1, number+1):
    if i%2== 0:
        even_numbers+=i
        
        
print(f"The sum of even numbers between 1 and {number} is {even_numbers}")