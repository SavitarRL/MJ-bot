import random

###########
## Classes
###########


class Game:
    def __init__(self):
        self.players = {"E":Player("E"),"S":Player("S"),"W":Player("W"),"N":Player("N")}
        ## can add more stuff 
        
        self.stick_tiles =[]
        for value in range(1,10):
            for num_stick in range(4):
                self.stick_tiles.append(Tile('s', value))
        
        self.circle_tiles =[]
        for value in range(1,10):
            for num_circle in range(4):
                self.stick_tiles.append(Tile('c', value))
        
        self.million_tiles =[]
        for value in range(1,10):
            for num_mil in range(4):
                self.stick_tiles.append(Tile('m', value))
        
        
        self.word_tiles =[]
        for value in range(1,8):
            for num_word in range(4):
                self.stick_tiles.append(Tile('w', value))

        self.drawable_tiles = self.stick_tiles + self.circle_tiles + self.million_tiles +self.word_tiles

        ## {"tile", number of tiles(136)}
        ## when drawing from drawable_tiles to player_tiles: --> drawable_tile - 1; player_tiles + 1
        ## when player_discard: --> player_tiles - 1; played_tiles + 1
        ### drawable_tiles + played_tiles = 136

        self.played_tiles = []

        ## dict or list??? sld be dict {"tile",number of played tiles(0)}
        ## use list coz more direct 



    def reset(self):
        ## empty player_tiles, put all into drawable
        pass

    def pick_tile(self):
        picked_tile = random.choice(self.drawable_tiles)
        return picked_tile
        ## returns a random/top tile from derawable
        ## use this in deal

    def deal(self,starting_wind): #distributing tiles
        ## deals tiles to 4 players (starting wind has 14, other 13)
        ## if start wind i.e. player at startingwind => 14, else 13
        for i in self.players.values():
            if i.wind == starting_wind:
                for tiles_dis in range(14):
                    self.player_draw(starting_wind)
            else:
                for tiles_dis in range(13):
                    self.player_draw(i.wind)

    ## define starting_wind
    def player_discard(self, player_wind, idx): 
        return 
        pass

    def player_draw(self,player_wind):
        picked_tile = self.pick_tile()
        self.drawable_tiles.remove(picked_tile)
        self.players[player_wind].draw(picked_tile)
        ## player draws a tile from drawable tiles
        ## return picked tile to that player only?
    
    def num_tiles_left(self): ## give number of tiles ***drawable*** left
        return len(self.drawable_tiles)


    def __str__(self):
        bigstring = ""
        for player in self.players.values():
            bigstring += str(player)
            bigstring += "\n"
        return bigstring

# class MyThing: #hash objects if use dict
#     def __init__(self,,location,length):
#         self.name = name
#         self.location = location
#         self.length = length
 
#     def __hash__(self):
#         return hash((self.name, self.location))

#     def __eq__(self, other):
#         return (self.name, self.location) == (other.name, other.location)

#     def __ne__(self, other):
#         # Not strictly necessary, but to avoid having both x==y and x!=y
#         # True at the same time
#         return not(self == other)


# class PlayerAction: #??
#     def __init__(self):
#         self.hand = Hand()
#         self



class Player:
    def __init__(self,wind):
        self.hand = Hand()
        self.wind = wind


    def draw(self, tile):  #should add to self.hand 
        self.hand.add_tile(tile)

    def discard(self, idx): # should remove from self.hand
        return self.hand.remove_tile(idx)
    
    def isDealer(self): #dice and wind
        pass

    def __str__(self):
        return self.wind + "\n" + str(self.hand)
    

class Hand:
    def __init__(self):
        self.tiles = []

    def add_tile(self,tile): ## add tile to self.tiles
        self.tiles.append(tile)

    def remove_tile(self,idx): ## removes tile at idx from self.tiles
        return self.tile.pop(idx)

    def num_tiles(self): ##return number of tiles in hand
        return len(self.tiles)


    def __str__(self):
        idx_string = ""
        tile_string = ""
        count = 0
        for tile in self.tiles:
            idx_string += "  {}  |".format(count)
            tile_string += "{:^5}|".format(str(tile))
            count+=1
        return idx_string + "\n" + tile_string
    



class Tile:
    """ 
    Attributes:
    
    Methods:
    """

    def __init__(self, type, value):
        """
        Parameters:
        -------------
        type : str
            stick (s), circle (c), million(m), words(w)

        value: int
            normal: 1-9
            words: 1:east, 2:south, 3:west, 4:north, 5:mid, 6:fat, 7:white
        """
        super().__init__() #inherit
        if type not in ["s", "c", "m", "w"]:
            raise Exception("No such Mahjong type, got {}".format(self.type))
        self.type = type
        self.value = value
        self.word_dict = {1:"east", 2:"south", 3: "west", 4: "north", 5:"mid", 6:"fat",7: "white"}
        if type != "w":
            if value >9 or value <1:
                raise Exception("Value not in range")
        else:
            if value >7 or value <1:
                raise Exception("Value not in range")


    def __str__(self): 
        if self.type == "w":
            return self.word_dict[self.value]
        else:
            return "{}{}".format(self.value, self.type)

    
    def isWind(self): #identifying wind tiles 
        if self.type == "w":
            if self.value < 5:
                return True  
        return False

    def isDragon(self): #identifying dragon tiles
        if self.type == "w":
            if self.value > 4:
                return True
        return False
        

    def __eq__(self, other):
        if self.type == other.type and self.value == other.value:
            return True
        else:
            return False



    
