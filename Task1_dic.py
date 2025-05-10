student ={'Shaban':30, 'Zeeshan':40,'Alfaiz':50}

student_name =input("Enter student marks : ")

if student_name in student:
    print(f"{student_name}'s marks :{student[student_name]}")
else:
    print("Student not found.")