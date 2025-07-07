import tkinter as tk

# Constants
BACKGROUND_COLOR = "#f5f5dc" # Beige
BOOKSTORE_TITLE = "Flourishing Blotts"

class MainPage(tk.Frame):
    def __init__(self, root=None, background_color=BACKGROUND_COLOR, font_name="Cambria", page_title=BOOKSTORE_TITLE):
        super().__init__(root) # Create our frame in the root window
        self.configure(bg=background_color)
        self.pack(fill=tk.X)
        self.create_widgets(background_color, font_name, page_title)
        self.mainloop() # Run page

    def create_widgets(self, background_color, font_name, page_title):
        # Create, style, and pack quit button
        tk.Button(self, text="Quit", font=(font_name, 15), command=self.quit).pack(padx=40, pady=25, anchor=tk.E)

        # Create and position page title
        self.page_title = tk.Label(self, text=page_title, font=(font_name, 40))
        self.page_title.config(bg=background_color)
        self.page_title.pack(pady=100)

# Define root window
root = tk.Tk()
root.title(BOOKSTORE_TITLE)
root.configure(bg=BACKGROUND_COLOR) # Assign root beige color
root.attributes("-fullscreen", True) # Enable fullscreen

MainPage(root) # Instantiate and run main page