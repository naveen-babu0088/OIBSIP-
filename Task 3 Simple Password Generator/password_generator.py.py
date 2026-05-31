import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        title = tk.Label(
            root,
            text="Advanced Password Generator",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        # Password Length
        length_frame = tk.Frame(root)
        length_frame.pack(pady=5)

        tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)

        self.length_var = tk.IntVar(value=12)
        self.length_spin = tk.Spinbox(
            length_frame,
            from_=4,
            to=100,
            textvariable=self.length_var,
            width=10
        )
        self.length_spin.pack(side=tk.LEFT, padx=5)

        # Character Options
        options_frame = tk.LabelFrame(root, text="Character Options")
        options_frame.pack(fill="x", padx=20, pady=10)

        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        tk.Checkbutton(
            options_frame,
            text="Lowercase Letters (a-z)",
            variable=self.lowercase_var
        ).pack(anchor="w")

        tk.Checkbutton(
            options_frame,
            text="Uppercase Letters (A-Z)",
            variable=self.uppercase_var
        ).pack(anchor="w")

        tk.Checkbutton(
            options_frame,
            text="Numbers (0-9)",
            variable=self.digits_var
        ).pack(anchor="w")

        tk.Checkbutton(
            options_frame,
            text="Symbols (!@#$...)",
            variable=self.symbols_var
        ).pack(anchor="w")

        # Exclude Characters
        exclude_frame = tk.LabelFrame(root, text="Exclude Characters")
        exclude_frame.pack(fill="x", padx=20, pady=10)

        self.exclude_entry = tk.Entry(exclude_frame)
        self.exclude_entry.pack(fill="x", padx=10, pady=5)

        # Password Display
        password_frame = tk.LabelFrame(root, text="Generated Password")
        password_frame.pack(fill="x", padx=20, pady=10)

        self.password_var = tk.StringVar()

        self.password_entry = tk.Entry(
            password_frame,
            textvariable=self.password_var,
            font=("Consolas", 14)
        )
        self.password_entry.pack(fill="x", padx=10, pady=10)

        # Strength Label
        self.strength_label = tk.Label(
            root,
            text="Strength: N/A",
            font=("Arial", 11, "bold")
        )
        self.strength_label.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        ttk.Button(
            button_frame,
            text="Generate Password",
            command=self.generate_password
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame,
            text="Copy to Clipboard",
            command=self.copy_password
        ).grid(row=0, column=1, padx=10)

    def generate_password(self):
        length = self.length_var.get()

        if length < 4:
            messagebox.showerror(
                "Error",
                "Password length must be at least 4."
            )
            return

        charset = ""

        if self.lowercase_var.get():
            charset += string.ascii_lowercase

        if self.uppercase_var.get():
            charset += string.ascii_uppercase

        if self.digits_var.get():
            charset += string.digits

        if self.symbols_var.get():
            charset += string.punctuation

        if not charset:
            messagebox.showerror(
                "Error",
                "Select at least one character type."
            )
            return

        # Remove excluded characters
        excluded = self.exclude_entry.get()

        for char in excluded:
            charset = charset.replace(char, "")

        if not charset:
            messagebox.showerror(
                "Error",
                "No characters available after exclusions."
            )
            return

        password = []

        # Security Rules
        if self.lowercase_var.get():
            password.append(secrets.choice(string.ascii_lowercase))

        if self.uppercase_var.get():
            password.append(secrets.choice(string.ascii_uppercase))

        if self.digits_var.get():
            password.append(secrets.choice(string.digits))

        if self.symbols_var.get():
            password.append(secrets.choice(string.punctuation))

        while len(password) < length:
            password.append(secrets.choice(charset))

        secrets.SystemRandom().shuffle(password)

        final_password = "".join(password[:length])

        self.password_var.set(final_password)
        self.check_strength(final_password)

    def check_strength(self, password):
        score = 0

        if len(password) >= 8:
            score += 1

        if len(password) >= 12:
            score += 1

        if any(c.islower() for c in password):
            score += 1

        if any(c.isupper() for c in password):
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if any(c in string.punctuation for c in password):
            score += 1

        if score <= 2:
            strength = "Weak"

        elif score <= 4:
            strength = "Medium"

        else:
            strength = "Strong"

        self.strength_label.config(
            text=f"Strength: {strength}"
        )

    def copy_password(self):
        password = self.password_var.get()

        if not password:
            messagebox.showwarning(
                "Warning",
                "Generate a password first."
            )
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()