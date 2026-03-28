# ============================================================
# Part 1 — Student Grade Tracker
# Python Basics & Control Flow
# ============================================================


# ============================================================
# TASK 1 — Data Parsing & Profile Cleaning
# ============================================================

# Raw student data with messy names, string roll numbers,
# and marks stored as a single comma-separated string
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# This list will store all cleaned student dictionaries
cleaned_students = []

print("=" * 40)
print("       TASK 1 — Profile Cleaning")
print("=" * 40)

for student in raw_students:

    # Step 1: Clean the name — remove extra spaces and convert to Title Case
    clean_name = student["name"].strip().title()

    # Step 2: Convert roll number from string to integer
    clean_roll = int(student["roll"])

    # Step 3: Split the marks string on ", " and convert each part to an integer
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]

    # Build a new clean student dictionary
    clean_student = {
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks
    }

    # Add to our cleaned list
    cleaned_students.append(clean_student)

    # Step 4: Validate the name — every word must contain only letters
    is_valid = all(word.isalpha() for word in clean_name.split())

    if is_valid:
        validity = "✓ Valid name"
    else:
        validity = "✗ Invalid name"

    # Step 5: Print the formatted profile card
    print("================================")
    print(f"Student : {clean_name}  {validity}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("================================")

# Step 6: Find the student with roll number 103 and print name in ALL CAPS and lowercase
for student in cleaned_students:
    if student["roll"] == 103:
        print(f"\nStudent with Roll 103:")
        print(f"  ALL CAPS   : {student['name'].upper()}")
        print(f"  lowercase  : {student['name'].lower()}")


# ============================================================
# TASK 2 — Marks Analysis Using Loops & Conditionals
# ============================================================

print("\n" + "=" * 40)
print("    TASK 2 — Marks Analysis")
print("=" * 40)

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print(f"\nStudent: {student_name}\n")

# --- For loop: print each subject, marks, and grade ---

# This function takes a mark and returns the correct grade label
def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "F"

print(f"{'Subject':<12} {'Marks':<8} {'Grade'}")
print("-" * 30)

for i in range(len(subjects)):
    grade = get_grade(marks[i])
    print(f"{subjects[i]:<12} {marks[i]:<8} {grade}")

# --- Calculations ---

total = sum(marks)
average = round(total / len(marks), 2)

# Find highest scoring subject using a simple loop
highest_mark = marks[0]
highest_subject = subjects[0]
for i in range(len(marks)):
    if marks[i] > highest_mark:
        highest_mark = marks[i]
        highest_subject = subjects[i]

# Find lowest scoring subject using a simple loop
lowest_mark = marks[0]
lowest_subject = subjects[0]
for i in range(len(marks)):
    if marks[i] < lowest_mark:
        lowest_mark = marks[i]
        lowest_subject = subjects[i]

print(f"\nTotal Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Highest       : {highest_subject} ({highest_mark})")
print(f"Lowest        : {lowest_subject} ({lowest_mark})")

# --- While loop: simulate a marks-entry system ---

print("\n--- Add New Subjects (type 'done' to stop) ---")

new_subjects_count = 0  # track how many valid subjects were added

while True:
    # Ask for subject name first
    subject_input = input("Enter subject name (or 'done' to stop): ").strip()

    # Stop the loop if user types 'done'
    if subject_input.lower() == "done":
        break

    # Ask for marks for that subject
    marks_input = input(f"Enter marks for {subject_input} (0-100): ").strip()

    # Check if the marks input is a valid number
    if not marks_input.isnumeric():
        print("⚠ Warning: Invalid input — marks must be a number. Skipping.")
        continue

    # Convert to integer and check the range
    new_mark = int(marks_input)
    if new_mark < 0 or new_mark > 100:
        print("⚠ Warning: Marks must be between 0 and 100. Skipping.")
        continue

    # Valid entry — add to the lists
    subjects.append(subject_input)
    marks.append(new_mark)
    new_subjects_count += 1
    print(f"✓ Added: {subject_input} — {new_mark}")

# Print summary after the while loop
updated_average = round(sum(marks) / len(marks), 2)
print(f"\nNew subjects added : {new_subjects_count}")
print(f"Updated average    : {updated_average}")


# ============================================================
# TASK 3 — Class Performance Summary
# ============================================================

print("\n" + "=" * 40)
print("  TASK 3 — Class Performance Summary")
print("=" * 40)

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Print the table header
print(f"\n{'Name':<18} | {'Average':^7} | {'Status'}")
print("-" * 40)

passed = 0
failed = 0
all_averages = []

# Track the class topper
topper_name = ""
topper_avg = 0

for name, student_marks in class_data:

    # Calculate average for this student
    avg = round(sum(student_marks) / len(student_marks), 2)
    all_averages.append(avg)

    # Determine pass or fail
    if avg >= 60:
        status = "Pass"
        passed += 1
    else:
        status = "Fail"
        failed += 1

    # Check if this student is the topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # Print the row for this student
    print(f"{name:<18} | {avg:^7} | {status}")

# Print summary after the table
class_average = round(sum(all_averages) / len(all_averages), 2)

print(f"\nStudents Passed : {passed}")
print(f"Students Failed : {failed}")
print(f"Class Topper    : {topper_name} ({topper_avg})")
print(f"Class Average   : {class_average}")


# ============================================================
# TASK 4 — String Manipulation Utility
# ============================================================

print("\n" + "=" * 40)
print("  TASK 4 — String Manipulation")
print("=" * 40)

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip leading and trailing whitespace
clean_essay = essay.strip()
print(f"\nStep 1 — Stripped Essay:\n{clean_essay}")

# Step 2: Convert to Title Case
print(f"\nStep 2 — Title Case:\n{clean_essay.title()}")

# Step 3: Count how many times "python" appears (case-insensitive)
# clean_essay is already lowercase after strip, so .count("python") works directly
python_count = clean_essay.count("python")
print(f"\nStep 3 — 'python' appears {python_count} time(s)")

# Step 4: Replace "python" with "Python 🐍"
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"\nStep 4 — After Replace:\n{replaced_essay}")

# Step 5: Split into sentences by splitting on ". " (period followed by space)
sentences = clean_essay.split(". ")
print(f"\nStep 5 — Sentences List:\n{sentences}")

# Step 6: Print each sentence numbered, with a "." at the end if missing
print(f"\nStep 6 — Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    # Add a period at the end if the sentence doesn't already have one
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{i}. {sentence}")
