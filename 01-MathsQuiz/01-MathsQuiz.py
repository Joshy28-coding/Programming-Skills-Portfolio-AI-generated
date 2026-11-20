from tkinter import *
import random

# ==============================================================
# 1. CONFIGURATION - Colors, Fonts, and Declaration
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
    
    # ! - Difficulty Colors
    "easy": "#10B981",
    "moderate": "#00D9F5",
    "advanced": "#8B5CF6",
    
    # ! - Feedback Colors
    "error" : "#F87171"
}

FONTS = {
    "title": ("Helvetica", 16),
    "heading": ("Helvetica", 14),
    "body": ("Helvetica", 12),
    "body_bold": ("Helvetica", 12, "bold"),
}

# ! - Difficulty library eases the use of using loops instead of repeatedly writing the same code.
DIFFICULTIES = {
    "easy": {
        "number_label": "Single-Digit Numbers",
        "min_number": 1,
        "max_number": 9,
        "question_count": 10,
        "description": "Ideal for warming up and mental agility",
    },
    "moderate": {
        "number_label": "Double-Digit Numbers",
        "min_number": 10,
        "max_number": 99,
        "question_count": 10,
        "description": "Standard challenge testing speed and accuracy",
    },
    "advanced": {
        "number_label": "4-Digit Numbers",
        "min_number": 1000,
        "max_number": 9999,
        "question_count": 10,
        "description": "High complexity mental computation",
    },
}

RANKINGS = {
    "A+": {
        "minimum": 91,
        "description": "Outstanding performance!"
    },
    "A": {
        "minimum": 81,
        "description": "Excellent performance!"
    },
    "B": {
        "minimum": 71,
        "description": "Very good performance!"
    },
    "C": {
        "minimum": 61,
        "description": "Good performance!"
    },
    "D": {
        "minimum": 51,
        "description": "Satisfactory performance!"
    },
    "F": {
        "minimum": 0,
        "description": "Keep practising!"
    }
}

WINDOW_SIZE = "800x800"

# ==============================================================
# 2. FUNCTIONS
# ==============================================================

def switch_to_frame(frame):
    # ! - Bring the selected frame to the front.
    frame.tkraise()

def select_difficulty(difficulty):

    # ! - Save the chosen tier and reset state so each round starts fresh.
    app_data["selected_difficulty"] = difficulty
    
    app_data["score"] = 0
    app_data["current_question"] = 1
    app_data["current_attempt"] = 1
    app_data["completed_questions"] = 0

    # ! - Read this tier's settings to update its question counter.
    settings = DIFFICULTIES[difficulty]

    # ! - Refresh the quiz header and score for the selected tier.
    widgets["quiz_difficulty_label"].config(
        text=difficulty.upper()
    )

    widgets["question_count_label"].config(
        text=f"01 / {settings['question_count']}"
    )

    widgets["score_label"].config(
        text="0 pts"
    )

    # ! - Prepare the first question before showing the quiz screen.
    display_question()

    # Reset progress bar
    update_progress()
    
    # ! - Show the quiz screen, then refresh progress after layout dimensions are available.
    switch_to_frame(frames["quiz"])
    root.update_idletasks()
    update_progress()
    
# ! - Generate one arithmetic problem using the selected tier's number range.
def generate_question():

    # ! - Use the selected tier to determine the range for both operands.
    difficulty = app_data["selected_difficulty"]

    # ! - Retrieve its number range
    settings = DIFFICULTIES[difficulty]

    minimum = settings["min_number"]
    maximum = settings["max_number"]

    # ! - Pick operands and an operation for this problem.
    number1 = random.randint(minimum, maximum)
    number2 = random.randint(minimum, maximum)

    # ! - Randomly select addition or subtraction
    operation = random.choice(["+", "-"])

    # ! - Prevent negative subtraction answers
    if operation == "-" and number1 < number2:
        number1, number2 = number2, number1

    # ! - Calculate the correct answer
    if operation == "+":
        answer = number1 + number2

    else:
        answer = number1 - number2

    # Return the question information
    return {
        "number1": number1,
        "number2": number2,
        "operation": operation,
        "answer": answer
    }
    
def display_question():

    # ! - Generate a problem and retain its answer for later checking.
    question = generate_question()

    # Store the question for later answer validation
    app_data["current_question_data"] = question

    # ! - Build the expression shown to the player.
    question_text = (
        f"{question['number1']} "
        f"{question['operation']} "
        f"{question['number2']} = ?"
    )

    # ! - Show the new expression and clear any answer from the previous one.
    widgets["question_label"].config(
        text=question_text
    )
    widgets["answer_entry"].delete(0, END)


