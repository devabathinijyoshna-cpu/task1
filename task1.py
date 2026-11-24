name = input("Enter student name: ")
marks = float(input("Enter aggregate marks: "))
attendance = float(input("Enter attendance: "))
income = float(input("Enter family income: "))
subject = float(input("Enter minimum subject marks: "))

if marks >= 75 and attendance >= 75 and income <= 200000 and subject >= 40:
    print("Student is Eligible for Scholarship")
else:
    print("Student is Not Eligible for Scholarship")