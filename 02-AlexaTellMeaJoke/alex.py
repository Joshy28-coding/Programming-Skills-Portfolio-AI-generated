from tkinter import *
from pathlib import Path
import random

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
    "title": ("Helvetica", 16),
    "heading": ("Helvetica", 14),
    "body": ("Helvetica", 12),
    "body_bold": ("Helvetica", 12, "bold"),
}

WINDOW_SIZE = "800x800"

# Get the directory where this Python file is located.
BASE_DIR = Path(__file__).resolve().parent

# Locate the resources folder and its text file.
JOKE_FILE = BASE_DIR / "resources" / "randomJokes.txt"

print("Testing GitHub Alignment.")
# Second test in aligning Cloned repository with Github

# ==============================================================
# FUNCTIONS
# ==============================================================

def switch_to_frame(frame):
    """Raise the requested Tkinter frame so it becomes the visible screen."""
    # ! - Bring the selected frame to the front.
    frame.tkraise()
    
def load_jokes():
    """Read the joke dataset and seperate each joke into setup and punchline"""
    
    jokes = []
    
    try: 
        # Open the text file in read mode.
        with open(JOKE_FILE, "r", encoding="utf-8") as file:
            
            # Read each individual line in the text file.
            for line in file:
                
                # Removes unecessary whitespace and newline characters.
                line = line.strip()
                
                #Ignore empty lines.
                if not line:
                    continue
                
                #seperate the setup and punchline at the first question mark.
                setup, separator, punchline = line.partition("?")

                # Check that the line actually contained a question mark.
                if not separator:
                    print(f"Skipping invalid joke: {line}")
                    continue

                # Store the setup and punchline together.
                jokes.append({
                    "setup": setup + separator,
                    "punchline": punchline.strip()
                })

        print(f"Successfully loaded {len(jokes)} jokes.")
    
    except FileNotFoundError:
        print(f"Error: Could not find the joke file at {JOKE_FILE}")
        
    return jokes

# Load the jokes from the external file text.
joke_list  = load_jokes()

# TEMPORARY CHECK TEST = Display the first joke to test the dataset.
def joke_check():
    if joke_list:
        print(joke_list[0]["setup"])
        print(joke_list[0]["punchline"])

# ==============================================================
# JOKE INTERACTION FUNCTIONS
# ==============================================================

# Stores the currently selected joke.
current_joke = None

def tell_joke():
    """Select a random joke and display its setup."""

    global current_joke

    if not joke_list:
        setup_label.config(text="Sorry! I couldn't find any jokes.")
        punchline_label.config(text="")
        return

    # Avoid repeating the previous joke when possible.
    available_jokes = [
        joke for joke in joke_list
        if joke != current_joke
    ]

    current_joke = random.choice(available_jokes)

    # Display the joke setup.
    setup_label.config(text=current_joke["setup"])

    # Keep the punchline hidden until requested.
    punchline_label.config(text="")

    status_label.config(text="I've got a joke for you!")


def show_punchline():
    """Reveal the punchline of the currently selected joke."""

    if current_joke is None:
        status_label.config(text="Ask me for a joke first!")
        return

    punchline_label.config(text=current_joke["punchline"])
    status_label.config(text="Hope you enjoyed that!")


def next_joke():
    """Load another joke."""

    tell_joke()

# ==============================================================
#   ! APPLICATION SETUP ! 
# ==============================================================

root = Tk()
root.title("Alexa - Joke Assistant")
root.geometry(WINDOW_SIZE)
root.config(bg=COLORS["bg_color"])

# Prevent the window from being resized
root.resizable(False, True)

# =============================================================
# ! MAIN APPLICATION FRAME !
# =============================================================

main_frame = Frame(
    root,
    bg=COLORS["bg_color"]
)
main_frame.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=40
)

# =============================================================
# ! ASSISTANT CARD !
# =============================================================
card_frame = Frame(
    main_frame,
    bg=COLORS["bg_card"],
    padx=30,
    pady=30
)
card_frame.pack(
    fill="both",
    expand=True
)
# =============================================================
# ! HEADER SECTION !
# =============================================================

title_label = Label(
    card_frame,
    text="ALEXA",
    font=FONTS["title"],
    fg= COLORS["fg_text"],
    bg=["bg_card"]
)
title_label.pack(pady(15, 5))

status_label = Label(
    card_frame,
    text="Hello! I'm ready to tell you a very silly joke, listen in?",
    font=FONTS["body"],
    fg=COLORS["fg_muted"],
    bg=["bg_card"]
)
status_label.pack(pady=(0, 30))

# ==============================================================
# JOKE DISPLAY SECTION
# ==============================================================

joke_frame = Frame(
    card_frame,
    bg=COLORS["bg_card_inner"],
    padx=25,
    pady=35
)

joke_frame.pack(
    fill="x",
    pady=10
)


setup_label = Label(
    joke_frame,
    text="Press the button below to hear a joke!",
    font=FONTS["heading"],
    fg=COLORS["fg_text"],
    bg=COLORS["bg_card_inner"],
    wraplength=550,
    justify="center"
)

setup_label.pack(pady=(10, 25))


punchline_label = Label(
    joke_frame,
    text="",
    font=FONTS["body_bold"],
    fg="#60A5FA",
    bg=COLORS["bg_card_inner"],
    wraplength=550,
    justify="center"
)

punchline_label.pack(pady=(5, 10))

# ==============================================================
# JOKE DISPLAY SECTION
# ==============================================================

button_frame = Frame(
    card_frame,
    bg=COLORS["bg_card"]
)
button_frame.pack(fill="x", pady=25)

# The Main silly joke button
joke_button = Button(
    button_frame,
    text="Alexa tell me a joke!",
    font=FONTS["body_bold"],
    fg=COLORS["fg_text"],
    bg="#2563EB",
    activebackground="#1D4ED8",
    activeforeground=COLORS[fg_text],
    command=tell_joke,
    crusor="hand2",
    relief="flat",
    padx=20,
    pady=12
)
joke_button.pack(
    fill="x",
    pady=8
)
root.mainloop()