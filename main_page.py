import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.media_label = tk.Label(self, text="Flourishing Blotts")
        self.media_label.config(bg="#00ffff")
        self.media_label.grid()
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid()

root = tk.Tk()
root.title("Flourishing Blotts")
main_page = MainPage(root)
main_page.mainloop()