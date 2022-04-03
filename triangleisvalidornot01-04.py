a=int(input("Enter the length of side a:"))
b=int(input("Enter the length of side b:"))
c=int(input("Enter the length of side c:"))
if a+b>c and b+c>a and c+a>b:
    print("It is a valid triangle")
else:
    print("It is not a valid triangle")
