
print("Welcom to the student Organizer!")

print("Select an Option : ")

while True:
    
    print("1. Add Student")
    print("2. Display all students")
    print("3. Update students information")
    print("4. Delete Student")
    print("5. Disply subject offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    studentID = []
    name = []
    age = []
    grade = []
    dob = []
    subject = set()
    match choice:
        case 1:
            print("Enter student details:")
            
            id = int(input("Enter student ID : "))
            studentID.append(id)
            
            username = input("Enter Name : ")
            name.append(username)
            
            user_age = input("Enter Age : ")
            age.append(user_age)
            
            user_grade = input("Enter Grade : ")
            grade.append(user_grade)
            
            user_dob = input("Enter Date : ")
            dob.append(user_dob)
            
            user_subject = input("Enter Subject : ")
            subject.add(user_subject)
            
            print("student added successfully!")
        case 2:
            print(studentID)
            print(name)
            print(age)
            print(grade)
            print(dob)
            print(subject)
        case _:
            print("Invalid Input!")
    
  
 

