
total = 0

print("Enter marks of 5 subjects:")
a=float(input("Subject 1: "))
b=float(input("Subject 2: "))
c=float(input("Subject 3: "))
d=float(input("Subject 4: "))
e=float(input("Subject 5: "))   
total = a + b + c + d + e
print("\nTotal Marks:", total)


avg = total / 5

print("\nAverage Marks:", avg)


if avg >= 90:
    print("Grade S")
elif avg >= 80:
    print("Grade A")
elif avg >= 70:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
elif avg >= 35:
    print("Grade D")
else:
    print("Fail")
