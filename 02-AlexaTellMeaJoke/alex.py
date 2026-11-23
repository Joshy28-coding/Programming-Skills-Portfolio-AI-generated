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
    "title": ("Helvetica", 16),
    "heading": ("Helvetica", 14),
    "body": ("Helvetica", 12),
    "body_bold": ("Helvetica", 12, "bold"),
}

WINDOW_SIZE = "800x800"

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

# ==============================================================
#   ! APPLICATION SETUP ! 
# ==============================================================
root = Tk()
root.title("Alexa")
root.geometry(WINDOW_SIZE)
root.config(bg=COLORS["bg_color"])


root.mainloop()