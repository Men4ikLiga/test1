import tkinter as tk
from datetime import datetime

# Простое приложение
root = tk.Tk()
root.title("Приложение из GitHub")
root.geometry("400x300")

# Заголовок
label = tk.Label(root, text="🎉 Код запущен из GitHub!", 
                font=("Arial", 16), fg="green")
label.pack(pady=50)

# Информация
info = tk.Label(root, text=f"Запущено: {datetime.now()}", 
               font=("Arial", 12))
info.pack(pady=20)

# Кнопка
button = tk.Button(root, text="Закрыть", command=root.quit,
                  font=("Arial", 12))
button.pack(pady=20)

root.mainloop()