def submit_answer():

    # Retrieve the student's input
    user_input = widgets["answer_entry"].get().strip()

    # Prevent empty submissions
    if not user_input:
        widgets["feedback_label"].config(
            text="Please enter an answer.",
            fg=COLORS["error"]
        )
        return

    # Check that the input is a whole number
    try:
        user_answer = int(user_input)

    except ValueError:
        widgets["feedback_label"].config(
            text="Please enter a valid whole number.",
            fg=COLORS["error"]
        )
        return

    # Retrieve the correct answer
    question = app_data["current_question_data"]
    correct_answer = question["answer"]

    # Retrieve the current attempt
    attempt = app_data["current_attempt"]

    # Check whether the answer is correct
    if user_answer == correct_answer:

        # Award points based on the attempt
        if attempt == 1:
            app_data["score"] += 10
            message = "Correct! You earned 10 points."

        else:
            app_data["score"] += 5
            message = "Correct! You earned 5 points."

        widgets["feedback_label"].config(
            text=message,
            fg=COLORS["easy"]
        )

        # Update the displayed score
        widgets["score_label"].config(
            text=f"{app_data['score']} pts"
        )

        resolve_question()

    else:

        # First incorrect attempt
        if attempt == 1:

            app_data["current_attempt"] = 2

            widgets["feedback_label"].config(
                text="Incorrect! Try one more time.",
                fg=COLORS["error"]
            )

            widgets["answer_entry"].delete(0, END)

        # Second incorrect attempt
        else:

            widgets["feedback_label"].config(
                text=f"No points! The correct answer was {correct_answer}.",
                fg=COLORS["error"]
            )

            resolve_question()

def resolve_question():

    # Mark the current question as completed
    app_data["completed_questions"] += 1

    # Update the progress bar
    update_progress()

    # Prevent further answers for this question
    widgets["answer_entry"].config(state=DISABLED)

    # Change the submit button into a navigation button
    widgets["submit_button"].config(
        text="NEXT QUESTION",
        command=advance_question
    )

def advance_question():

    # Retrieve the total number of questions
    difficulty = app_data["selected_difficulty"]

    total = DIFFICULTIES[difficulty]["question_count"]

    # Check whether the quiz has finished
    if app_data["completed_questions"] >= total:
        finish_quiz()
        return

    # Move to the next question
    app_data["current_question"] += 1

    # Reset the attempt counter
    app_data["current_attempt"] = 1

    # Update the question counter
    widgets["question_count_label"].config(
        text=f"{app_data['current_question']:02d} / {total}"
    )

    # Generate the next question
    display_question()

    # Restore the answer input
    widgets["answer_entry"].config(state=NORMAL)

    # Reset feedback
    widgets["feedback_label"].config(
        text="",
        fg=COLORS["fg_muted"]
    )

    # Restore the submit button
    widgets["submit_button"].config(
        text="SUBMIT ANSWER",
        command=submit_answer
    )

def update_progress():

    # ! - Find the completed and total questions for the active tier.
    completed = app_data["completed_questions"]

    difficulty = app_data["selected_difficulty"]
    total = DIFFICULTIES[difficulty]["question_count"]

    # ! - Scale the progress fill to the completed fraction of the quiz.
    percentage = completed / total

    # ! - Use the Canvas width to size the fill rectangle.
    canvas = widgets["progress_canvas"]
    canvas_width = canvas.winfo_width()

    fill_width = canvas_width * percentage

    # ! - Redraw the fill and update the completed/total text.
    canvas.coords(
        widgets["progress_fill"],
        0, 0,
        fill_width, 9
    )

    # ! - Update the completed-question count displayed under the bar.
    widgets["progress_label"].config(
        text=f"{completed} / {total} questions completed"
    )
    
def calculate_rank(score):

    # Check each ranking category
    for rank, details in RANKINGS.items():

        if score >= details["minimum"]:
            return rank, details["description"]

def finish_quiz():

    difficulty = app_data["selected_difficulty"]

    total = DIFFICULTIES[difficulty]["question_count"]
    score = app_data["score"]

    maximum_score = total * 10

    # Calculate the score percentage
    percentage = (score / maximum_score) * 100

    # Update the scoreboard
    widgets["final_score_label"].config(
        text=f"{score} / {maximum_score} POINTS"
    )

    widgets["final_summary_label"].config(
        text=f"You completed {total} questions! "
             f"Your final score is {percentage:.1f}%."
    )
    
    widgets["final_rank_label"].config(
    text=rank
    )

    widgets["rank_description_label"].config(
        text=description
    )
    # Calculate the student's rank
    rank, description = calculate_rank(score)

    # Display results
    switch_to_frame(frames["results"])

