while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        with open("students.txt", "a") as file:
            name = input("Enter student name: ")
            marks = input("Enter student marks: ")
            file.write(f"{name},{marks}\n")
            print("Student record added successfully!")

    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                print("\n--- Student Records ---")
                print(file.read())
        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Try again.")