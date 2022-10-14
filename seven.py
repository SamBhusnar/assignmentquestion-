get = int(input("Enter any number\n"))
let = get + 1
save = 0
for s in range(1, let):
    if (get % s == 0):
        save = save + 1
if (save == 2):
    print("Entered number is prime ", get)
else:
    print("Entered number is not prime ", get)
