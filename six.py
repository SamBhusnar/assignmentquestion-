x=int(input("Enter any number\n"))
y=int(input("Enter any number\n"))
# logical operator "and"," or"," not";
if(x==y and x<=y):
    print("entered number is same and first number is less than equal second number");
elif(x==y or x<y):
    print("entered number is same or first number is less than second number");
elif(not(not(x==44 and y==9))):
    print("first number is 44 and second number is 9");
else:
    print("first number is big than second");
