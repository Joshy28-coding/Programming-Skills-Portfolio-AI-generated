from tkinter import *


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

WINDOW_SIZE = "800x800"

# ==============================================================
# 2. FUNCTIONS
# ==============================================================
def switch_to_frame(frame):
    # ! - Bring the selected frame to the front.
    frame.tkraise()

def select_difficulty(difficulty):

    # Store the selected difficulty
    app_data["selected_difficulty"] = difficulty

    # Retrieve the selected difficulty settings
    settings = DIFFICULTIES[difficulty]

    # Update the quiz screen information
    widgets["quiz_difficulty_label"].config(
        text=difficulty.upper()
    )

    widgets["question_count_label"].config(
        text=f"01 / {settings['question_count']}"
    )

    widgets["score_label"].config(
        text="0 pts"
    )

    # Navigate to the quiz screen
    switch_to_frame(frames["quiz"])


# =============================================================
# 3. FRAME FORMATTING AND CREATION
# =============================================================

def create_difficulty_card(parent, difficulty, details):
    # ! - Creates reusable difficulty card.
    # ! - Uses a specialized components that would easily create the 3 difficulty cards needed for the quiz homescreen.
    # ! - Below are the declarations of various variables and attributes that create the key components such as difficulty descriptions, colors, etc.
    title = difficulty.title()
    color = COLORS[difficulty]
    
    # ! - Main card container
    card = Frame(
        parent,
        bg=COLORS["bg_card_inner"]
    )
    card.pack(fill="x", pady=9)

    # ! - Coloured vertical accent on the left
    accent = Frame(
        card,
        bg=color,
        width=5
    )
    accent.pack(side=LEFT, fill="y")
    
    # ! - Container for the card's text
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
    
    # ! - Difficulty heading
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
    # ! - Create the first screen of the application.
    # ! - Difficulty selection screen.

    frame = Frame(
        root,
        bg=COLORS["bg_color"]
    )
    
    # Main content panel
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
    
    # Small application heading
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
    
    # ! - Greetings Description and challenge introduction.
    Label(
        panel,
        text="Choose your challenge tier. Each tier has 10 questions each.\n"
             "Earn 10 points on your first attempt, or 5 points on your second.",
        font=FONTS["body"],
        bg=COLORS["bg_card"],
        fg=COLORS["fg_muted"],
        justify="center"
    ).pack(pady=12)   

    # Container for the difficulty cards
    cards_container = Frame(
        panel,
        bg=COLORS["bg_card"]
    )
    cards_container.pack(
        fill="x",
        padx=35,
        pady=35
    )
    
    # ! - Further optimized code instead of calling all different items repeatedly, the card builder receives and loops the settings dictionary directly.
    for difficulty, details in DIFFICULTIES.items():
        create_difficulty_card(cards_container, difficulty, details)

    return frame

# =============================================================
# 3.2 MAINQUIZ FRAME !
# =============================================================
def create_quiz_frame():
    # Creates the main quiz interface.

    frame = Frame(
        root,
        bg=COLORS["bg_color"]
    )

    # Main content panel
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

    # ------------------------------------------
    # SCORE AND QUESTION COUNTER
    # ------------------------------------------

    info_container = Frame(
        panel,
        bg=COLORS["bg_card"]
    )
    info_container.pack(
        fill="x",
        padx=30,
        pady=15
    )

    # Question counter
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

    # Score display
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
        font=("Helvetica", 18),
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

    # Submit button will be connected in our next lesson.
    widgets["submit_button"] = Button(
        answer_panel,
        text="SUBMIT ANSWER",
        font=FONTS["body"],
        bg=COLORS["moderate"],
        fg=COLORS["bg_color"],
        relief="flat",
        state=DISABLED
    )
    widgets["submit_button"].pack(
        fill="x",
        padx=15,
        pady=(0, 15)
    )

    return frame


# =============================================================
# 4. APPLICATION SETUP
# =============================================================

# ! - Dictionaries for storing application objects
root = Tk()

root.title("Multiple Frames Example")
root.geometry(WINDOW_SIZE)
root.config(bg=COLORS["bg_color"],)

# ! - dictionaries
frames = {}
widgets = {}
# ! - Stores individual widgets so functions can access
# ! - and update them without recreating the interface.
# ! - Widgets help me store individual interface components like greeting labels or name entries.


# ! - Helps store information such as selected difficulty.
# ! - Unlike widgets that is currently storing interface components, app_data helps store application information.
app_data = {
    "selected_difficulty": None,
    "score": 0,
    "current_question": 1,
    "current_attempt": 1
}

# ! - Create both frames
frames["home"] = create_home_frame()
frames["second"] = create_second_frame()

# Position both frames in the same location
for frame in frames.values():
    frame.place(x=0, y=0, relwidth=1, relheight=1)

switch_to_frame(frames["home"])


# ==========================================
# 5. RUN APPLICATION
# ==========================================

root.mainloop()
