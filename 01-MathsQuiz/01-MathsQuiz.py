from tkinter import *

# ==============================================================
# 1. CONFIGURATION - Colors, Fonts, and Declaration
# ==============================================================

COLORS = {
    "bg_color": "#0B0F19",  # Background color
    "bg_card": "#111827",  # Card Container
    "bg_card_inner": "#1F2937",  # Inner Card Container
    "bg_entry": "#0F172A",  # Dark Entry Card
    "fg_text": "#F9FAFB",  # White Text
    "fg_muted": "#9CA3AF",  # Muted Grey Text
}

FONTS = {
    "title": ("Helvetica", 16),
    "heading": ("Helvetica", 14),
    "body": ("Helvetica", 12),
}
# Testing my first GitHub connection!
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
            fg="#F87171"
        )


# =============================================================
# 3. FRAME FORMATTING AND CREATION
# =============================================================
def create_home_frame():
    # ! - Create the first screen of the application.

    frame = Frame(root, bg=COLORS["bg_color"])

    Label(
        frame,
        text="Working with multiple frames",
        font=FONTS["title"],
        bg=COLORS["bg_color"],
        fg=COLORS["fg_text"]
    ).pack(pady=15)

    Label(
        frame,
        text="This is Frame 1",
        font=FONTS["body"],
        bg=COLORS["bg_color"],
        fg=COLORS["fg_muted"]
    ).pack(pady=5)

    Label(
        frame,
        text="Enter Name",
        font=FONTS["body"],
        bg=COLORS["bg_color"],
        fg=COLORS["fg_text"]
    ).pack(pady=5)

    widgets["name_entry"] = Entry(
        frame,
        font=FONTS["body"],
        bg=COLORS["bg_entry"],
        fg=COLORS["fg_text"],
        insertbackground=COLORS["fg_text"]
    )
    widgets["name_entry"].pack(pady=5)

    widgets["greeting_label"] = Label(
        frame,
        text="",
        font=FONTS["body"],
        bg=COLORS["bg_color"],
        fg=COLORS["fg_text"]
    )
    widgets["greeting_label"].pack(pady=10)

    Button(
        frame,
        text="Show Greeting",
        font=FONTS["body"],
        command=display_greeting,
        bg=COLORS["bg_color"],
        fg=COLORS["fg_text"]
    ).pack(pady=5)

    Button(
        frame,
        text="Switch to frame 2",
        font=FONTS["body"],
        command=lambda: switch_to_frame(frames["second"]),
        bg=COLORS["bg_color"],
        fg=COLORS["fg_text"]
    ).pack(pady=5)

    return frame


def create_second_frame():
    # ! - Create the second screen of the application.

    frame = Frame(root, bg=COLORS["bg_color"])

    Label(
        frame,
        text="This is Frame 2",
        font=("Roboto", 16),
        bg=COLORS["bg_color"],
        fg=COLORS["fg_text"]
    ).pack(pady=5)

    Button(
        frame,
        text="Switch to Frame 1",
        font=FONTS["body"],
        command=lambda: switch_to_frame(frames["home"]),
        bg=COLORS["bg_color"],
        fg=COLORS["fg_text"]
    ).pack(pady=5)

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

# ! - Create both frames
# Create both frames
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
