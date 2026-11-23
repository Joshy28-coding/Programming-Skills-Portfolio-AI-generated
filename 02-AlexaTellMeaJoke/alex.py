from tkinter import *
root = Tk()

# ==============================================================
#   Dictionaries and Declarations 
# ==============================================================
COLORS = {
    # ! - Background Colors
    "bg_color": "#0B0F19",  # Background color
    "bg_card": "#111827",  # Card Container
    "bg_card_inner": "#1F2937",  # Inner Card Container
    "bg_entry": "#0F172A",  # Dark Entry Card
}

WINDOW_SIZE = "800x800"

print("Testing GitHub Alignment.")
# Second test in aligning Cloned repository with Github

# ==============================================================
#   ! APPLICATION SETUP ! 
# ==============================================================
root.title("Alexa")
root.geometry(WINDOW_SIZE)
root.config(bg=COLORS["bg_color"])
root.mainloop()