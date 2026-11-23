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

WINDOW_SIZE = "800x800"

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


# Load student records into the program.
student_list = load_students()

# ==============================================================
#   ! APPLICATION SETUP ! 
# ==============================================================

root = Tk()
root.title("Alexa - Joke Assistant")
root.geometry(WINDOW_SIZE)
root.config(bg=COLORS["bg_color"])

# Prevent the window from being resized
root.resizable(False, True)

# ==============================================================
# START APPLICATION
# ==============================================================

root.mainloop()