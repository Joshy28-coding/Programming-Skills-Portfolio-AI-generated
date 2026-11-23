from tkinter import *

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

# ==============================================================
#   ! APPLICATION SETUP ! 
# ==============================================================
root = Tk()
root.title("Alexa")
root.geometry(WINDOW_SIZE)
root.config(bg=COLORS["bg_color"])


root.mainloop()