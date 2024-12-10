import tkinter as tk

def on_button_click(symbol):
    current_text = entry.get()
    if symbol == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Помилка!")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x500")
root.config(bg="#2c2c2c")

entry = tk.Entry(root, font=("Arial", 20), bg="#333", fg="#fff", bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 20), bg="#e87e1d", fg="#fff", bd=5, relief="raised",
                       command=lambda symbol=text: on_button_click(symbol))
    button.grid(row=row, column=col, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
