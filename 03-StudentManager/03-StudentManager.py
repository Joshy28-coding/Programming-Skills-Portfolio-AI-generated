from tkinter import *
from pathlib import Path

# ==============================================================
#   Dictionaries and Declarations 
# ==============================================================

COLORS = {
    # ! - Background Colors
    "bg_color": "#0B0F19",  # Background color
    "bg_card": "#111827",  # Card Container
    "bg_card_inner": "#1F2937",  # Inner Card Container
    "bg_entry": "#0F172A",  # Dark Entry Card
    
    # ! - Text Colors
    "fg_text": "#F9FAFB",  # White Text
    "fg_muted": "#9CA3AF",  # Muted Grey Text
}

FONTS = {
    "title": ("Helvetica", 20),
    "heading": ("Helvetica", 14),
    "body": ("Helvetica", 12),
    "body_bold": ("Helvetica", 12, "bold"),
}

# Get the directory where this Python file is located.
BASE_DIR = Path(__file__).resolve().parent

# Locate the student records file.
STUDENT_FILE = BASE_DIR / "resources" / "studentMarks.txt"

# ==============================================================
#   STUDENT DATA FUNCTIONS
# ==============================================================

def load_students():
    """Read student records from the text file and organise them."""

    students = []

    try:
        # Open the student file in read mode.
        with open(STUDENT_FILE, "r", encoding="utf-8") as file:

            # Read the first line to get the expected number of students.
            expected_count = int(file.readline().strip())

            # Read the remaining lines, one student at a time.
            for line in file:

                # Remove unnecessary whitespace and newline characters.
                line = line.strip()

                # Ignore empty lines.
                if not line:
                    continue

                # Separate the information using commas.
                data = line.split(",")

                # Each student should have exactly six pieces of information.
                if len(data) != 6:
                    print(f"Skipping invalid record: {line}")
                    continue

                # Convert the student information into a dictionary.
                student = {
                    "student_number": int(data[0]),
                    "name": data[1],
                    "coursework": [
                        int(data[2]),
                        int(data[3]),
                        int(data[4])
                    ],
                    "exam": int(data[5])
                }

                # Add the student dictionary to our list.
                students.append(student)

        print(f"Successfully loaded {len(students)} students.")

        # Check whether the loaded number matches the file's first line.
        if len(students) != expected_count:
            print(f"Warning: Expected {expected_count} students, "
                  f"but loaded {len(students)}.")

    except FileNotFoundError:
        print(f"Error: Could not find the student file at {STUDENT_FILE}")

    except ValueError:
        print("Error: Student file contains invalid numerical data.")

    return students

def calculate_coursework(student):
    """Calculate the combined coursework mark."""

    return sum(student["coursework"])

def calculate_percentage(student):
    """Calculate the student's overall percentage."""

    coursework_total = calculate_coursework(student)

    overall_total = coursework_total + student["exam"]

    percentage = (overall_total / 160) * 100

    return percentage

def calculate_grade(percentage):
    """Determine the student's grade based on their percentage."""

    if percentage >= 70:
        return "A"

    elif percentage >= 60:
        return "B"

    elif percentage >= 50:
        return "C"

    elif percentage >= 40:
        return "D"

    else:
        return "F"

# Load student records into the program.
student_list = load_students()

# I Prompted ChatGPT for this function
def view_all_students():
    """Display all student records and the class average."""

    total_percentage = 0

    for student in student_list:

        coursework = calculate_coursework(student)
        percentage = calculate_percentage(student)
        grade = calculate_grade(percentage)

        print("-----------------------------------")
        print(f"Student Name: {student['name']}")
        print(f"Student Number: {student['student_number']}")
        print(f"Coursework: {coursework}/60")
        print(f"Exam Mark: {student['exam']}/100")
        print(f"Overall Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")

        total_percentage += percentage

    # Calculate the average percentage for the class.
    if student_list:
        average_percentage = total_percentage / len(student_list)

        print("-----------------------------------")
        print("CLASS SUMMARY")
        print(f"Number of Students: {len(student_list)}")
        print(f"Class Average: {average_percentage:.2f}%")
        print("-----------------------------------")

