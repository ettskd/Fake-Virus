import tkinter as tk
import random
import threading
import time 
import winsound

POPUP_COUNT = 10
POPUP_TEXTS = ["SYSTEM ERROR!", "DATA CORRUPTED", "WARNING!",
               "VIRUS DETECTED!", "HARD DRIVE FAILING"]
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 100

def play_alert_sound():
    while True:
        winsound.MessageBeep(winsound.MB_ICONHAND)
        time.sleep(1)

class Popup:
    def __init__(self, master=None):
        self.root = tk.Toplevel(master)
        self.root.overrideredirect(True)
        self.root.configure(bg='lightgrey')

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = random.randint(0, screen_width - WINDOW_WIDTH)
        y_position = random.randint(0, screen_height - WINDOW_HEIGHT)

        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_position}+{y_position}")

        title_bar = tk.Frame(self.root, bg="blue", height=20)
        title_bar.pack(fill=tk.X, side=tk.TOP)

        title_label = tk.Label(title_bar, text="ERROR", bg="blue", fg="white", font=("Arial", 10, "bold"))
        close_button = tk.Label(title_bar, text="X",
                                bg="blue", fg="white", font=("Arial", 10, "bold"))
        close_button.pack(side=tk.RIGHT, padx=5)
        close_button.bind("<Button-1>", lambda e: self.root.destroy())

        message_label = tk.Label(self.root, text=random.choice(POPUP_TEXTS),
                                 bg="lightgrey", font=("Arial", 12, "bold"))
        message_label.pack(expand=True, padx=10, pady=20)

def create_popups():
    root = tk.Tk()
    root.withdraw()
    for _ in range(POPUP_COUNT):
        Popup(root)
    
    def add_more_popups():
        while True:
            Popup(root)
            time.sleep(random.uniform(0.5, 1.5))
    
    popup_thread = threading.Thread(target=add_more_popups, daemon=True)
    popup_thread.start()
    root.mainloop()

sound_thread = threading.Thread(target=play_alert_sound, daemon=True)
sound_thread.start()

create_popups()
        