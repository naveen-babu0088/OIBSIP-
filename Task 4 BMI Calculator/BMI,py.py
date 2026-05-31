import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ================= DATABASE =================

conn = sqlite3.connect("bmi_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    weight REAL,
    height REAL,
    bmi REAL,
    category TEXT,
    date TEXT
)
""")
conn.commit()

# ================= BMI FUNCTIONS =================

def calculate_bmi():
    try:
        name = name_var.get().strip()

        if not name:
            messagebox.showerror("Error", "Enter user name")
            return

        weight = float(weight_var.get())
        height_cm = float(height_var.get())

        if weight <= 0 or weight > 500:
            raise ValueError

        if height_cm <= 0 or height_cm > 300:
            raise ValueError

        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

        save_record(
            name,
            weight,
            height_cm,
            bmi,
            category
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Enter valid weight and height values."
        )


def save_record(name, weight, height, bmi, category):

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO bmi_records
    (name,weight,height,bmi,category,date)
    VALUES (?,?,?,?,?,?)
    """,
    (name, weight, height, bmi, category, date))

    conn.commit()

    load_history()


def load_history():

    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("""
    SELECT name,bmi,category,date
    FROM bmi_records
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


def show_graph():

    name = name_var.get().strip()

    if not name:
        messagebox.showwarning(
            "Warning",
            "Enter username first"
        )
        return

    cursor.execute("""
    SELECT bmi,date
    FROM bmi_records
    WHERE name=?
    ORDER BY id
    """, (name,))

    records = cursor.fetchall()

    if len(records) < 1:
        messagebox.showinfo(
            "No Data",
            "No records found."
        )
        return

    bmi_values = [r[0] for r in records]
    dates = [r[1] for r in records]

    plt.figure(figsize=(8,4))
    plt.plot(dates, bmi_values, marker="o")
    plt.title(f"BMI Trend - {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ================= GUI =================

root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("900x700")

title = tk.Label(
    root,
    text="Advanced BMI Calculator",
    font=("Arial",20,"bold")
)
title.pack(pady=10)

# Inputs

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(
    input_frame,
    text="Name:"
).grid(row=0,column=0,padx=5,pady=5)

name_var = tk.StringVar()
tk.Entry(
    input_frame,
    textvariable=name_var
).grid(row=0,column=1)

tk.Label(
    input_frame,
    text="Weight (kg):"
).grid(row=1,column=0,padx=5,pady=5)

weight_var = tk.StringVar()
tk.Entry(
    input_frame,
    textvariable=weight_var
).grid(row=1,column=1)

tk.Label(
    input_frame,
    text="Height (cm):"
).grid(row=2,column=0,padx=5,pady=5)

height_var = tk.StringVar()
tk.Entry(
    input_frame,
    textvariable=height_var
).grid(row=2,column=1)

# Buttons

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate_bmi
).grid(row=0,column=0,padx=10)

ttk.Button(
    button_frame,
    text="Show Trend Graph",
    command=show_graph
).grid(row=0,column=1,padx=10)

# Result

result_label = tk.Label(
    root,
    text="BMI Result",
    font=("Arial",14,"bold")
)

result_label.pack(pady=10)

# History Table

history_frame = tk.Frame(root)
history_frame.pack(fill="both", expand=True)

columns = (
    "Name",
    "BMI",
    "Category",
    "Date"
)

tree = ttk.Treeview(
    history_frame,
    columns=columns,
    show="headings"
)

for col in columns:
    tree.heading(col,text=col)
    tree.column(col,width=180)

tree.pack(
    fill="both",
    expand=True
)

load_history()

root.mainloop()

conn.close()