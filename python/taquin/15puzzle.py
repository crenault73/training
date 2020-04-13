# 15puzzle

from tkinter import *
from tkinter import filedialog
import os, os.path
from PIL import Image as PilImage, ImageTk
from grid import Grid


class My15PuzzleApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("15puzzle")
        #self.window.iconbitmap("images/15puzzle.ico")
        self.window.config(background="white")
        self.window.resizable(False,False)

        # Components initialisation
        self.frame = Frame(self.window, bg='white')

        # Loading default image
        self.im = PilImage.open("images/my-puppy-maggie-1362787-1280x1280.png")
        w, h = self.im.size
        self.im = self.im.resize([int(w / 2), int(h / 2)])
        w, h = self.im.size
        self.create_canvas()

        # Packing
        self.frame.pack(expand=YES)

        # Menu bar creation
        menu_bar = Menu(self.window)
        # File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_grid)
        file_menu.add_command(label="Quit", command=self.window.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Adding menu bar to the window
        self.window.config(menu=menu_bar)
        self.window.geometry(str(w) + "x" + str(h + 22))

    def click_on_tile(self, evt):
        # print('Click down in:', evt)
        pos = self.grid.get_position_by_mouse_box(evt.x, evt.y)
        # print('Pos:', pos)
        self.grid.move_tile(pos)
        new_im = self.grid.get_image_tiles()
        self.image = ImageTk.PhotoImage(new_im)
        w, h = self.im.size
        self.canvas.create_image(w / 2, h / 2, image=self.image)

        if self.grid.is_solved():
            print("Victory!")

    def new_grid(self):
        self.window.filename = filedialog.askopenfilename(initialdir="images", title="Select file",
                                                          filetypes=(("png files", "*.png"), ("all files", "*.*")))

        if self.window.filename is "": return

        self.im = PilImage.open(self.window.filename)
        w, h = self.im.size
        self.im = self.im.resize([int(w / 2), int(h / 2)])
        w, h = self.im.size

        self.grid = Grid(self.im)
        new_im = self.grid.get_image_tiles()
        self.image = ImageTk.PhotoImage(new_im)
        w, h = self.im.size
        self.canvas.create_image(w / 2, h / 2, image=self.image)
        self.window.geometry(str(w) + "x" + str(h))

    def create_canvas(self):
        self.grid = Grid(self.im)
        # print(self.grid)
        w, h = self.im.size
        new_im = self.grid.get_image_tiles()
        self.image = ImageTk.PhotoImage(new_im)
        self.canvas = Canvas(self.frame, width=w, height=h, bg="#4065A4", bd=0, highlightthickness=0)
        self.canvas.create_image(w / 2, h / 2, image=self.image)
        self.canvas.bind('<Button-1>', self.click_on_tile)
        self.canvas.pack(expand=YES)


# Display
app = My15PuzzleApp()
app.window.mainloop()