# ==============================================================
#   STUDENT SEARCH FUNCTIONS
# ==============================================================

def find_student(student_number):
    """Search for a student using their student number."""

    for student in student_list:

        # Check whether the current student's number matches.
        if student["student_number"] == student_number:
            return student

    # Return None if no matching student was found.
    return None

def display_student_record(student, heading="STUDENT RECORD"):
    """Display the academic results of a student."""

    coursework = calculate_coursework(student)
    percentage = calculate_percentage(student)
    grade = calculate_grade(percentage)

    print("-----------------------------------")
    print(heading)
    print(f"Student Name: {student['name']}")
    print(f"Student Number: {student['student_number']}")
    print(f"Coursework: {coursework}/60")
    print(f"Exam Mark: {student['exam']}/100")
    print(f"Overall Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("-----------------------------------")

def view_individual_student(student_number):
    """Find and display an individual student's results."""

    student = find_student(student_number)

    if student is None:
        print("No student found with that student number.")
        return

    display_student_record(student, "INDIVIDUAL STUDENT RECORD")


# ==============================================================
#   STUDENT PERFORMANCE FUNCTIONS
# ==============================================================

def show_highest_student():
    """Find and display the student with the highest overall score."""

    if not student_list:
        print("There are no student records available.")
        return

    highest_student = max(student_list, key=calculate_percentage)

    display_student_record(
        highest_student,
        "HIGHEST OVERALL STUDENT"
    )
    
def show_lowest_student():
    """Find and display the student with the lowest overall score."""

    if not student_list:
        print("There are no student records available.")
        return

    lowest_student = min(student_list, key=calculate_percentage)

    display_student_record(
        lowest_student,
        "LOWEST OVERALL STUDENT"
    )

# ==============================================================
#   STUDENT SORTING FUNCTIONS
# ==============================================================

def sort_students(ascending=True):
    """Sort student records by overall percentage."""

    if not student_list:
        print("There are no student records available.")
        return

    # Sort students according to their overall percentage.
    sorted_students = sorted(
        student_list,
        key=calculate_percentage,
        reverse=not ascending
    )

    # Display the sorted student records.
    print("-----------------------------------")

    if ascending:
        print("STUDENTS SORTED: LOWEST TO HIGHEST")
    else:
        print("STUDENTS SORTED: HIGHEST TO LOWEST")

    print("-----------------------------------")

    total_percentage = 0

    for student in sorted_students:

        display_student_record(student)

        total_percentage += calculate_percentage(student)

    # Display the class summary.
    average_percentage = total_percentage / len(sorted_students)

    print("CLASS SUMMARY")
    print(f"Number of Students: {len(sorted_students)}")
    print(f"Class Average: {average_percentage:.2f}%")
    print("-----------------------------------")

# ==============================================================
#   SAVE STUDENT DATA
# ==============================================================

def save_students():
    """Save all student records back into the text file."""

    try:
        with open(STUDENT_FILE, "w", encoding="utf-8") as file:
            file.write(f"{len(student_list)}\n")

            for student in student_list:
                coursework = student["coursework"]

                file.write(
                    f"{student['student_number']},"
                    f"{student['name']},"
                    f"{coursework[0]},"
                    f"{coursework[1]},"
                    f"{coursework[2]},"
                    f"{student['exam']}\n"
                )

        print("Student records saved successfully.")
        return True

    except OSError as error:
        print(f"Error saving student records: {error}")
        return False

# ==============================================================
#   ADD STUDENT FUNCTION
# ==============================================================

def add_student(student_number, name, coursework1, coursework2,
                coursework3, exam):
    """Validate and add a new student record."""

    # Convert the numerical information into integers.
    try:
        student_number = int(student_number)
        coursework1 = int(coursework1)
        coursework2 = int(coursework2)
        coursework3 = int(coursework3)
        exam = int(exam)

    except ValueError:
        print("Error: Please enter valid numerical marks and student number.")
        return

    # Check the student number is within the required range.
    if not 1000 <= student_number <= 9999:
        print("Error: Student number must be between 1000 and 9999.")
        return

    # Check whether the student number already exists.
    if find_student(student_number):
        print("Error: This student number already exists.")
        return

    # Check the student's name.
    name = name.strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    # Validate coursework marks.
    coursework_marks = [coursework1, coursework2, coursework3]

    if any(mark < 0 or mark > 20 for mark in coursework_marks):
        print("Error: Each coursework mark must be between 0 and 20.")
        return

    # Validate exam mark.
    if not 0 <= exam <= 100:
        print("Error: Exam mark must be between 0 and 100.")
        return

    # Create the new student dictionary.
    new_student = {
        "student_number": student_number,
        "name": name,
        "coursework": coursework_marks,
        "exam": exam
    }

    # Add the student to our list.
    student_list.append(new_student)

    # Save the updated list.
    if save_students():
        print(f"Successfully added {name}.")

    else:
        # Undo the addition if saving failed.
        student_list.remove(new_student)
        print("Student was not added because saving failed.")

# ==============================================================
#   DELETE STUDENT FUNCTION
# ==============================================================
# Allows user to delete selected student records.

def delete_student(student_number=None, name=None):
    """Delete a student using their number or name."""

    student_to_delete = None

    # Search using the student number if provided.
    if student_number is not None:

        try:
            student_number = int(student_number)

        except ValueError:
            print("Error: Invalid student number.")
            return

        student_to_delete = find_student(student_number)

    # Otherwise, search using the student's name.
    elif name is not None:

        matching_students = [
            student for student in student_list
            if student["name"].lower() == name.strip().lower()
        ]

        if len(matching_students) > 1:
            print("Multiple students have that name. Use their student number.")
            return

        if matching_students:
            student_to_delete = matching_students[0]

    else:
        print("Error: Please provide a student number or name.")
        return

    # Check whether a matching student was found.
    if student_to_delete is None:
        print("Error: Student record not found.")
        return

    # Remember the student's original position in the list.
    original_index = student_list.index(student_to_delete)

    # Remove the student.
    student_list.remove(student_to_delete)

    # Save the updated list.
    if save_students():
        print(f"Successfully deleted {student_to_delete['name']}.")

    else:
        # Restore the student if saving failed.
        student_list.insert(original_index, student_to_delete)
        print("Student was not deleted because saving failed.")

# ==============================================================
#   UPDATE STUDENT FUNCTION
# ==============================================================

def update_student(student_number, new_name, coursework1, coursework2,
                   coursework3, exam):
    """Update an existing student's name and academic marks."""

    # Find the student we want to update.
    student = find_student(student_number)

    if student is None:
        print("Error: Student record not found.")
        return

    # Convert the new marks into integers.
    try:
        coursework1 = int(coursework1)
        coursework2 = int(coursework2)
        coursework3 = int(coursework3)
        exam = int(exam)

    except ValueError:
        print("Error: Please enter valid numerical marks.")
        return

    # Validate the new name.
    new_name = new_name.strip()

    if not new_name:
        print("Error: Student name cannot be empty.")
        return

    # Validate coursework marks.
    new_coursework = [coursework1, coursework2, coursework3]

    if any(mark < 0 or mark > 20 for mark in new_coursework):
        print("Error: Each coursework mark must be between 0 and 20.")
        return

    # Validate exam mark.
    if not 0 <= exam <= 100:
        print("Error: Exam mark must be between 0 and 100.")
        return

    # Keep a copy of the original record in case saving fails.
    original_student = student.copy()

    # Update the student's information.
    student["name"] = new_name
    student["coursework"] = new_coursework
    student["exam"] = exam

    # Save the updated records.
    if save_students():
        print(f"Successfully updated {new_name}.")

    else:
        # Restore the original information if saving failed.
        student_list[student_list.index(student)] = original_student
        print("Student was not updated because saving failed.")

# ==============================================================
#   DASHBOARD STATISTICS
# ==============================================================

def get_class_statistics():
    """Calculate the main student performance statistics."""

    if not student_list:
        return {
            "total_students": 0,
            "average": 0,
            "highest": None,
            "lowest": None
        }

    # Calculate the average percentage.
    total_percentage = sum(
        calculate_percentage(student)
        for student in student_list
    )

    average = total_percentage / len(student_list)

    # Find the highest and lowest scoring students.
    highest = max(student_list, key=calculate_percentage)
    lowest = min(student_list, key=calculate_percentage)

    return {
        "total_students": len(student_list),
        "average": average,
        "highest": highest,
        "lowest": lowest
    }

# ==============================================================
#   ! APPLICATION SETUP !
# ==============================================================

root = Tk()
root.title("Student Manager")
root.geometry("1100x900")
root.config(bg=COLORS["bg_color"])
root.minsize(900, 650)

# Main window layout.
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)


