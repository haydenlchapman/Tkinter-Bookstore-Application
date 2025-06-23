import tkinter as tk

# Constants
BACKGROUND_COLOR = "#f5f5dc" # Beige
BOOKSTORE_TITLE = "Flourishing Blotts"
#consider making const var for cambria

class MainPage(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.configure(bg=BACKGROUND_COLOR) # Assign window beige color
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create, style, and place exit button
        tk.Button(self, text="Quit", font=("Cambria", 15), command=self.quit).grid(row=0, column=2, pady=(20, 20), padx=20)

        # Create and position page title
        self.page_title = tk.Label(self, text=BOOKSTORE_TITLE, font=("Cambria", 40))
        self.page_title.config(bg="#00ffff")
        self.page_title.grid(row=1, column=1, pady=(100, 20), padx=20)


# Define root window
root = tk.Tk()
root.title(BOOKSTORE_TITLE)
root.configure(bg=BACKGROUND_COLOR) # Assign root beige color
root.attributes("-fullscreen", True) # Enable fullscreen

MainPage(root).mainloop() # Instantiate and run main page