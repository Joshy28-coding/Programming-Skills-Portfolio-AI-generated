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
}
# ! - Testing my first GitHub connection!
WINDOW_SIZE = "800x800"

# ==============================================================
# 2. FUNCTIONS
# ==============================================================


def switch_to_frame(frame):
    # ! - Bring the selected frame to the front.
    frame.tkraise()


def display_greeting():
    # ! - Retrieve the name and display a greeting.
    name = widgets["name_entry"].get().strip()

    if name:
        widgets["greeting_label"].config(
            text=f"Hello, {name}!",
            fg=COLORS["fg_text"]
        )
    else:
        widgets["greeting_label"].config(
            text="Please enter your name.",
            fg=COLORS["error"]
        )

def select_difficulty(difficulty):

    # Store the selected difficulty
    app_data["selected_difficulty"] = difficulty

    # Update the next screen
    widgets["selected_difficulty_label"].config(
        text=f"Selected Difficulty: {difficulty.title()}"
    )

    # Navigate to the next frame
    switch_to_frame(frames["second"])


# =============================================================
# 3. FRAME FORMATTING AND CREATION
# =============================================================

def create_difficulty_card(parent, title, subtitle, description, color, difficulty):
    # ! - Creates reusable difficulty card.
    # ! - Uses a specialized format that would easily create the 3 difficulty cards needed for the quiz.

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
        text=subtitle,
        font=FONTS["body"],
        bg=COLORS["bg_card_inner"],
        fg=COLORS["fg_text"]
    ).pack(anchor="w", pady=3)
    
    # ! - Difficulty desription
    Label(
        content,
        text=description,
        font=("Helvetica", 10),
        bg=COLORS["bg_card_inner"],
        fg=COLORS["fg_muted"]
    ).pack(anchor="w")
    
    Button(
        card,
        text=f"Start, {title.title()} →",
        font=FONTS["body"],
        bg=color,
        fg="#0B0F19",
        relief="flat",
        padx=15,
        pady=10,
        command=lambda: select_difficulty(difficulty)
    ).pack(side=RIGHT,padx=16, pady=15)
    
    return card

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
        font=("Helvetica", 10, "bold"),
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
        text="Choose your challenge tier. Each test round comprises 10 questions.\n"
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
    
    # ! - Create the three difficulty cards
    # ! - These three difficulty cards call from cards_container frame, it's been specially formatted to be used
    # ! - as a template so all that is needed is the expected Content for the variables.
    create_difficulty_card(
        cards_container,
        "Easy",
        "Single-Digit Numbers (1 – 9)",
        "Ideal for warming up and mental agility",
        COLORS["easy"],
        "easy"
    )

    create_difficulty_card(
        cards_container,
        "Moderate",
        "Double-Digit Numbers (10 – 99)",
        "Standard challenge testing speed and accuracy",
        COLORS["moderate"],
        "moderate"
    )

    create_difficulty_card(
        cards_container,
        "Advanced",
        "4-Digit Numbers (1000 – 9999)",
        "High complexity mental computation",
        COLORS["advanced"],
        "advanced"
    )

    return frame


def create_second_frame():
    # ! - Create the second screen of the application.
    # ! - Deleted contents to make way for appropriate difficulty test.
    frame = Frame(
        root,
        bg=COLORS["bg_color"]
    )
    
    widgets["selected_difficulty_label"] = Label(
    frame,
    text="",
    font=FONTS["heading"],
    bg=COLORS["bg_color"],
    fg=COLORS["fg_text"]
    )
    widgets["selected_difficulty_label"].pack(pady=15)

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

app_data = {
    "selected_difficulty": None,
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