# ==============================================================
#   HELPER FUNCTIONS
# ==============================================================

def create_label(parent, text, font, color, bg):
    """Create a consistently styled label."""
    return Label(
        parent,
        text=text,
        font=font,
        fg=color,
        bg=bg
    )


def show_placeholder(section):
    """Temporarily display which section was selected."""
    results_text.config(state=NORMAL)
    results_text.delete("1.0", END)
    results_text.insert(
        END,
        f"{section}\n\n"
        "This section will be connected to the student functions "
        "in the next stages."
    )
    results_text.config(state=DISABLED)


# ==============================================================
#   HEADER
# ==============================================================

header = Frame(
    root,
    bg=COLORS["bg_card"],
    height=85
)
header.grid(row=0, column=0, columnspan=2, sticky="ew")
header.grid_propagate(False)

header.grid_columnconfigure(0, weight=1)

create_label(
    header,
    "STUDENT MANAGER",
    FONTS["title"],
    COLORS["fg_text"],
    COLORS["bg_card"]
).grid(row=0, column=0, sticky="sw", padx=25, pady=(15, 0))

create_label(
    header,
    "ACADEMIC RECORDS SYSTEM",
    FONTS["body"],
    COLORS["fg_muted"],
    COLORS["bg_card"]
).grid(row=1, column=0, sticky="nw", padx=27, pady=(2, 12))


