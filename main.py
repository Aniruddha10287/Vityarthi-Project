def get_valid_subject():
    subjects = ["CSE", "EVS", "English", "Maths"]
    while True:
        sub = input(f"Enter Subject ({'/'.join(subjects)}): ").strip()
        for s in subjects:
            if sub.lower() == s.lower():
                return s
        print("Invalid subject! Choose from CSE, EVS, English, or Maths.")

def get_positive_int(prompt):
    while True:
        val = input(prompt).strip()
        if val.isdigit() and int(val) > 0:
            return int(val)
        print("Invalid input! Please enter a positive whole number.")

def check_attendance():
    print("\n" + "=" * 40 + "\n      STUDENT ATTENDANCE RECORD\n" + "=" * 40)
    name = input("Enter Student Name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter Student Name: ").strip()

    subject = get_valid_subject()
    total_classes = get_positive_int("Enter Total Classes: ")

    while True:
        val = input("Enter Classes Attended: ").strip()
        if val.isdigit() and 0 <= int(val) <= total_classes:
            attended_classes = int(val)
            break
        print(f"Invalid! Attended must be between 0 and {total_classes}.")

    percentage = (attended_classes / total_classes) * 100

    print("\n" + "-" * 40 + "\n           ATTENDANCE REPORT\n" + "-" * 40)
    print(f"Student Name      : {name}")
    print(f"Subject           : {subject}")
    print(f"Total Classes     : {total_classes}")
    print(f"Classes Attended  : {attended_classes}")
    print(f"Attendance Rate   : {percentage:.2f}%")
    print("-" * 40)

    if percentage >= 75.0:
        print("Eligibility Status: ELIGIBLE")
        print("Criteria Remark   : Satisfies 75% rule for CAT 1 & CAT 2.")
    else:
        print("Eligibility Status: NOT ELIGIBLE")
        print("Criteria Remark   : Attendance shortage! Below 75% minimum.")
    print("=" * 40)

def main():
    print("Welcome to Student Attendance Record System")
    while True:
        check_attendance()
        choice = input("\nCheck another record? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            print("Thank you for using the system. Have a great day!")
            break

if __name__ == "__main__":
    main()
