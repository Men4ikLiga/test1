import tkinter as tk
import sys
import os
import subprocess

def restart_program():
    """Перезапускает программу"""
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Создаем главное окно
root = tk.Tk()
root.title("Приветствие")
root.geometry("300x150")
root.resizable(False, False)

# Надпись "Привет друг!"
label = tk.Label(
    root, 
    text="Привет друг!", 
    font=("Arial", 16, "bold"),
    fg="blue"
)
label.pack(pady=20)

# Кнопка "Перезапустить"
restart_button = tk.Button(
    root,
    text="Перезапустить",
    command=restart_program,
    font=("Arial", 12),
    bg="lightgreen",
    padx=10,
    pady=5
)
restart_button.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