# ==============================================================
#   SIDEBAR
# ==============================================================

sidebar = Frame(
    root,
    bg=COLORS["bg_card"],
    width=220
)
sidebar.grid(row=1, column=0, sticky="ns")
sidebar.grid_propagate(False)

create_label(
    sidebar,
    "MAIN MENU",
    FONTS["body_bold"],
    COLORS["fg_muted"],
    COLORS["bg_card"]
).pack(anchor="w", padx=20, pady=(25, 12))


def create_menu_button(parent, text, command):
    """Create a reusable sidebar button."""
    button = Button(
        parent,
        text=text,
        font=FONTS["body"],
        fg=COLORS["fg_text"],
        bg=COLORS["bg_card"],
        activeforeground=COLORS["fg_text"],
        activebackground=COLORS["bg_card_inner"],
        relief=FLAT,
        anchor="w",
        padx=20,
        pady=12,
        cursor="hand2",
        command=command
    )

    button.pack(fill=X, padx=10, pady=2)

    return button


create_menu_button(
    sidebar,
    "Dashboard",
    lambda: show_placeholder("DASHBOARD")
)

# ==============================================================
#   VIEW ALL STUDENTS - GUI
# ==============================================================

def view_all_students_gui():
    """Display all student records inside the GUI."""

    clear_results()

    # Display the section heading.
    results_text.insert(
        END,
        "ALL STUDENT RECORDS\n",
        "title"
    )

    results_text.insert(
        END,
        "=" * 75 + "\n\n",
        "muted"
    )

    total_percentage = 0

    # Check whether there are any students.
    if not student_list:
        results_text.insert(
            END,
            "No student records are currently available.\n",
            "normal"
        )

        finish_results()
        return

    # Display every student.
    for student in student_list:

        coursework = calculate_coursework(student)
        percentage = calculate_percentage(student)
        grade = calculate_grade(percentage)

        results_text.insert(
            END,
            f"Student Name: {student['name']}\n",
            "heading"
        )

        results_text.insert(
            END,
            f"Student Number: {student['student_number']}\n"
        )

        results_text.insert(
            END,
            f"Coursework: {coursework}/60\n"
        )

        results_text.insert(
            END,
            f"Exam Mark: {student['exam']}/100\n"
        )

        results_text.insert(
            END,
            f"Overall Percentage: {percentage:.2f}%\n"
        )

        results_text.insert(
            END,
            f"Grade: {grade}\n"
        )

        results_text.insert(
            END,
            "-" * 75 + "\n\n",
            "muted"
        )

        total_percentage += percentage

    # Calculate the class average.
    average_percentage = total_percentage / len(student_list)

    # Display the class summary.
    results_text.insert(
        END,
        "CLASS SUMMARY\n",
        "title"
    )

    results_text.insert(
        END,
        f"Number of Students: {len(student_list)}\n"
    )

    results_text.insert(
        END,
        f"Class Average: {average_percentage:.2f}%\n"
    )

    finish_results()

