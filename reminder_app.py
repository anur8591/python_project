import tkinter as tk
from tkinter import messagebox
import time
import threading

def set_reminder():
    reminder_text = reminder_entry.get()
    try:
        delay = int(time_entry.get())
        if reminder_text and delay > 0:
            message_label.config(text=f"Reminder set for {delay} seconds!", fg="green")
            threading.Thread(target=show_reminder, args=(reminder_text, delay), daemon=True).start()
        else:
            message_label.config(text="Enter valid details!", fg="red")
    except ValueError:
        message_label.config(text="Enter a valid number for time!", fg="red")

def show_reminder(reminder_text, delay):
    def countdown(remaining):
        if remaining > 0:
            countdown_label.config(text=f"Time remaining: {remaining} seconds")
            root.after(1000, countdown, remaining - 1)
        else:
            messagebox.showinfo("Reminder", reminder_text)

    root.after(0, countdown, delay)  # Run countdown in the main thread

# GUI Setup
root = tk.Tk()
root.title("Reminder App")

tk.Label(root, text="Enter Reminder:").pack()
reminder_entry = tk.Entry(root, width=40)
reminder_entry.pack()

tk.Label(root, text="Time (in seconds):").pack()
time_entry = tk.Entry(root, width=10)
time_entry.pack()

tk.Button(root, text="Set Reminder", command=set_reminder).pack()

countdown_label = tk.Label(root, text="", fg="blue")
countdown_label.pack()

message_label = tk.Label(root, text="", fg="red")
message_label.pack()

root.mainloop()
