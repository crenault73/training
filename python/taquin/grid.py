from PIL import Image
import copy
import random


class Grid:
    # 2D Array containing the tiles
    tiles = [[None] * 4 for i in range(4)]

    def __init__(self, image):
        self.image = image
        self.split_image_into_tiles(image)
        # list=[13,6,7,10,8,9,11,0,15,2,12,5,14,3,1,4]
        # self.arrange_tiles(list)
        self.shuffle_tiles()
        countReshuffles = 0
        while self.isSolvable() is not True:
            self.shuffle_tiles()
            countReshuffles += 1
            #print("Number of Re-Shuffles :", countReshuffles)

    def __str__(self):
        str_tiles = ""
        pos = 0
        for j in range(0, 4):
            for i in range(0, 4):
                str_tiles += ",[id:" + str(self.tiles[i][j].id) + ",pos:" + str(pos) + "]"
                if i % 4 == 3: str_tiles += "\n"
                pos += 1
        str_tiles = str_tiles[1:]
        str_tiles = "[" + str_tiles[:-1] + "]"
        return str_tiles

    def find_near_blank_tile_position(self, pos):
        i, j = self.get_coords_by_position(pos)
        # print("Search for tiles near Tile: (",i,j,")")
        m = -1
        if i - 1 >= 0:
            # print("Case i-1>=0")
            if self.tiles[i - 1][j].img is None: m = pos - 1
        if i + 1 < 4:
            # print("Case i+1<4")
            if self.tiles[i + 1][j].img is None: m = pos + 1
        if j - 1 >= 0:
            # print("Case j-1>=0")
            if self.tiles[i][j - 1].img is None: m = pos - 4
        if j + 1 < 4:
            # print("Case j+1<4")
            if self.tiles[i][j + 1].img is None: m = pos + 4
        return m

    def get_coords_by_position(self, pos):
        i = int(pos % 4)
        j = int(pos / 4)
        return i, j

    def get_position_by_coords(self, i, j):
        pos = 4 * j + i
        return pos

    def get_position_by_mouse_box(self, x, y):
        # print("Mouse coords:", x, y)
        w, h = self.image.size
        # tile (i,j)
        i, j = int(x * 4 / w), int(y * 4 / h)
        # tile pos
        pos = 4 * j + i
        # print("(", i, ",", j, ")", "Tile N°:", n)
        return pos

    def get_image_tiles(self):
        w, h = self.image.size
        tiles_im = Image.new('RGB', (w, h), (250, 250, 250))
        offset = 1
        for j in range(0, 4):
            for i in range(0, 4):
                # print("Displaying tile:", i, j)
                pos = self.get_position_by_coords(i, j)
                # print("Displaying tile:", n)
                if (self.tiles[i][j].img is not None):
                    # print("Image_cropped size: " + str(self.tiles[i][j].img.width) + "/" + str( self.tiles[i][j].img.height))
                    tiles_im.paste(self.tiles[i][j].img, (i * int(offset + w / 4), j * int(offset + w / 4)))
                    # print("Tile id:", self.tiles[i][j].id)
                else:
                    # print("Do not display Empty Tile N°:", pos)
                    k = 0
        return tiles_im

    def move_tile(self, pos):
        i, j = self.get_coords_by_position(pos)
        # Move the current tile in place of the blank tile if close to
        if (self.tiles[i][j].id != 0):
            pos_blank_tile = self.find_near_blank_tile_position(pos)
            if pos_blank_tile >= 0:
                # print("Empty tile found:", pos_blank_tile)
                self.swap_tiles_by_positions(pos, pos_blank_tile)
        else:
            k = -1
            # print("Blank tile can't be moved")

    # Cut the image into Tiles
    def split_image_into_tiles(self, image):
        w, h = self.image.size
        # ("Size:", self.image.size)
        id = 0
        for j in range(0, 4):
            for i in range(0, 4):
                # (i=0,j=0) are the coordinates of the blank tile
                if (i == 0 and j == 0):
                    tile = Tile(id, None)
                else:
                    tile = Tile(id, self.image.crop(
                        (i * int(w / 4), j * int(w / 4), (i * int(w / 4)) + int(w / 4), (j * int(w / 4)) + int(w / 4))))
                id += 1
                self.tiles[i][j] = tile

    def shuffle_tiles(self):
        tmp_tiles = copy.deepcopy(self.tiles)
        # Generate random positions in the grid from 0 to 15
        rand_pos = random.sample(range(0, 16), 16)

        for i in range(0, 4):
            for j in range(0, 4):
                pos = rand_pos[i + 4 * j]
                i2, j2 = self.get_coords_by_position(pos)
                self.tiles[i][j] = tmp_tiles[i2][j2]

    def arrange_tiles(self, pos_list):
        tmp_tiles = copy.deepcopy(self.tiles)
        # Arrange tiles according to the list
        for i in range(0, 4):
            for j in range(0, 4):
                pos = pos_list[i + 4 * j]
                i2, j2 = self.get_coords_by_position(pos)
                self.tiles[i][j] = tmp_tiles[i2][j2]

    def swap_tiles_by_positions(self, pos1, pos2):
        i1, j1 = self.get_coords_by_position(pos1)
        i2, j2 = self.get_coords_by_position(pos2)

        tmp1 = copy.deepcopy(self.tiles[i1][j1])
        tmp2 = copy.deepcopy(self.tiles[i2][j2])

        self.tiles[i1][j1] = tmp2
        self.tiles[i2][j2] = tmp1

    ''' A utility function to count inversions in given array list[] '''

    def getInvCount(self):
        inv_count = 0
        # Put 2D array into a list
        list = []
        for j in range(0, 4):
            for i in range(0, 4):
                list.append(self.tiles[i][j].id)

        # print("list:",list)

        for k in range(0, 15):
            for l in range(k + 1, 16):
                # count pairs(k, l) such that k appears
                # before l, but k > l. (exclude blank tile)
                if (list[k] > list[l] and list[l] != 0):
                    inv_count += 1
        return inv_count

    ''' find Position of blank from bottom of the grid '''

    def findXPosition(self):
        # start from upper corner  corner of matrix
        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                if self.tiles[i][j].img is None:
                    return j + 1

    def isSolvable(self):
        # Count inversions in given puzzle
        invCount = self.getInvCount()
        # print("Nb of inv:", invCount)
        # If grid is odd, return true if inversion
        # count is even.
        if (4 % 2 == 1):  # grid is odd
            # print("Grid is odd")
            return True if invCount % 2 == 0 else False
        else:  # grid is even
            # print("Grid is even")
            xpos = self.findXPosition()
            # print("findXPosition:", xpos)
            if xpos % 2 == 1:
                return False if invCount % 2 == 1 else True
            else:
                return True if invCount % 2 == 1 else False

    def is_solved(self):
        ordered = True
        for j in range(0, 4):
            for i in range(0, 4):
                pos = self.get_position_by_coords(i, j)
                # print("Displaying tile pos:", n, "Tile id:",self.tiles[i][j].id)
                if pos != self.tiles[i][j].id: ordered = False
        return ordered


class Tile:
    def __init__(self, id, img):
        self.id = id
        self.img = img

    def __str__(self):
        return str(self.id) + "," + str(self.img)
