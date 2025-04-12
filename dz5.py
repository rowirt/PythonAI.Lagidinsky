class Door:
    pass

class HouseOne:
    def __init__(self):
        self.door = Door()

class HouseTwo(HouseOne):
    def __init__(self):
        super().__init__()
        self.windows = None

class HouseThree(HouseTwo):
    def __init__(self):
        super().__init__()
        self.roof = None

house1 = HouseOne()
house2 = HouseTwo()
house3 = HouseThree()

