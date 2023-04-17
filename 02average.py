sub1 = float(input("Enter mrks of Sub1: "))
sub2 = float(input("Enter mrks of Sub2: "))
sub3 = float(input("Enter mrks of Sub3: "))
sub4 = float(input("Enter mrks of Sub4: "))
sub5 = float(input("Enter mrks of Sub5: "))
total = sub1+sub2+sub3+sub4+sub5
avg = total/5
if avg >=80:
    grade = "A"
elif avg>=70 and avg<80:
    grade = "B"
elif avg>=60 and avg<70:
    grade = "C"
elif avg>=40 and avg<60:
    grade = "D"
else :
    grade = "E"
print(f"\nThe Total marks is {total}\nThe Average is {avg}\nThe Grade Alloted is {grade}")
