import tkinter as tk
import math

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace("√", "math.sqrt(") + ")" if "√" in expression else expression
        expression = expression.replace("%", "/100")
        expression = expression.replace("x" , "*")
        expression = expression.replace("÷" , "/")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        bg_color = "#222222"
        fg_color = "#ffffff"
        active_bg = "#555555"
        active_fg = "#ffffff"
    else:
        bg_color = "#ffffff"
        fg_color = "#000000"
        active_bg = "#eeeeee"
        active_fg = "#000000"
    
    root.config(bg=bg_color)
    entry.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(
                bg=bg_color, 
                fg=fg_color,
                activebackground=active_bg,
                activeforeground=active_fg
            )
    
    mode_button.config(text="Light Mode" if dark_mode else "Dark Mode")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# لیست دکمه‌ها با ترتیب صحیح
buttons = [
    ("7", "7"), ("8", "8"), ("9", "9"), ("÷", "÷"),
    ("4", "4"), ("5", "5"), ("6", "6"), ("x", "x"),
    ("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"),
    ("0", "0"), (".", "."), ("=", "="), ("+", "+"),
    ("√", "√"), ("%", "%")
]

row = 1
col = 0

for text, val in buttons:
    if val == "=":
        cmd = calculate
    else:
        cmd = lambda x=val: press(x)
    
    tk.Button(
        root, 
        text=text, 
        width=5,
        height=2, 
        font=("Arial", 16), 
        command=cmd
    ).grid(
        row=row, 
        column=col, 
        padx=5, 
        pady=5
    )
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# ردیف آخر با دکمه C و Dark Mode
tk.Button(
    root, 
    text="C", 
    width=11,
    height=2, 
    font=("Arial", 16), 
    command=clear
).grid(
    row=row, 
    column=0, 
    columnspan=2,
    padx=5, 
    pady=5,
    sticky="nsew"
)

# دکمه‌های درصد و رادیکال در ردیف جدید
tk.Button(
    root, 
    text="√", 
    width=5,
    height=2, 
    font=("Arial", 16), 
    command=lambda: press("√")
).grid(
    row=row+1, 
    column=0, 
    padx=5, 
    pady=5
)

tk.Button(
    root, 
    text="%", 
    width=5,
    height=2, 
    font=("Arial", 16), 
    command=lambda: press("%")
).grid(
    row=row+1, 
    column=1, 
    padx=5, 
    pady=5
)

dark_mode = False
mode_button = tk.Button(
    root, 
    text="Dark Mode", 
    width=11,
    height=2, 
    font=("Arial", 16), 
    command=toggle_mode
)
mode_button.grid(
    row=row, 
    column=2, 
    columnspan=2,
    padx=5, 
    pady=5,
    sticky="nsew"
)

# تنظیم اندازه‌گیری ستون‌ها
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()