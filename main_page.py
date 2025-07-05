import tkinter as tk

# Constants
BACKGROUND_COLOR = "#f5f5dc" # Beige
BOOKSTORE_TITLE = "Flourishing Blotts"
RIGHT = tk.RIGHT

class MainPage(tk.Frame):
    def __init__(self, root=None, background_color=BACKGROUND_COLOR, font_name="Cambria", page_title=BOOKSTORE_TITLE):
        super().__init__(root)
        self.configure(bg=background_color) # Assign window beige color
        self.pack()
        self.create_widgets(background_color, font_name, page_title)

    def create_widgets(self, background_color, font_name, bookstore_title):
        # Create, style, and place exit button
        tk.Button(self, text="Quit", font=(font_name, 15), command=self.quit).pack(side=RIGHT, padx=20, pady=20)

        # Create and position page title
        self.page_title = tk.Label(self, text=bookstore_title, font=(font_name, 40))
        self.page_title.config(bg=background_color)
        self.page_title.pack(pady=100)


# Define root window
root = tk.Tk()
root.title(BOOKSTORE_TITLE)
root.configure(bg=BACKGROUND_COLOR) # Assign root beige color
root.attributes("-fullscreen", True) # Enable fullscreen

MainPage(root).mainloop() # Instantiate and run main page