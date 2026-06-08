student = []
while True:
    name = input("Enter your student name:")
    name = name.strip()

    if name.lower() == "exit":
        break
    student.append(name)
    print(student)
    print ("done")
    print("Total number of students:", len(student))
    