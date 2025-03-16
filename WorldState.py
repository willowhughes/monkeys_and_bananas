class WorldState:

    state = dict()

    def __init__(self, monkey_location, banana_location, box_location, monkey_level, has_banana):
        self.state["monkey_location"] = monkey_location
        self.state["banana_location"] = banana_location
        self.state["box_location"] = box_location
        self.state["monkey_level"] = monkey_level
        self.state["has_banana"] = has_banana
    
    def copy(self):
        return WorldState(self.state["monkey_location"], self.state["banana_location"], self.state["box_location"], self.state["monkey_level"], self.state["has_banana"])

    def __str__(self):
        return "Monkey is at " + str(self.monkey_location) + " and the banana is at " + str(self.banana_location) + " and the box is at " + str(self.box_location)
    
    