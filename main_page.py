import random
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

from books.book_list import book_list

# Constants
BEIGE = "#f5f5dc" # Beige
BOOKSTORE_TITLE = "Flourishing Blotts"
DEFAULT_FONT = "Cambria"
SEARCH_ICON_PATH = "images/search_icon.png"
EXIT_IMAGE_PATH = "images/exit_cropped.png"

class MainPage(tk.Frame):
    def __init__(self, root=None, background_color=BEIGE, font_name=DEFAULT_FONT, page_title=BOOKSTORE_TITLE):
        super().__init__(root) # Create frame in root window

        # Instance variables
        self.background_color = background_color
        self.font_name = font_name
        self.page_title = page_title
        self.images = []  # Book cover list to prevent garbage collection

        self.configure(bg=background_color)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_canvas() # Enable scroll
        self.create_widgets()

    def create_widgets(self):
        # Quit button
        self.exit_image = Image.open(EXIT_IMAGE_PATH).resize((50, 25))
        self.exit_image = ImageTk.PhotoImage(self.exit_image)
        tk.Button(self.canvas_frame, image=self.exit_image, command=self.quit).pack(padx=40, pady=25, anchor=tk.E)

        # Page title
        self.page_title = tk.Label(self.canvas_frame, text=self.page_title, font=(self.font_name, 100))
        self.page_title.config(bg=self.background_color)
        self.page_title.pack(pady=100)

        self.search_bar() # Search bar and search button
        self.create_books()

    def create_books(self):
        book_catalogue = tk.Frame(self.canvas_frame)
        book_catalogue.configure(bg=self.background_color)
        book_catalogue.pack()

        # Draw books
        random.shuffle(book_list) # Shuffle book list so it can be iterated without books appearing in order
        book_row, book_column = 0, 0
        for book_index, book in enumerate(book_list[0:30]):
            book_cover = Image.open(book.cover_path).resize((252, 380)) # Retrieve book cover from path
            book_cover = ImageTk.PhotoImage(book_cover)  # Convert cover into a Tk-compatible image
            book_entry = tk.Button(book_catalogue, image=book_cover, bd=0)
            book_entry.grid(row=book_row, column=book_column, padx=10, pady=10)
            self.images.append(book_cover)

            # Update grid position such that there are 5 books per row
            if book_index % 5 == 0 and book_index != 0:
                book_row += 1
                book_column = 0
            elif book_index != 0:
                book_column += 1

    def create_canvas(self):
        # Canvas and scrollbar
        canvas = tk.Canvas(self, bg=self.background_color)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.canvas_frame = tk.Frame(canvas, bg=self.background_color)

        # I wish I could use a an expand/fill type of strategy here, but idk how so i just passed bg color to everything
        # Additionally, I think this is what I'll need to look at if I want to improve the logic for centering the content, though that's decent for now
        # ALSO, I'd like the quit button to be in the actual far right corner of the screen
        canvas.create_window((250, 0), window=self.canvas_frame, anchor=tk.NW)

    def search_bar(self):
        search_widgets = tk.Frame(self.canvas_frame, background=self.background_color)

        # Search bar
        tk.Entry(search_widgets, font=(self.font_name, 16), width=50).pack(side=tk.LEFT, pady=20, ipadx=20, ipady=20)

        # Search button
        self.search_icon = Image.open(SEARCH_ICON_PATH).resize((65, 66))
        self.search_icon = ImageTk.PhotoImage(self.search_icon)
        tk.Button(search_widgets, image=self.search_icon, bd=0).pack(side=tk.LEFT)

        search_widgets.pack()

# Define root window
root = tk.Tk()
root.title(BOOKSTORE_TITLE)
root.attributes("-fullscreen", True) # Enable fullscreen

MainPage(root).mainloop() # Instantiate and run main page