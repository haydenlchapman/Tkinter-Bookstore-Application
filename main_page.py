import tkinter as tk

BACKGROUND_COLOR = "#f5f5dc" # Beige
BOOKSTORE_TITLE = "Flourishing Blotts"

class MainPage(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.configure(bg=BACKGROUND_COLOR) # Assign window beige color
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create, style, and place exit button
        tk.Button(self, text="Quit", font=("Cambria, 15"), command=self.quit).grid(pady=(20, 20))

        # Create and position page title
        self.page_title = tk.Label(self, text=BOOKSTORE_TITLE, font=("Cambria", 40))
        self.page_title.config(bg="#00ffff")
        self.page_title.grid(pady=(100, 20))


# Define root window
root = tk.Tk()
root.title(BOOKSTORE_TITLE)
root.configure(bg=BACKGROUND_COLOR) # Assign root beige color
root.attributes("-fullscreen", True) # Enable fullscreen

main_page = MainPage(root).mainloop() # Instantiate and run main page