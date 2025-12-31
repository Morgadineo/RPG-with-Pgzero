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

class Door(Floor):
    def __init__(self, id: str, name: str):

        super().__init__(id, name)

class SpawnDoor(Door):

    def __init__(self, id: str, name: str):
        super().__init__(id, name)

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
    "22": SpawnDoor("22", "tile_0022"),
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
    "64": Wall("64",  "tile_0064"),
    "65": Wall("65",  "tile_0065"),
    "66": Floor("66",  "tile_0066"),
    "67": Wall("67",  "tile_0067"),
    "68": Wall("68",  "tile_0068"),
    "69": Wall("69",  "tile_0069"),
    "70": Wall("70",  "tile_0070"),
    "71": Wall("71",  "tile_0071"),
    "72": Wall("72",  "tile_0072"),
    "73": Wall("73",  "tile_0073"),
    "74": Wall("74",  "tile_0074"),
    "75": Wall("75",  "tile_0075"),
    "76": Wall("76",  "tile_0076"),
    "77": Wall("77",  "tile_0077"),
    "78": Wall("78",  "tile_0078"),
    "79": Wall("79",  "tile_0079"),
    "80": Wall("80",  "tile_0080"),
    "81": Wall("81",  "tile_0081"),
    "82": Wall("82",  "tile_0082"),
    "83": Wall("83",  "tile_0083"),
    "84": Floor("84",  "tile_0084"),
    "85": Floor("85",  "tile_0085"),
    "86": Floor("86",  "tile_0086"),
    "87": Floor("87",  "tile_0087"),
    "88": Floor("88",  "tile_0088"),
    "89": Wall("89",  "tile_0089"),
    "90": Wall("90",  "tile_0090"),
    "91": Wall("91",  "tile_0091"),
    "92": Wall("92",  "tile_0092"),
    "93": Wall("93",  "tile_0093"),
    "94": Wall("94",  "tile_0094"),
    "95": Wall("95",  "tile_0095"),
    "96": Floor("96",  "tile_0096"),
    "97": Floor("97",  "tile_0097"),
    "98": Floor("98",  "tile_0098"),
    "99": Floor("99",  "tile_0099"),
    "100": Floor("100", "tile_0100"),
    "101": Floor("101", "tile_0101"),
    "102": Floor("102", "tile_0102"),
    "103": Floor("103", "tile_0103"),
    "104": Floor("104", "tile_0104"),
    "105": Floor("105", "tile_0105"),
    "106": Floor("106", "tile_0106"),
    "107": Floor("107", "tile_0107"),
    "108": Floor("108", "tile_0108"),
    "109": Floor("109", "tile_0109"),
    "110": Floor("110", "tile_0110"),
    "111": Floor("111", "tile_0111"),
    "112": Floor("112", "tile_0112"),
    "113": Floor("113", "tile_0113"),
    "114": Floor("114", "tile_0114"),
    "115": Floor("115", "tile_0115"),
    "116": Floor("116", "tile_0116"),
    "117": Floor("117", "tile_0117"),
    "118": Floor("118", "tile_0118"),
    "119": Floor("119", "tile_0119"),
    "120": Floor("120", "tile_0120"),
    "121": Floor("121", "tile_0121"),
    "122": Floor("122", "tile_0122"),
    "123": Floor("123", "tile_0123"),
    "124": Floor("124", "tile_0124"),
    "125": Floor("125", "tile_0125"),
    "126": Floor("126", "tile_0126"),
    "127": Floor("127", "tile_0127"),
    "128": Floor("128", "tile_0128"),
    "129": Floor("129", "tile_0129"),
    "130": Floor("130", "tile_0130"),
    "131": Floor("131", "tile_0131"),
}

