"""
图形化计算器 / Graphical Calculator
作者 / Author: SnowCodeDev
描述 / Description: 基于 Tkinter 的简易双语计算器
"""

import tkinter as tk
from tkinter import ttk, messagebox
import locale

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简易计算器 / Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # 设置主题色
        self.bg_color = "#f0f0f0"
        self.btn_color = "#e6e6e6"
        self.accent_color = "#4a90e2"
        self.root.configure(bg=self.bg_color)
        
        # 初始化变量
        self.current_input = tk.StringVar()
        self.history_text = ""
        self.language = "zh"  # 默认中文
        
        self.setup_ui()
        self.bind_keys()
    
    def setup_ui(self):
        """设置用户界面"""
        # 顶部标题
        title_frame = tk.Frame(self.root, bg=self.accent_color, height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="简易计算器 / Simple Calculator",
            font=("Microsoft YaHei", 14, "bold"),
            fg="white",
            bg=self.accent_color
        )
        title_label.pack(expand=True)
        
        # 语言切换按钮
        lang_btn = tk.Button(
            title_frame,
            text="EN/中",
            font=("Arial", 10),
            command=self.toggle_language,
            relief="flat",
            bg="white",
            fg=self.accent_color
        )
        lang_btn.place(relx=0.85, rely=0.5, anchor="center")
        
        # 显示区域
        display_frame = tk.Frame(self.root, bg="white", height=100)
        display_frame.pack(fill="x", padx=20, pady=(20, 10))
        display_frame.pack_propagate(False)
        
        # 历史记录
        self.history_label = tk.Label(
            display_frame,
            text="",
            font=("Arial", 10),
            fg="#666666",
            bg="white",
            anchor="e"
        )
        self.history_label.pack(fill="x", padx=10, pady=(10, 0))
        
        # 当前输入显示
        self.display_entry = tk.Entry(
            display_frame,
            textvariable=self.current_input,
            font=("Arial", 24, "bold"),
            fg="#333333",
            bg="white",
            bd=0,
            justify="right",
            insertwidth=0
        )
        self.display_entry.pack(fill="x", padx=10, pady=(5, 10))
        self.display_entry.configure(state="readonly")
        
        # 按钮区域
        buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        buttons_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # 按钮布局和文本（中文/英文）
        button_configs = [
            # 第一行
            [("C", "C", self.clear_display), ("⌫", "⌫", self.backspace), ("%", "%", lambda: self.add_operator("%")), ("÷", "/", lambda: self.add_operator("/"))],
            # 第二行
            [("7", "7", lambda: self.add_number("7")), ("8", "8", lambda: self.add_number("8")), ("9", "9", lambda: self.add_number("9")), ("×", "*", lambda: self.add_operator("*"))],
            # 第三行
            [("4", "4", lambda: self.add_number("4")), ("5", "5", lambda: self.add_number("5")), ("6", "6", lambda: self.add_number("6")), ("-", "-", lambda: self.add_operator("-"))],
            # 第四行
            [("1", "1", lambda: self.add_number("1")), ("2", "2", lambda: self.add_number("2")), ("3", "3", lambda: self.add_number("3")), ("+", "+", lambda: self.add_operator("+"))],
            # 第五行
            [("±", "±", self.toggle_sign), ("0", "0", lambda: self.add_number("0")), (".", ".", self.add_decimal), ("=", "=", self.calculate)]
        ]
        
        # 创建按钮
        for i, row in enumerate(button_configs):
            buttons_frame.grid_rowconfigure(i, weight=1)
            for j, (zh_text, en_text, command) in enumerate(row):
                buttons_frame.grid_columnconfigure(j, weight=1)
                
                # 特殊样式：操作符按钮和等号按钮
                if zh_text in ["÷", "×", "-", "+", "="]:
                    bg_color = self.accent_color
                    fg_color = "white"
                elif zh_text in ["C", "⌫", "%", "±"]:
                    bg_color = "#d9d9d9"
                    fg_color = "#333333"
                else:
                    bg_color = self.btn_color
                    fg_color = "#333333"
                
                btn = tk.Button(
                    buttons_frame,
                    text=zh_text,
                    font=("Arial", 16, "bold" if zh_text == "=" else "normal"),
                    command=command,
                    bg=bg_color,
                    fg=fg_color,
                    relief="flat",
                    bd=2,
                    activebackground="#cccccc" if zh_text != "=" else "#3a7bc8"
                )
                btn.grid(row=i, column=j, padx=3, pady=3, sticky="nsew")
                btn.zh_text = zh_text
                btn.en_text = en_text
        
        # 历史记录区域
        history_frame = tk.LabelFrame(
            self.root,
            text="历史记录 / History",
            font=("Microsoft YaHei", 10),
            bg=self.bg_color
        )
        history_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.history_textbox = tk.Text(
            history_frame,
            height=4,
            font=("Consolas", 9),
            bg="white",
            fg="#333333",
            state="disabled"
        )
        self.history_textbox.pack(fill="x", padx=5, pady=5)
        
        # 底部状态栏
        status_frame = tk.Frame(self.root, bg="#e0e0e0", height=30)
        status_frame.pack(fill="x")
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="就绪 / Ready",
            font=("Arial", 9),
            fg="#666666",
            bg="#e0e0e0"
        )
        self.status_label.pack(side="left", padx=10)
    
    def bind_keys(self):
        """绑定键盘事件"""
        # 数字键
        for num in range(10):
            self.root.bind(str(num), lambda e, n=num: self.add_number(str(n)))
        
        # 操作符键
        self.root.bind("+", lambda e: self.add_operator("+"))
        self.root.bind("-", lambda e: self.add_operator("-"))
        self.root.bind("*", lambda e: self.add_operator("*"))
        self.root.bind("/", lambda e: self.add_operator("/"))
        
        # 其他键
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<Escape>", lambda e: self.clear_display())
        self.root.bind("<BackSpace>", lambda e: self.backspace())
        self.root.bind(".", lambda e: self.add_decimal())
        self.root.bind("%", lambda e: self.add_operator("%"))
    
    def toggle_language(self):
        """切换界面语言"""
        self.language = "en" if self.language == "zh" else "zh"
        
        # 更新标题
        title = "Simple Calculator" if self.language == "en" else "简易计算器"
        self.root.title(title)
        
        # 更新历史记录框标题
        history_title = "History" if self.language == "en" else "历史记录"
        for child in self.root.winfo_children():
            if isinstance(child, tk.LabelFrame):
                child.config(text=f"{history_title} / {history_title}")
                break
        
        # 更新状态
        status = "Ready" if self.language == "en" else "就绪"
        self.status_label.config(text=status)
        
        # 更新按钮文本
        for child in self.root.winfo_children():
            if isinstance(child, tk.Frame):
                for widget in child.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(text=widget.en_text if self.language == "en" else widget.zh_text)
    
    def add_number(self, number):
        """添加数字到输入框"""
        current = self.current_input.get()
        self.current_input.set(current + number)
        self.status_label.config(text="输入中 / Inputting")
    
    def add_operator(self, operator):
        """添加操作符"""
        current = self.current_input.get()
        if current and current[-1] not in "+-*/%":
            # 将显示的符号转换为实际计算的符号
            display_op = {"÷": "/", "×": "*"}.get(operator, operator)
            self.current_input.set(current + display_op)
            self.status_label.config(text="输入操作符 / Operator entered")
    
    def add_decimal(self):
        """添加小数点"""
        current = self.current_input.get()
        if not current or current[-1] in "+-*/%":
            self.current_input.set(current + "0.")
        elif "." not in current.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1].split("%")[-1]:
            self.current_input.set(current + ".")
    
    def clear_display(self):
        """清除显示"""
        self.current_input.set("")
        self.history_label.config(text="")
        self.status_label.config(text="已清除 / Cleared")
    
    def backspace(self):
        """删除最后一个字符"""
        current = self.current_input.get()
        self.current_input.set(current[:-1])
        self.status_label.config(text="回退 / Backspaced")
    
    def toggle_sign(self):
        """切换正负号"""
        current = self.current_input.get()
        if current:
            # 简单的正负号切换逻辑（实际应该更智能地处理表达式）
            try:
                # 尝试计算当前值并取反
                result = eval(current)
                self.current_input.set(str(-result))
            except:
                # 如果计算失败，直接在开头加负号
                if current[0] == "-":
                    self.current_input.set(current[1:])
                else:
                    self.current_input.set("-" + current)
    
    def calculate(self):
        """执行计算"""
        expression = self.current_input.get()
        if not expression:
            return
        
        try:
            # 替换显示的符号为实际计算的符号
            calc_expr = expression.replace("×", "*").replace("÷", "/")
            
            # 安全评估表达式（在生产环境中应该使用更安全的评估方法）
            result = eval(calc_expr)
            
            # 格式化结果（如果是整数就不显示小数点）
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            # 更新历史记录
            self.history_label.config(text=expression)
            self.add_to_history(f"{expression} = {result}")
            
            # 显示结果
            self.current_input.set(str(result))
            self.status_label.config(text="计算完成 / Calculated")
            
        except ZeroDivisionError:
            error_msg = "错误: 不能除以零 / Error: Cannot divide by zero"
            messagebox.showerror("错误 / Error", error_msg)
            self.status_label.config(text=error_msg)
        except Exception as e:
            error_msg = f"错误: 无效表达式 / Error: Invalid expression"
            messagebox.showerror("错误 / Error", error_msg)
            self.status_label.config(text=error_msg)
    
    def add_to_history(self, entry):
        """添加条目到历史记录"""
        self.history_textbox.config(state="normal")
        
        # 如果历史记录太多，删除最旧的一行
        history_lines = self.history_textbox.get("1.0", "end").strip().split("\n")
        if len(history_lines) >= 10:
            self.history_textbox.delete("1.0", "2.0")
        
        # 添加新条目
        if self.history_textbox.get("1.0", "end-1c"):
            self.history_textbox.insert("end", "\n")
        self.history_textbox.insert("end", entry)
        
        # 滚动到底部
        self.history_textbox.see("end")
        self.history_textbox.config(state="disabled")

def main():
    """主函数"""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
