Student Manager

A beginner-friendly Python project that demonstrates how to manage student names using lists and loops.

📌 Description

This program:

Takes student names as input from the user
Stores them in a list
Displays the updated student list
Shows the total number of students
Stops when the user enters "exit"

🧠 Concepts Used

Lists
append() method
while True loop
User Input
String Methods (strip(), lower())
Conditional Statements (if)
len() function

💻 Code

student = []

while True:
    name = input("Enter your student name:")
    name = name.strip()

    if name.lower() == "exit":
        break

    student.append(name)

    print(student)
    print("done")
    print("Total number of students:", len(student))

▶️ Example Output

Enter your student name: Rahul
['Rahul']
done
Total number of students: 1

Enter your student name: Aman
['Rahul', 'Aman']
done
Total number of students: 2

Enter your student name: exit

🎯 Learning Outcome

By building this project, you will learn:

How to use lists
How to add items with append()
How to use loops for continuous input
How to count items using len()
How to stop a program using a condition
