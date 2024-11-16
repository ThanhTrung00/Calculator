import tkinter as tk
from tkinter import ttk

class SimpleCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy tính đơn giản")
        self.root.geometry("400x400")

        self.history = []  # Lưu lịch sử phép tính

        self.create_widgets()

    def create_widgets(self):
        # Tạo tab control
        self.notebook = ttk.Notebook(self.root)
        
        # Tạo tab tính toán
        self.tab_calculator = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_calculator, text="Tính toán")
        
        # Tạo tab lịch sử
        self.tab_history = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_history, text="Lịch sử")
        
        self.notebook.pack(expand=1, fill="both")

        # Tab tính toán
        self.entry_display = tk.Entry(self.tab_calculator, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        self.entry_display.grid(row=0, column=0, columnspan=4)

        # Các nút số và toán tử
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.tab_calculator, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

        # Nút xóa
        self.button_clear = tk.Button(self.tab_calculator, text="C", font=("Arial", 18), width=5, height=2, command=self.clear_display)
        self.button_clear.grid(row=5, column=0)

        # Tab lịch sử
        self.history_listbox = tk.Listbox(self.tab_history, font=("Arial", 14), height=10, selectmode=tk.SINGLE)
        self.history_listbox.pack(expand=True, fill="both", padx=10, pady=10)

    def on_button_click(self, button_text):
        if button_text == "=":
            # Tính toán và hiển thị kết quả
            expression = self.entry_display.get()
            try:
                result = str(eval(expression))  # Sử dụng eval để tính toán biểu thức
                self.entry_display.delete(0, tk.END)
                self.entry_display.insert(tk.END, result)
                self.add_to_history(expression + " = " + result)  # Lưu lịch sử
            except Exception as e:
                self.entry_display.delete(0, tk.END)
                self.entry_display.insert(tk.END, "Lỗi")
        else:
            current_text = self.entry_display.get()
            self.entry_display.delete(0, tk.END)
            self.entry_display.insert(tk.END, current_text + button_text)

    def clear_display(self):
        self.entry_display.delete(0, tk.END)

    def add_to_history(self, entry):
        self.history.append(entry)
        self.update_history_listbox()

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for item in self.history:
            self.history_listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculatorApp(root)
    root.mainloop()