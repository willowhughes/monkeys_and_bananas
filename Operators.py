import copy


class Move:

    def check_pre(state, room_a, room_b):
        return state['monkey_location'] == room_a and canMoveTo(room_a, room_b) and state['monkey_level'] == "LOW" 

    def get_post(state, room_a, room_b):
        new_state = copy.deepcopy(state)
        new_state['monkey_location'] = room_b
        return new_state
    
class Push:

    def check_pre(state, room_a, room_b):
        return state['monkey_location'] == room_a and canMoveTo(room_a, room_b) and state['monkey_level'] == "LOW" and state['box_location'] == room_a
    
    def get_post(state, room_a, room_b):
        new_state = copy.deepcopy(state)
        new_state['monkey_location'] = room_b
        new_state['box_location'] = room_b
        return new_state

class ClimbUp:
     
    def check_pre(state):
        return state['monkey_location'] == state['box_location'] and state['monkey_level'] == "LOW"
    
    def get_post(state):
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = "HIGH"
        return new_state

class ClimbDown:

    def check_pre(state):
        return state['monkey_location'] == state['box_location'] and state['monkey_level'] == "HIGH"
    
    def get_post(state):
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = "LOW"
        return new_state
    
class Grab:

    def check_pre(state):
        return state['monkey_location'] == state['banana_location'] and state['monkey_level'] == "HIGH"
    
    def get_post(state):
        new_state = copy.deepcopy(state)
        new_state['has_banana'] = True
        return new_state