# ==============================================================
#   FIND STUDENT - GUI
# ==============================================================

def show_find_student():
    """Display the student search interface."""

    clear_results()

    results_text.insert(
        END,
        "FIND INDIVIDUAL STUDENT\n\n",
        "title"
    )

    results_text.insert(
        END,
        "Enter a student number below to find their academic record.\n",
        "muted"
    )

    finish_results()

    # Clear any previous search input.
    search_entry.delete(0, END)

create_menu_button(
    sidebar,
    "View All Students",
    view_all_students_gui
)

create_menu_button(
    sidebar,
    "Find Student",
    show_find_student
)
create_label(
    sidebar,
    "STUDENT MANAGEMENT",
    FONTS["body_bold"],
    COLORS["fg_muted"],
    COLORS["bg_card"]
).pack(anchor="w", padx=20, pady=(25, 12))

create_menu_button(
    sidebar,
    "Add Student",
    lambda: show_placeholder("ADD STUDENT")
)

create_menu_button(
    sidebar,
    "Update Student",
    lambda: show_placeholder("UPDATE STUDENT")
)

create_menu_button(
    sidebar,
    "Delete Student",
    lambda: show_placeholder("DELETE STUDENT")
)

create_label(
    sidebar,
    "PERFORMANCE",
    FONTS["body_bold"],
    COLORS["fg_muted"],
    COLORS["bg_card"]
).pack(anchor="w", padx=20, pady=(25, 12))

create_menu_button(
    sidebar,
    "Highest / Lowest",
    lambda: show_placeholder("STUDENT PERFORMANCE")
)

create_menu_button(
    sidebar,
    "Sort Students",
    lambda: show_placeholder("SORT STUDENTS")
)


# ==============================================================
#   MAIN CONTENT AREA
# ==============================================================

main_content = Frame(
    root,
    bg=COLORS["bg_color"]
)
main_content.grid(row=1, column=1, sticky="nsew", padx=25, pady=25)

main_content.grid_columnconfigure(0, weight=1)
main_content.grid_rowconfigure(3, weight=1)


