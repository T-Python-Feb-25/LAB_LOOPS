n:int = int(input("Enter a positive number: "))
while n <= 0:
    n = int(input("wrong numbers, please Enter a positive number: "))   
    
sum:int = 0
for i in range(1,n+1):
    if i % 2 == 0:
        
        sum += i
print(f"the sum of even numbers between 1 and {n} is {sum}")