# =============================================================
# 3. FRAME FORMATTING AND CREATION
# =============================================================

def create_difficulty_card(parent, difficulty, details):
    # ! - Build one card from a tier key and its matching DIFFICULTIES settings.
    title = difficulty.title()
    color = COLORS[difficulty]
    
    # ! - Keep each card's accent, text, and button inside one reusable container.
    card = Frame(
        parent,
        bg=COLORS["bg_card_inner"]
    )
    card.pack(fill="x", pady=9)

    # ! - Mark the card with the color associated with its difficulty.
    accent = Frame(
        card,
        bg=color,
        width=5
    )
    accent.pack(side=LEFT, fill="y")
    
    # ! - Group the title, range, question count, and description together.
    content = Frame(
        card,
        bg=COLORS["bg_card_inner"]
    )
    content.pack(
        side=LEFT,
        fill="both",
        expand=True,
        padx=16,
        pady=12
    )
    
    # ! - Show the difficulty name and its configured details.
    Label(
        content,
        text=title,
        font=FONTS["heading"],
        bg=COLORS["bg_card_inner"],
        fg=color
    ).pack(anchor="w")
    
    # ! - Difficulty subtitle
    Label(
        content,
        text=(
            f"{details['number_label']} "
            f"({details['min_number']} – {details['max_number']}) · "
            f"{details['question_count']} questions"
        ),
        font=FONTS["body"],
        bg=COLORS["bg_card_inner"],
        fg=COLORS["fg_text"]
    ).pack(anchor="w", pady=3)
    
    # ! - Difficulty desription
    Label(
        content,
        text=details["description"],
        font=("Helvetica", 10),
        bg=COLORS["bg_card_inner"],
        fg=COLORS["fg_muted"]
    ).pack(anchor="w")
    
    # ! - Start a round for this tier when its button is pressed.
    Button(
        card,
        text=f"Start {title.title()} →",
        font=FONTS["body_bold"],
        bg=color,
        fg="#0B0F19",
        relief="flat",
        padx=15,
        pady=10,
        command=lambda: select_difficulty(difficulty)
    ).pack(side=RIGHT,padx=16, pady=15)
    
    return card

# =============================================================
# 3.1 HOMESCREEN FRAME !
# =============================================================
def create_home_frame():
    # ! - Build the home screen where the player chooses a difficulty.

    frame = Frame(
        root,
        bg=COLORS["bg_color"]
    )
    
    # ! - Center the home screen content inside a contrasting panel.
    panel = Frame(
        frame,
        bg=COLORS["bg_card"]
    )
    panel.pack(
        padx=40,
        pady=40,
        fill="both",
        expand="true"
    )
    
    # ! - Identify the application and introduce the difficulty choices.
    Label(
        panel,
        text="- ARITHMETIC MATH QUIZ! -",
        font=FONTS["body_bold"],
        bg=COLORS["bg_card"],
        fg=COLORS["moderate"]
    ).pack(pady=(40, 10))
    
    # Main title
    Label(
        panel,
        text="Select Difficulty Level",
        font=("Helvetica", 26, "bold"),
        bg=COLORS["bg_card"],
        fg=COLORS["fg_text"]
    ).pack()
    
    # ! - Explain the quiz scoring rules before the player starts.
    Label(
        panel,
        text="Choose your challenge tier. Each tier has 10 questions each.\n"
             "Earn 10 points on your first attempt, or 5 points on your second.",
        font=FONTS["body"],
        bg=COLORS["bg_card"],
        fg=COLORS["fg_muted"],
        justify="center"
    ).pack(pady=12)   

    # ! - Hold one generated card for each configured difficulty.
    cards_container = Frame(
        panel,
        bg=COLORS["bg_card"]
    )
    cards_container.pack(
        fill="x",
        padx=35,
        pady=35
    )
    
    # ! - Build cards from the configuration so tier details stay in one place.
    for difficulty, details in DIFFICULTIES.items():
        create_difficulty_card(cards_container, difficulty, details)

    return frame

