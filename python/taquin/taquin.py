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
        self.window.resizable(False, False)
        # self.window.geometry(str(600) + "x" + str(600))
        self.meal_suggestion = ""

        # Initialization des composants
        self.frame = Frame(self.window, bg='white')

        # Création des composants
        # self.create_elements()s
        self.create_canvas()
        self.split_image_into_tiles()
        # self.display_tiles()
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
        self.canvas.bind('<Button-1>', self.click_on_tile)
        self.window.geometry(str(w) + "x" + str(h))
        self.canvas.pack(expand=YES)

    def identify_tile_num_by_mouse_coords(self, x, y):
        print("Mouse coords:", x, y)
        w, h = self.im.size
        # tile (i,j)
        i, j = int(x * 4 / w), int(y * 4 / h)
        # tile n
        n = 4 * j + i
        print("(", i, ",", j, ")", "Tile N°:", n)
        return n

    def identify_tile_num_by_tile_coords(self, i, j):
        #print("Tile coords:(", i, j,")")
        # tile (i,j)
        pos = 4 * j + i
        #print("Tile (", i, j, ")", " is pos:", pos)
        return pos

    def identify_tile_coords_by_pos(self, pos):
        w, h = self.im.size
        # tile pos
        i = int(pos % 4)
        j = int(pos / 4)
        # tile (i,j)
        #print("Tile coords:", i, j)
        return i, j

    def log_tiles(self):
        for j in range(0, 4):
            for i in range(0, 4):
                n = self.identify_tile_num_by_tile_coords(i,j)
                print("Displaying tile pos:", n, "Tile id:",self.tiles[i][j].id)

    def swap_tiles(self, n, m):
        #self.log_tiles()

        i1, j1 = self.identify_tile_coords_by_pos(n)
        i2, j2 = self.identify_tile_coords_by_pos(m)

        tmp1 = copy.deepcopy(self.tiles[i1][j1])
        tmp2 = copy.deepcopy(self.tiles[i2][j2])

        self.tiles[i1][j1] = tmp2
        self.tiles[i2][j2] = tmp1

        #self.log_tiles()

    def move_tile(self, n):
        i, j = self.identify_tile_coords_by_pos(n)
        print("self.tiles[i][j].img: ", self.tiles[i][j].img)
        # Bouge la tuile s'il existe une tuile vide à côté
        # identifie la tuile vide connexe
        if (self.tiles[i][j].img is not None):
            m = self.find_near_empty_tile_pos(n)
            if m>=0:
                print("Empty tile found:", m)
                self.swap_tiles(n,m)
        else:
            print("Empty tile can't move :(", i, ",", j, ")")

    def find_near_empty_tile_pos(self, n):
        i, j = self.identify_tile_coords_by_pos(n)
        #print("Search for tiles near Tile: (",i,j,")")
        m = -1
        if i-1 >= 0:
            #print("Case i-1>=0")
            if self.tiles[i-1][j].img is None: m=n-1
        if i+1 < 4:
            #print("Case i+1<4")
            if self.tiles[i+1][j].img is None: m=n+1
        if j-1 >= 0:
            #print("Case j-1>=0")
            if self.tiles[i][j-1].img is None: m=n-4
        if j+1 < 4:
            #print("Case j+1<4")
            if self.tiles[i][j+1].img is None: m=n+4
        # si aucune tuille nulle trouvé
        return m

    def click_on_tile(self, evt):
        print('Click down in:', evt)
        n = self.identify_tile_num_by_mouse_coords(evt.x, evt.y)
        self.move_tile(n)
        self.display_tiles()

    # Creation et indexation des tuiles
    def split_image_into_tiles(self):
        w, h = self.im.size
        print("Size:", self.im.size)
        id = 0
        for j in range(0, 4):
            for i in range(0, 4):
                # cropped = self.im.crop((0, 0, 200, 200))
                # print("img", i, j, "coords:", i * int(w / 4), j * int(w / 4) , (i * int(w / 4)) + int(w / 4), (j * int(w / 4)) + int(w / 4))
                if (i == 3 and j == 0):
                    tile = Tile(id, None)
                else:
                    tile = Tile(id, self.im.crop(
                        (i * int(w / 4), j * int(w / 4), (i * int(w / 4)) + int(w / 4), (j * int(w / 4)) + int(w / 4))))
                id += 1
                self.tiles[i][j] = tile
        print("Tiles:", self.tiles)

    # Affichage des tuiles
    def display_tiles(self):
        w, h = self.im.size
        new_im = Image.new('RGB', (w, h), (255, 255, 255))
        offset = 1
        for j in range(0, 4):
            for i in range(0, 4):
                n = self.identify_tile_num_by_tile_coords(i,j)
                #print("Displaying tile:", n)
                if (self.tiles[i][j].img is not None):
                    #print("Image_cropped size: " + str(self.tiles[i][j].img.width) + "/" + str( self.tiles[i][j].img.height))
                    new_im.paste(self.tiles[i][j].img, (i * int(offset + w / 4), j * int(offset + w / 4)))
                    #print("Tile id:", self.tiles[i][j].id)
                else:
                    #print("Do not display Empty Tile N°:", n)
                    k=0
            self.image = ImageTk.PhotoImage(new_im)
        self.canvas.create_image(w / 2, h / 2, image=self.image)
        self.canvas.pack(expand=YES)

    # Mélange l'ensemble des tuiles
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
                print("i,j:", i, j, "l[", n, "]", idx, ", 4*i+j:", 4 * i + j, " - [", i2, ",", j2, "]", "Tile id:",
                      tmp[i][j].id, ", TileTmp id:", tmp[i2][j2].id)
                self.tiles[i][j] = tmp[i2][j2]
                n += 1


class Tile:
    def __init__(self, id, img):
        self.id = id
        self.img = img

# Afficher
app = My15PuzzleApp()
app.window.mainloop()
