import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("Simple UI Design")
root.geometry("400x300")

# 标签
label = tk.Label(root, text="Hello, welcome to the simple UI!", font=("Helvetica", 16))
label.pack(pady=20)

# 输入框
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# 按钮点击事件
def on_button_click():
    user_input = entry.get()
    messagebox.showinfo("Info", f"You entered: {user_input}")

# 按钮
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=20)

# 运行主循环
root.mainloop()