# =============================================================
# 3.2 MAINQUIZ FRAME !
# =============================================================
def create_quiz_frame():
    # ! - Build the quiz screen and save widgets that callbacks update later.

    frame = Frame(
        root,
        bg=COLORS["bg_color"]
    )

    # ! - Center the quiz sections inside the main content panel.
    panel = Frame(
        frame,
        bg=COLORS["bg_card"]
    )
    panel.pack(
        padx=40,
        pady=40,
        fill="both",
        expand=True
    )
    
    # ------------------------------------------
    # QUIZ PROGRESS BAR
    # ------------------------------------------

    progress_section = Frame(
        panel,
        bg=COLORS["bg_card"]
    )
    progress_section.pack(
        fill="x",
        padx=30,
        pady=(5, 15)
    )

    # ! - Display the completed and total question counts.
    widgets["progress_label"] = Label(
        progress_section,
        text="0 / 10 questions completed",
        font=("Helvetica", 10),
        bg=COLORS["bg_card"],
        fg=COLORS["fg_muted"]
    )
    widgets["progress_label"].pack(anchor="w", pady=(0, 6))

    # ! - Use a Canvas so update_progress can resize the colored fill.
    widgets["progress_canvas"] = Canvas(
        progress_section,
        height=9,
        bg=COLORS["bg_card_inner"],
        highlightthickness=0
    )
    widgets["progress_canvas"].pack(fill="x")

    # ! - Keep the fill item ID so update_progress can redraw it.
    widgets["progress_fill"] = widgets["progress_canvas"].create_rectangle(
        0, 0, 0, 9,
        fill=COLORS["moderate"],
        outline=""
    )

    # ------------------------------------------
    # HEADER
    # ------------------------------------------

    header = Frame(
        panel,
        bg=COLORS["bg_card"]
    )
    header.pack(
        fill="x",
        padx=30,
        pady=25
    )

    Label(
        header,
        text="MATHQUIZ",
        font=FONTS["heading"],
        bg=COLORS["bg_card"],
        fg=COLORS["moderate"]
    ).pack(side=LEFT)

    widgets["quiz_difficulty_label"] = Label(
        header,
        text="",
        font=FONTS["body"],
        bg=COLORS["bg_card"],
        fg=COLORS["fg_muted"]
    )
    widgets["quiz_difficulty_label"].pack(side=RIGHT)

    # ! - Group the current question number and score in the quiz header.
    info_container = Frame(
        panel,
        bg=COLORS["bg_card"]
    )
    info_container.pack(
        fill="x",
        padx=30,
        pady=15
    )

    # ! - Present the current question against the tier's total.
    question_section = Frame(
        info_container,
        bg=COLORS["bg_card"]
    )
    question_section.pack(side=LEFT)

    Label(
        question_section,
        text="QUESTION",
        font=FONTS["body"],
        bg=COLORS["bg_card"],
        fg=COLORS["fg_muted"]
    ).pack(anchor="w")

    widgets["question_count_label"] = Label(
        question_section,
        text="01 / 10",
        font=("Helvetica", 22, "bold"),
        bg=COLORS["bg_card"],
        fg=COLORS["fg_text"]
    )
    widgets["question_count_label"].pack(anchor="w")

    # ! - Show the player's current score.
    score_section = Frame(
        info_container,
        bg=COLORS["bg_card"]
    )
    score_section.pack(side=RIGHT)

    Label(
        score_section,
        text="YOUR SCORE",
        font=FONTS["body"],
        bg=COLORS["bg_card"],
        fg=COLORS["fg_muted"]
    ).pack(anchor="e")

    widgets["score_label"] = Label(
        score_section,
        text="0 pts",
        font=("Helvetica", 22, "bold"),
        bg=COLORS["bg_card"],
        fg=COLORS["easy"]
    )
    widgets["score_label"].pack(anchor="e")

    # ------------------------------------------
    # QUESTION DISPLAY
    # ------------------------------------------

    question_panel = Frame(
        panel,
        bg=COLORS["bg_card_inner"]
    )
    question_panel.pack(
        fill="x",
        padx=30,
        pady=25
    )

    Label(
        question_panel,
        text="SOLVE THE FOLLOWING",
        font=FONTS["body"],
        bg=COLORS["bg_card_inner"],
        fg=COLORS["fg_muted"]
    ).pack(pady=(25, 10))

    widgets["question_label"] = Label(
        question_panel,
        text="Your question will appear here.",
        font=("Helvetica", 26, "bold"),
        bg=COLORS["bg_card_inner"],
        fg=COLORS["fg_text"]
    )
    widgets["question_label"].pack(pady=(5, 25))

    # ------------------------------------------
    # ANSWER INPUT
    # ------------------------------------------

    answer_panel = Frame(
        panel,
        bg=COLORS["bg_card_inner"]
    )
    answer_panel.pack(
        fill="x",
        padx=30,
        pady=10
    )

    Label(
        answer_panel,
        text="YOUR ANSWER",
        font=FONTS["body"],
        bg=COLORS["bg_card_inner"],
        fg=COLORS["fg_muted"]
    ).pack(anchor="w", padx=15, pady=(15, 5))

    widgets["answer_entry"] = Entry(
        answer_panel,
        font=("Arial", 18, "bold"),
        bg=COLORS["bg_entry"],
        fg=COLORS["fg_text"],
        insertbackground=COLORS["fg_text"],
        justify="center"
    )
    widgets["answer_entry"].pack(
        fill="x",
        padx=15,
        pady=(5, 15),
        ipady=8
    )
    widgets["feedback_label"] = Label(
    answer_panel,
    text="",
    font=FONTS["body"],
    bg=COLORS["bg_card_inner"],
    fg=COLORS["fg_muted"]
    )
    widgets["feedback_label"].pack(pady=8)

    # ! - Keep submission disabled until answer-checking behavior is added.
    widgets["submit_button"] = Button(
        answer_panel,
        text="SUBMIT ANSWER",
        font=FONTS["body"],
        bg=COLORS["moderate"],
        fg=COLORS["bg_color"],
        relief="flat",
        state=NORMAL,
        command=submit_answer
    )

    widgets["submit_button"].pack(
        fill="x",
        padx=15,
        pady=(0, 15)
    )

    return frame


