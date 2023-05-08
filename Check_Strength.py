import tkinter as tk
from tkinter import messagebox
import re

class PasswordChecker(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Strength Checker")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.password_label = tk.Label(self, text="Enter password:")
        self.password_label.grid(row=0, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)

        self.check_button = tk.Button(self, text="Check Strength", command=self.check_password_strength)
        self.check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.strength_label = tk.Label(self, text="Strength:")
        self.strength_label.grid(row=2, column=0, padx=10, pady=10)

        self.strength_value = tk.StringVar()
        self.strength_value.set("")

        self.strength_display = tk.Label(self, textvariable=self.strength_value)
        self.strength_display.grid(row=2, column=1, padx=10, pady=10)

    def check_password_strength(self):
        password = self.password_entry.get()

        if len(password) < 6:
            self.strength_value.set("Weak")
            return

        has_digit = bool(re.search(r'\d', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

        if has_digit and has_upper and has_lower and has_special:
            self.strength_value.set("Strong")
        elif has_digit and (has_upper or has_lower) and has_special:
            self.strength_value.set("Moderate")
        else:
            self.strength_value.set("Weak")

if __name__ == "__main__":
    app = PasswordChecker()
    app.mainloop()
