import tkinter as tk
from tkinter import ttk
import subprocess

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Desktop App")
        self.geometry("600x400")

        # Create a frame to contain main.py content
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Create buttons
        self.start_button = ttk.Button(self, text="Start", command=self.load_main_py)
        self.start_button.pack(side="left", padx=10, pady=10)
        self.exit_button = ttk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(side="right", padx=10, pady=10)

    def load_main_py(self):
        # Execute main.py using subprocess
        try:
            subprocess.Popen(["python", "main.py"], cwd=".")
        except FileNotFoundError:
            print("Error: main.py not found.")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
