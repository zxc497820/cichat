import tkinter as tk

def on_button_click():
    label.config(text="Tkinter работает!")

# Создание главного окна
root = tk.Tk()
root.title("Tkinter Test")

# Создание метки
label = tk.Label(root, text="Нажмите кнопку, чтобы проверить Tkinter")
label.pack(pady=20)

# Создание кнопки
button = tk.Button(root, text="Проверить", command=on_button_click)
button.pack(pady=10)

# Запуск главного цикла
root.mainloop()