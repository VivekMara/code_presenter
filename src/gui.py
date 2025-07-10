from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Code Presenter")
        self.root.configure(bg="#1e1e1e")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="#ffffff")
        style.configure("TButton", background="#333333", foreground="#ffffff")
        self.current_frame = None
    
    def select_file(self):
        filepath = filedialog.askopenfilename(title="Select Code File",filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        print(filepath)
    
    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ttk.Frame(self.root, padding=10)
        self.current_frame.grid()

        ttk.Label(self.current_frame, text="Hello Darthman").grid(row=0, column=0, pady=5)
        ttk.Button(self.current_frame, text="Go to Code Viewer", command=self.show_code_viewer).grid(row=1, column=0, pady=5)
        ttk.Button(self.current_frame, text="Quit", command=self.root.destroy).grid(row=2, column=0, pady=5)
    
    def show_code_viewer(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ttk.Frame(self.root, padding=10)
        self.current_frame.grid()

        ttk.Label(self.current_frame, text="Code Viewer").grid(row=0, column=0, pady=5)
        ttk.Button(self.current_frame, text="Select File", command=self.select_file).grid(row=1, column=0, pady=5)
        ttk.Button(self.current_frame, text="Back to Menu", command=self.show_main_menu).grid(row=2, column=0, pady=5)
    
    def start(self):
        self.root.mainloop()