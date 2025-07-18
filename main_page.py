import random
import tkinter as tk
from operator import indexOf
from tkinter import ttk

from PIL import ImageTk, Image

from books.book_list import book_list

# Constants
BACKGROUND_COLOR = "#f5f5dc" # Beige
BOOKSTORE_TITLE = "Flourishing Blotts"
DEFAULT_FONT = "Cambria"

class MainPage(tk.Frame):
    def __init__(self, root=None, background_color=BACKGROUND_COLOR, font_name=DEFAULT_FONT, page_title=BOOKSTORE_TITLE, button_color="#B0C4DE"):
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

        # Create frame for packing search bar and search button side-by-side
        search_widgets = tk.Frame(self, background=background_color)

        # Create and position search bar
        search_bar = tk.Text(search_widgets, height=2, font=(font_name, 16))
        search_bar.pack(side=tk.LEFT, pady=20)

        # Create and position search button
        search_button = tk.Button(search_widgets, text="Search", bg=button_color, font=(font_name, 15))
        search_button.pack(side=tk.LEFT, padx=5)

        search_widgets.pack()

        self.create_book_widgets(background_color)

    def create_book_widgets(self, background_color):
        # Create and position book catalogue
        book_catalogue = tk.Frame(self)
        book_catalogue.configure(bg=background_color)
        book_catalogue.pack()

        # Create books and add them to the book catalogue frame
        self.image_refs = []  # Maintain a list of books to prevent garbage collection of books after loop terminates
        random.shuffle(book_list) # Shuffle book list so it can be iterated without books appearing in order of genre

        book_row, book_column = 0, 0
        for book_index, book in enumerate(book_list):
            book_cover = Image.open(book.cover_path).resize((252, 380)) # Access book's cover at its specified path
            book_cover = ImageTk.PhotoImage(book_cover)  # Convert cover into a Tk-compatible image
            book_entry = tk.Button(book_catalogue, image=book_cover, bd=0)
            book_entry.grid(row=book_row, column=book_column, padx=10, pady=10)
            self.image_refs.append(book_cover)

            # Update grid position such that there are 5 books per row
            if book_index % 5 == 0 and book_index != 0:
                book_row += 1
                book_column = 0
            elif book_index != 0:
                book_column += 1

# Define root window
root = tk.Tk()
root.title(BOOKSTORE_TITLE)
root.configure(bg=BACKGROUND_COLOR) # Assign root beige color
root.attributes("-fullscreen", True) # Enable fullscreen

MainPage(root) # Instantiate and run main page