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
    "title": ("Helvetica", 20),
    "heading": ("Helvetica", 14),
    "body": ("Helvetica", 12),
    "body_bold": ("Helvetica", 12, "bold"),
}

WINDOW_SIZE = "800x800"

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