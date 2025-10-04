
total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total += marks   


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
