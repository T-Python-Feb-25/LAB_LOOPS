n=int(input("inter a positive integer"))
while n<=0:
    print("try another number")
    n=int(input("inter a positive integer"))
evenNum=0

for num in range(1,n+1):
        if num%2 ==0:
            print(num)
            evenNum+= num
print("The sum of even numbers between 1 and {}"" is {}".format(n,evenNum))
        