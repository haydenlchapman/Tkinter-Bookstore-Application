import tkinter as tk
import random

import main_page # For accessing constants

class Book():
    def __init__(self, title, genre, author, year, publisher, cover_path):
        self.title = title
        self.genre = genre
        self.author = author
        self.year = year
        self.publisher = publisher
        self.cover_path = cover_path