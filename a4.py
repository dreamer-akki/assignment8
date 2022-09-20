#Write a python script to print first 10 odd natural numbers

num=int(input("Please enter a limit\n"))
x=1
while x<=num:
    if x%2!=0:
        print(x)
    x=x+1