def create_results_frame():

    # Creates the final scoreboard.

    frame = Frame(
        root,
        bg=COLORS["bg_color"]
    )

    panel = Frame(
        frame,
        bg=COLORS["bg_card"]
    )
    panel.pack(
        padx=40,
        pady=40,
        fill="both",
        expand=True
    )

    # Results heading
    Label(
        panel,
        text="QUIZ COMPLETED!",
        font=("Helvetica", 26, "bold"),
        bg=COLORS["bg_card"],
        fg=COLORS["moderate"]
    ).pack(pady=(60, 20))

    # Final score
    widgets["final_score_label"] = Label(
        panel,
        text="0 / 100 POINTS",
        font=("Helvetica", 30, "bold"),
        bg=COLORS["bg_card"],
        fg=COLORS["easy"]
    )
    widgets["final_score_label"].pack(pady=15)

    # Performance summary
    widgets["final_summary_label"] = Label(
        panel,
        text="You completed the quiz!",
        font=FONTS["body"],
        bg=COLORS["bg_card"],
        fg=COLORS["fg_muted"]
    )
    widgets["final_summary_label"].pack(pady=10)
    
    widgets["final_rank_label"] = Label(
    panel,
    text="",
    font=("Helvetica", 32, "bold"),
    bg=COLORS["bg_card"],
    fg=COLORS["moderate"]
    )
    widgets["final_rank_label"].pack(pady=10)

    widgets["rank_description_label"] = Label(
    panel,
    text="",
    font=FONTS["body"],
    bg=COLORS["bg_card"],
    fg=COLORS["fg_muted"]
)
    widgets["rank_description_label"].pack(pady=5)

    # Return to home screen
    Button(
        panel,
        text="RETURN TO HOME",
        font=FONTS["body"],
        bg=COLORS["moderate"],
        fg=COLORS["bg_color"],
        relief="flat",
        command=lambda: switch_to_frame(frames["home"])
    ).pack(pady=30)

    return frame


# =============================================================
# 4. APPLICATION SETUP
# =============================================================

# ! - Create the root window before building any frames or widgets.
root = Tk()

root.title("Multiple Frames Example")
root.geometry(WINDOW_SIZE)
root.config(bg=COLORS["bg_color"],)

# ! - Store named frames and widgets for later navigation and updates.
frames = {}
widgets = {}
# ! - Stores individual widgets so functions can access
# ! - and update them without recreating the interface.
# ! - Widgets help me store individual interface components like greeting labels or name entries.


# ! - Hold quiz state separately from the visible Tkinter widgets.
app_data = {
    "selected_difficulty": None,
    "score": 0,
    "current_question": 1,
    "current_attempt": 1,
    "completed_questions": 0,
    
    # ! - Keep the current problem and its answer for answer validation.
    "current_question_data": 0
}

frames["home"] = create_home_frame()
frames["quiz"] = create_quiz_frame()
frames["results"] = create_results_frame()
# Position both frames in the same location
for frame in frames.values():
    frame.place(x=0, y=0, relwidth=1, relheight=1)

switch_to_frame(frames["home"])


# ==========================================
# 5. RUN APPLICATION
# ==========================================

root.mainloop()
