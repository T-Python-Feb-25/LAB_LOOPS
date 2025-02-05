user_input:int=int(input('Enter a positive integer: '))
if user_input<=0:
    while user_input <=0:
        user_input:int=int(input('Enter a positive integer: '))
sum_of_even=0
for number in range(1,int(user_input)+1):
    if number%2==0:
        sum_of_even+=number
print(f"The sum of even numbers between 1 and {user_input} is {sum_of_even}.")
