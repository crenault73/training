# Jeu de taquin

from tkinter import *
from PIL import Image, ImageTk
import random
import copy


class My15PuzzleApp:
    # Tableau contenant les tuiles
    tiles = [[None] * 4 for i in range(4)]

    def __init__(self):
        self.window = Tk()
        self.window.title("Jeu de Taquin")
        self.window.iconbitmap("images/15puzzle.ico")
        self.window.config(background="white")
        self.window.resizable(False,False)
        # self.window.geometry(str(600) + "x" + str(600))
        self.meal_suggestion = ""

        # Initialization des composants
        self.frame = Frame(self.window, bg='white')

        # Création des composants
        # self.create_elements()
        self.create_canvas()
        self.split_image_into_tiles()
        #self.display_tiles()
        self.shuffle_tiles()
        self.display_tiles()


        # Empaquetage
        self.frame.pack(expand=YES)

    def create_canvas(self):
        # Creation d'image
        self.im = Image.open("images/tigers-3-1394809-639x639.png")
        w, h = self.im.size
        self.im = self.im.resize([int(w / 2), int(h / 2)])
        w, h = self.im.size

        self.image = ImageTk.PhotoImage(self.im)

        self.canvas = Canvas(self.frame, width=w, height=h, bg="#4065A4", bd=0,
                             highlightthickness=0)
        self.canvas.create_image(w / 2, h / 2, image=self.image)
        self.window.geometry(str(w) + "x" + str(h))
        self.canvas.pack(expand=YES)

    # Creation et indexation des tuiles
    def split_image_into_tiles(self):
        w, h = self.im.size
        print("Size:", self.im.size)
        n = 0
        for i in range(0, 4):
            for j in range(0, 4):
                # cropped = self.im.crop((0, 0, 200, 200))
                print("img", i, j, "coords:", i * int(w / 4), j * int(w / 4)
                      , (i * int(w / 4)) + int(w / 4), (j * int(w / 4)) + int(w / 4))
                tile = Tile(n, self.im.crop(
                    (i * int(w / 4), j * int(w / 4), (i * int(w / 4)) + int(w / 4), (j * int(w / 4)) + int(w / 4))))
                n += 1
                self.tiles[i][j] = tile
        print("Tiles:", self.tiles)

    # Affichage des tuiles
    def display_tiles(self):
        w, h = self.im.size
        new_im = Image.new('RGB', (w, h), (255, 255, 255))
        offset=1
        for i in range(0, 4):
            for j in range(0, 4):
                print("Image_cropped size: " + str(self.tiles[i][j].img.width) + "/" + str(self.tiles[i][j].img.height))
                print("Tile N°:", self.tiles[i][j].n)
                new_im.paste(self.tiles[i][j].img, (i * int(offset+w / 4), j * int(offset+w / 4)))
        self.image = ImageTk.PhotoImage(new_im)
        self.canvas.create_image(w / 2, h / 2, image=self.image)
        self.canvas.pack(expand=YES)

    #
    def shuffle_tiles(self):
        tmp = copy.deepcopy(self.tiles)
        # tmp = self.tiles
        # Liste des tuiles en desordre
        l = random.sample(range(0, 16), 16)
        print("L:", l)
        n = 0
        for i in range(0, 4):
            for j in range(0, 4):
                idx = l[i + 4 * j]
                i2 = int(idx / 4)
                j2 = int(idx % 4)
                print("i,j:", i, j, "l[", n, "]", idx, ", 4*i+j:", 4 * i + j, " - [", i2, ",", j2, "]", "Tile N:",
                      tmp[i][j].n, ", TileTmp N:", tmp[i2][j2].n)
                self.tiles[i][j] = tmp[i2][j2]
                n += 1


class Tile:
    def __init__(self, n, img):
        self.n = n
        self.img = img


# Afficher
app = My15PuzzleApp()
app.window.mainloop()
