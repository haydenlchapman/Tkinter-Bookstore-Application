import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.page_title = tk.Label(self, text="Flourishing Blotts", font=("Cambria", 40))
        self.page_title.config(bg="#00ffff")
        self.page_title.grid(row=0, column=2, pady=(100, 20))
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=1, column=2)

# Define root
root = tk.Tk()
root.title("Flourishing Blotts")
root.attributes("-fullscreen", True)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Instantiate and run our main page
main_page = MainPage(root)
main_page.mainloop()