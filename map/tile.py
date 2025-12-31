from pgzero.actor import Actor

class Tile(Actor):
    
    def __init__(self, id: str, name: str, walkable: bool):
        self.id = id
        self.name = name
        self.walkable = walkable
        self.image_path = f"tiles/{name}"

        super().__init__(self.image_path)

class Wall(Tile):
    
    def __init__(self, id: str, name: str):

        super().__init__(id, name, walkable=False)

class Floor(Tile):
    
    def __init__(self, id: str, name: str):

        super().__init__(id, name, walkable=True)

class SpawnDoor(Tile):

    def __init__(self, id: str, name: str):
        super().__init__(id, name, False)

TILES = {
    "0":  Wall("0",  "tile_0000"),
    "1":  Wall("1",  "tile_0001"),
    "2":  Wall("2",  "tile_0002"),
    "3":  Wall("3",  "tile_0003"),
    "4":  Wall("4",  "tile_0004"),
    "5":  Wall("5",  "tile_0005"),
    "6":  Wall("6",  "tile_0006"),
    "7":  Wall("7",  "tile_0007"),
    "8":  Wall("8",  "tile_0008"),
    "9":  Wall("9",  "tile_0009"),
    "10": Wall("10", "tile_0010"),
    "11": Wall("11", "tile_0011"),
    "12": Wall("12", "tile_0012"),
    "13": Wall("13", "tile_0013"),
    "14": Wall("14", "tile_0014"),
    "15": Wall("15", "tile_0015"),
    "16": Wall("16", "tile_0016"),
    "17": Wall("17", "tile_0017"),
    "18": Wall("18", "tile_0018"),
    "19": Wall("19", "tile_0019"),
    "20": Wall("20", "tile_0020"),
    "21": Floor("21", "tile_0021"),
    "22": Floor("22", "tile_0022"),
    "23": SpawnDoor("23", "tile_0023"),
    "24": Wall("24", "tile_0024"),
    "25": Wall("25", "tile_0025"),
    "26": Wall("26", "tile_0026"),
    "27": Wall("27", "tile_0027"),
    "28": Wall("28", "tile_0028"),
    "29": Wall("29", "tile_0029"),
    "30": Floor("30", "tile_0030"),
    "31": Wall("31", "tile_0031"),
    "32": Wall("32", "tile_0032"),
    "33": Wall("33", "tile_0033"),
    "34": Wall("34", "tile_0034"),
    "35": Wall("35", "tile_0035"),
    "36": Wall("36", "tile_0036"),
    "37": Wall("37", "tile_0037"),
    "38": Wall("38", "tile_0038"),
    "39": Wall("39", "tile_0039"),
    "40": Wall("40", "tile_0040"),
    "41": Floor("41", "tile_0041"),
    "42": Floor("42", "tile_0042"),
    "43": Floor("43", "tile_0043"),
    "44": Floor("44", "tile_0044"),
    "45": Wall("45", "tile_0045"),
    "46": Wall("46", "tile_0046"),
    "47": Wall("47", "tile_0047"),
    "48": Floor("48", "tile_0048"),
    "49": Floor("49", "tile_0049"),
    "50": Floor("50", "tile_0050"),
    "51": Floor("51", "tile_0051"),
    "52": Floor("52", "tile_0052"),
    "53": Floor("53", "tile_0053"),
    "54": Floor("54", "tile_0054"),
    "55": Floor("55", "tile_0055"),
    "56": Floor("56", "tile_0056"),
    "57": Wall("57", "tile_0057"),
    "58": Wall("58", "tile_0058"),
    "59": Wall("59", "tile_0059"),
    "60": Floor("60", "tile_0060"),
    "61": Floor("61", "tile_0061"),
    "62": Floor("62", "tile_0062"),
    "63": Wall("63", "tile_0063"),
}

