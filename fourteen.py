hour=int(input("Enter current time betweeen 0 to 23\n"));
status=input("Dog is barking or not now 'b' and 'n' respectively\n");
if((hour<=6 or hour>=20) and status=='b'):
    print("True");
else:
    print("false");

