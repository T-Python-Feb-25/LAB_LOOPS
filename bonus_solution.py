#Bouns

flag = True
while flag:
    number =input("Please Enter a Positive integer : ")
    if number.isdigit():
        number=int(number)
        if number>0:
            flag=False
        else:
            print("input cannot be negative try again..")
    else:
        print("invalid input please try again..")

sum =0
for value in range(1,number+1):
    if value%2==0:
        sum+=value

print(f"The sum of even numbers between 1 and {number} is {sum}.")

