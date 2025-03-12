class WorldState:

    def __init__(self, monkey_location, banana_location, box_location):
        self.monkey_location = monkey_location
        self.monkey_level = 0
        self.has_banana = False
        self.banana_location = banana_location
        self.box_location = box_location
    
    def __str__(self):
        return "Monkey is at " + str(self.monkey_location) + " and the banana is at " + str(self.banana_location) + " and the box is at " + str(self.box_location)
    
    