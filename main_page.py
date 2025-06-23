import tkinter as tk
from gc import collect


class MainPage(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.configure(bg="#f5f5dc") # Assign window beige color
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create, style, and place exit button
        tk.Button(self, text="Quit", font=("Cambria, 15"), command=self.quit).grid(row=0, column=0, sticky="e", padx=10, pady=(20, 20))

        # Create and position page title
        self.page_title = tk.Label(self, text="Flourishing Blotts", font=("Cambria", 40))
        self.page_title.config(bg="#00ffff")
        self.page_title.grid(pady=(100, 20))


# Define root window
root = tk.Tk()
root.title("Flourishing Blotts")
root.configure(bg="#f5f5dc") # Assign root beige color
root.attributes("-fullscreen", True) # Enable fullscreen3

main_page = MainPage(root).mainloop() # Instantiate and run main page