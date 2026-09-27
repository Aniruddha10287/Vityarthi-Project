# Student Attendance Record

A beginner-friendly Python console application to track classroom attendance and check **CAT 1** and **CAT 2** exam eligibility based on the **75% attendance criterion**.

---

## 📌 Project Overview

In universities and colleges, students must maintain at least **75% attendance** to appear for internal examinations (CAT 1 and CAT 2). 

This project allows students to record attendance across core subjects, calculates their attendance percentage, and immediately indicates whether they are **Eligible** or have an **Attendance Shortage**.

---

## ✨ Features

- **Beginner-Friendly**: Clean, simple procedural Python code.
- **Core Subject Support**:
  - `CSE` (Computer Science & Engineering)
  - `EVS` (Environmental Studies)
  - `English`
  - `Maths`
- **Defensive Input Validation**:
  - Validates non-empty student name.
  - Enforces case-insensitive subject selection.
  - Ensures total classes is a positive integer.
  - Checks that classes attended does not exceed total classes.
- **Precise Calculation**: Computes attendance percentage up to 2 decimal places.
- **75% Exam Criterion Check**: Clear remarks for CAT 1 & CAT 2 eligibility.
- **Multi-Record Query**: Allows checking another student record without restarting.

---

## ⚙️ Requirements

- **Python 3.8+**
- Operating System: Windows / macOS / Linux
- No external libraries required (uses standard Python library only)

---

## 🚀 How to Run

1. Open the project folder in a terminal.
2. Run `python main.py`.

Follow the on-screen prompts to enter student details and view the result.

---

## 🖥️ Example Output

### Case 1: Eligible Student (Attendance ≥ 75%)

```text
Welcome to Student Attendance Record System

========================================
      STUDENT ATTENDANCE RECORD
========================================
Enter Student Name: Aarav Sharma
Enter Subject (CSE/EVS/English/Maths): CSE
Enter Total Classes: 40
Enter Classes Attended: 32

----------------------------------------
           ATTENDANCE REPORT
----------------------------------------
Student Name      : Aarav Sharma
Subject           : CSE
Total Classes     : 40
Classes Attended  : 32
Attendance Rate   : 80.00%
----------------------------------------
Eligibility Status: ELIGIBLE
Criteria Remark   : Satisfies 75% rule for CAT 1 & CAT 2.
========================================

Check another record? (yes/no): yes
```

### Case 2: Ineligible Student (Attendance < 75%) & Input Validation

```text
========================================
      STUDENT ATTENDANCE RECORD
========================================
Enter Student Name: Diya Patel
Enter Subject (CSE/EVS/English/Maths): Physics
Invalid subject! Choose from CSE, EVS, English, or Maths.
Enter Subject (CSE/EVS/English/Maths): EVS
Enter Total Classes: 40
Enter Classes Attended: 25

----------------------------------------
           ATTENDANCE REPORT
----------------------------------------
Student Name      : Diya Patel
Subject           : EVS
Total Classes     : 40
Classes Attended  : 25
Attendance Rate   : 62.50%
----------------------------------------
Eligibility Status: NOT ELIGIBLE
Criteria Remark   : Attendance shortage! Below 75% minimum.
========================================

Check another record? (yes/no): no

Thank you for using the system. Have a great day!
```

---

## 📁 Project Structure

```text
Student Attendance Record/
├── main.py              # Main Python program (around 50-60 lines)
├── requirements.txt     # Python requirements
├── README.md            # Project documentation and guide
├── Diagrams.pdf         # 2-page system and workflow diagrams
└── Project Report.pdf   # 1-page academic project summary
```
