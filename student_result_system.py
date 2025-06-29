class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_result(self):
        print(f"\nName: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")
        average = sum(self.marks)/len(self.marks)
        print(f"Average: {average}")
        if average >= 60:
            print("Result: Passed")
        else:
            print("Result: Failed")

students = []

while True:
    print("\n1. Add Student\n2. View Results\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = list(map(int, input("Enter 3 subject marks separated by space: ").split()))
        s = Student(name, roll, marks)
        students.append(s)
        print("Student added successfully!")

    elif choice == '2':
        for s in students:
            s.display_result()

    elif choice == '3':
        break

    else:
        print("Invalid choice.")
