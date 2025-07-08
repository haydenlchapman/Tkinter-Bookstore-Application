import tkinter as tk
import random

from PIL import ImageTk, Image

from books.book_list import book_list

# Constants
BACKGROUND_COLOR = "#f5f5dc" # Beige
BOOKSTORE_TITLE = "Flourishing Blotts"

class MainPage(tk.Frame):
    def __init__(self, root=None, background_color=BACKGROUND_COLOR, font_name="Cambria", page_title=BOOKSTORE_TITLE, button_color="#B0C4DE"):
        super().__init__(root) # Create our frame in the root window
        self.configure(bg=background_color)
        self.pack(fill=tk.X)
        self.create_widgets(button_color, background_color, font_name, page_title)
        self.mainloop() # Run page

    def create_widgets(self, button_color, background_color, font_name, page_title):
        # Create, style, and pack quit button
        tk.Button(self, text="Quit", font=(font_name, 15), bg=button_color, command=self.quit).pack(padx=40, pady=25, anchor=tk.E)

        # Create and position page title
        self.page_title = tk.Label(self, text=page_title, font=(font_name, 40))
        self.page_title.config(bg=background_color)
        self.page_title.pack(pady=100)

        # Create and pack book catalogue
        book_catalogue = tk.Frame(self)
        book_catalogue.pack()

        # Shuffle book list and use grid to add them into the catalogue in order; this can be a method later
        random.shuffle(book_list)
        for book in book_list:
            pass # Should add books to catalogue; not sure exactly how to do that yet

        book_catalogue.configure(bg=background_color)
        book_button = tk.Button(book_catalogue, text="Hello,World!", font=("Cambria", 16))
        book_button.pack()

# Define root window
root = tk.Tk()
root.title(BOOKSTORE_TITLE)
root.configure(bg=BACKGROUND_COLOR) # Assign root beige color
root.attributes("-fullscreen", True) # Enable fullscreen

MainPage(root) # Instantiate and run main page