# Dashboard heading.
create_label(
    main_content,
    "Dashboard",
    FONTS["title"],
    COLORS["fg_text"],
    COLORS["bg_color"]
).grid(row=0, column=0, sticky="w")

create_label(
    main_content,
    "Manage student records and academic performance.",
    FONTS["body"],
    COLORS["fg_muted"],
    COLORS["bg_color"]
).grid(row=1, column=0, sticky="w", pady=(5, 20))

# ==============================================================
#   DASHBOARD SUMMARY CARDS
# ==============================================================

summary_frame = Frame(
    main_content,
    bg=COLORS["bg_color"]
)

summary_frame.grid(
    row=2,
    column=0,
    sticky="ew",
    pady=(0, 20)
)

# Give each card equal horizontal space.
for column in range(4):
    summary_frame.grid_columnconfigure(column, weight=1)

def create_summary_card(parent, title, value, column):
    """Create a reusable dashboard statistics card."""

    card = Frame(
        parent,
        bg=COLORS["bg_card"],
        padx=15,
        pady=15
    )

    card.grid(
        row=0,
        column=column,
        sticky="ew",
        padx=5
    )

    create_label(
        card,
        title,
        FONTS["body"],
        COLORS["fg_muted"],
        COLORS["bg_card"]
    ).pack(anchor="w")

    value_label = create_label(
        card,
        value,
        FONTS["title"],
        COLORS["fg_text"],
        COLORS["bg_card"]
    )

    value_label.pack(anchor="w", pady=(8, 0))

    return value_label


# Create four cards that display metrics
student_count_label = create_summary_card(
    summary_frame, "TOTAL STUDENTS", "0", 0
)

average_label = create_summary_card(
    summary_frame, "CLASS AVERAGE", "0%", 1
)

highest_label = create_summary_card(
    summary_frame, "HIGHEST SCORE", "0%", 2
)

lowest_label = create_summary_card(
    summary_frame, "LOWEST SCORE", "0%", 3
)

# ==============================================================
#   REFRESH DASHBOARD
# ==============================================================

def refresh_dashboard():
    """Update the dashboard statistics."""

    statistics = get_class_statistics()

    student_count_label.config(
        text=str(statistics["total_students"])
    )

    average_label.config(
        text=f"{statistics['average']:.2f}%"
    )

    if statistics["highest"]:
        highest_label.config(
            text=f"{calculate_percentage(statistics['highest']):.2f}%"
        )

        lowest_label.config(
            text=f"{calculate_percentage(statistics['lowest']):.2f}%"
        )

    else:
        highest_label.config(text="N/A")
        lowest_label.config(text="N/A")

# ==============================================================
#   RESULTS PANEL
# ==============================================================

results_card = Frame(
    main_content,
    bg=COLORS["bg_card"],
    padx=20,
    pady=20
)
results_card.grid(row=3, column=0, sticky="nsew")

results_card.grid_columnconfigure(0, weight=1)
results_card.grid_rowconfigure(2, weight=1)

create_label(
    results_card,
    "STUDENT RECORDS",
    FONTS["heading"],
    COLORS["fg_text"],
    COLORS["bg_card"]
).grid(row=0, column=0, sticky="w", pady=(0, 15))

# ==============================================================
#   SEARCH INPUT AREA
# ==============================================================

search_frame = Frame(
    results_card,
    bg=COLORS["bg_card"]
)

search_frame.grid(
    row=1,
    column=0,
    sticky="ew",
    pady=(0, 15)
)

create_label(
    search_frame,
    "Student Number",
    FONTS["body_bold"],
    COLORS["fg_text"],
    COLORS["bg_card"]
).pack(side=LEFT, padx=(0, 10))


search_entry = Entry(
    search_frame,
    font=FONTS["body"],
    fg=COLORS["fg_text"],
    bg=COLORS["bg_entry"],
    insertbackground=COLORS["fg_text"],
    relief=FLAT,
    width=20
)

