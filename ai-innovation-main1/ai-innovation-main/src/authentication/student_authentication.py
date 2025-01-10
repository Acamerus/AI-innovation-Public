import json
import hashlib
import os

# File to store student data
STUDENT_DATA_FILE = "students.json"

def load_student_data():
    """Load student data from the JSON file."""
    if not os.path.exists(STUDENT_DATA_FILE):
        return {}
    with open(STUDENT_DATA_FILE, "r") as file:
        return json.load(file)

def save_student_data(data):
    """Save student data to the JSON file."""
    with open(STUDENT_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_student():
    """Register a new student."""
    students = load_student_data()

    student_id = input("Enter your Student ID: ").strip()
    if student_id in students:
        print("Student ID already exists. Please log in or use another ID.")
        return

    password = input("Enter your password: ").strip()
    confirm_password = input("Confirm your password: ").strip()

    if password != confirm_password:
        print("Passwords do not match. Registration failed.")
        return

    students[student_id] = {
        "password": hash_password(password)
    }
    save_student_data(students)
    print("Registration successful!")

def login_student():
    """Authenticate a student."""
    students = load_student_data()

    student_id = input("Enter your Student ID: ").strip()
    password = input("Enter your password: ").strip()

    if student_id not in students:
        print("Student ID not found. Please register first.")
        return

    if students[student_id]["password"] != hash_password(password):
        print("Incorrect password. Please try again.")
        return

    print("Login successful! Welcome, Student.")

def reset_password():
    """Reset a student's password."""
    students = load_student_data()

    student_id = input("Enter your Student ID: ").strip()
    if student_id not in students:
        print("Student ID not found. Please register first.")
        return

    new_password = input("Enter your new password: ").strip()
    confirm_password = input("Confirm your new password: ").strip()

    if new_password != confirm_password:
        print("Passwords do not match. Password reset failed.")
        return

    students[student_id]["password"] = hash_password(new_password)
    save_student_data(students)
    print("Password reset successful!")

def main():
    """Main menu for the student authentication system."""
    while True:
        print("\n--- Student Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Reset Password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            login_student()
        elif choice == "3":
            reset_password()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()