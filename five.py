x=int(input("Enter first number\n"));
y=int(input("Enter second number\n"));

if(id(x)==id(y)):
    print("Memory location of two entered number is same \n");
else:
    print("Memory location of two entered number is distinct \n")
# memory allocation is depend upon value of variable if two or more variable have same value then that variable have same memory location if that variable have disting value then that variable have disting memory location 