search_entry.pack(side=LEFT, ipady=7, padx=5)

search_button = Button(
    search_frame,
    text="Search",
    font=FONTS["body_bold"],
    fg=COLORS["fg_text"],
    bg=COLORS["bg_card_inner"],
    activebackground=COLORS["bg_card"],
    activeforeground=COLORS["fg_text"],
    relief=FLAT,
    padx=15,
    pady=7,
    cursor="hand2",
    command=search_student_gui
)

search_button.pack(side=LEFT, padx=10)  

results_text = Text(
    results_card,
    font=FONTS["body"],
    fg=COLORS["fg_text"],
    bg=COLORS["bg_entry"],
    insertbackground=COLORS["fg_text"],
    relief=FLAT,
    wrap=WORD,
    padx=15,
    pady=15,
    state=DISABLED
)

results_text.grid(
    row=2,
    column=0,
    sticky="nsew"
)

def search_student_gui():
    """Search for a student and display their academic record."""

    student_number = search_entry.get().strip()

    # Check that the input is not empty.
    if not student_number:
        clear_results()
        results_text.insert(
            END,
            "Please enter a student number.\n",
            "normal"
        )
        finish_results()
        return

    # Check that the input contains only numbers.
    if not student_number.isdigit():
        clear_results()
        results_text.insert(
            END,
            "Invalid input. Please enter a numerical student number.\n",
            "normal"
        )
        finish_results()
        return

    # Search for the student.
    student = find_student(int(student_number))

    clear_results()

    if student is None:
        results_text.insert(
            END,
            "STUDENT NOT FOUND\n\n",
            "title"
        )

        results_text.insert(
            END,
            f"No student exists with number {student_number}.",
            "normal"
        )

    else:
        display_student_record_gui(student)

    finish_results()
    
def display_student_record_gui(student):
    """Display an individual student's academic record."""

    coursework = calculate_coursework(student)
    percentage = calculate_percentage(student)
    grade = calculate_grade(percentage)

    results_text.insert(
        END,
        "STUDENT RECORD\n\n",
        "title"
    )

    results_text.insert(
        END,
        f"Student Name: {student['name']}\n",
        "heading"
    )

    results_text.insert(
        END,
        f"Student Number: {student['student_number']}\n"
    )

    results_text.insert(
        END,
        f"Coursework: {coursework}/60\n"
    )

    results_text.insert(
        END,
        f"Exam Mark: {student['exam']}/100\n"
    )

    results_text.insert(
        END,
        f"Overall Percentage: {percentage:.2f}%\n"
    )

    results_text.insert(
        END,
        f"Grade: {grade}\n"
    )
# ==============================================================
#   RESULTS TEXT FORMATTING
# ==============================================================

results_text.tag_configure(
    "title",
    font=FONTS["heading"],
    foreground=COLORS["fg_text"]
)

results_text.tag_configure(
    "heading",
    font=FONTS["body_bold"],
    foreground=COLORS["fg_text"]
)

results_text.tag_configure(
    "normal",
    font=FONTS["body"],
    foreground=COLORS["fg_text"]
)

results_text.tag_configure(
    "muted",
    font=FONTS["body"],
    foreground=COLORS["fg_muted"]
)

# Why separate these?
# We'll be displaying different things in the same panel: student lists, individual records, search results, and performance information.
#Instead of repeating the same clearing and locking instructions everywhere, we can reuse these two functions.

# ==============================================================
#   RESULTS DISPLAY FUNCTIONS
# ==============================================================

def clear_results():
    """Clear the results panel before displaying new information."""

    results_text.config(state=NORMAL)
    results_text.delete("1.0", END)


def finish_results():
    """Prevent the user from editing the displayed results."""

    results_text.config(state=DISABLED)
    

# ==============================================================
#   START APPLICATION
# ==============================================================

refresh_dashboard()
root.mainloop()
