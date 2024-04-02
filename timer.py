import tkinter as tk
from tkinter import ttk
import winsound

# Constants
MILLISECONDS_LIMIT = 1000
SECONDS_LIMIT = 60
TIME_DELAY = 10
SOUND_FREQUENCY = 500
SOUND_DURATION = 100

class TimeTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Time Flies")
        self.state = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        self.display = ttk.Label(self.master, font=('Arial', 24), text='00:00:00')
        self.display.grid(row=0, column=0, columnspan=3, pady=10)

        self.start_stop_button = ttk.Button(self.master, text='Start', command=self.start_or_stop)
        self.start_stop_button.grid(row=1, column=0, padx=10, pady=10)

        reset_button = ttk.Button(self.master, text='Reset', command=self.reset)
        reset_button.grid(row=1, column=1, padx=10, pady=10)

        copy_button = ttk.Button(self.master, text='Copy', command=self.copy_to_clipboard)
        copy_button.grid(row=1, column=2, padx=10, pady=10)

    def start_or_stop(self):
        if self.state:
            self.state = False
            self.start_stop_button.config(text='Start')
            winsound.Beep(SOUND_FREQUENCY, SOUND_DURATION)
        else:
            self.state = True
            self.start_stop_button.config(text='Stop')
            self.count_time()
            winsound.Beep(SOUND_FREQUENCY, SOUND_DURATION)

    def reset(self):
        self.state = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.display.config(text='00:00:00')
        self.start_stop_button.config(text='Start')
        winsound.Beep(SOUND_FREQUENCY, SOUND_DURATION)

    def count_time(self):
        if self.state:
            self.milliseconds += TIME_DELAY
            if self.milliseconds >= MILLISECONDS_LIMIT:
                self.milliseconds = 0
                self.seconds += 1
            if self.seconds >= SECONDS_LIMIT:
                self.seconds = 0
                self.minutes += 1
            time_text = "{:02d}:{:02d}:{:03d}".format(self.minutes, self.seconds, self.milliseconds)
            self.display.config(text=time_text)
            self.master.after(TIME_DELAY, self.count_time)

    def copy_to_clipboard(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.display.cget("text"))
        winsound.Beep(SOUND_FREQUENCY, SOUND_DURATION)


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()

    # Configure the colors
    style.configure('TButton', foreground='black', background='light gray')
    style.configure('TLabel', foreground='black', background='white')

    tracker = TimeTracker(root)
    root.mainloop()