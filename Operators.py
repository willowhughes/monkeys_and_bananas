import copy


class Move:

    # check is monkey is low and in src_room
    def check_pre(state, src_room):
        return state['monkey_location'] == src_room and state['monkey_level'] == 0

    # move monkey to dst_room (can be used for backwards chaining)
    def get_post(state, dst_room):
        new_state = copy.deepcopy(state)
        new_state['monkey_location'] = dst_room
        return new_state
    
class Push:

    # check if monkey is low and monkey_location == box_location
    def check_pre(state, src_room):
        return state['monkey_location'] == src_room and state['monkey_level'] == 0 and state['box_location'] == src_room
    
    # move monkey and box to dst room (can be used for backwards chaining)
    def get_post(state, dst_room):
        new_state = copy.deepcopy(state)
        new_state['monkey_location'] = dst_room
        new_state['box_location'] = dst_room
        return new_state

class ClimbUp:
     
    # check if monkey is low and monkey_location == box_location
    def check_pre(state):
        return state['monkey_location'] == state['box_location'] and state['monkey_level'] == 0
    
    # move monkey to high
    def get_post(state):
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 1
        return new_state
    
    # check if monkey is high (used for backwards chaining)
    def check_post(state):
        return state['monkey_level'] == 1
    
    # move monkey to low (used for backwards chaining)
    def get_pre(state):
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 0
        new_state['box_location'] = state['monkey_location']
        return new_state

class ClimbDown:

    # check if monkey is high and monkey_location == box_location
    def check_pre(state):
        return state['monkey_location'] == state['box_location'] and state['monkey_level'] == 1
    
    # move monkey to low
    def get_post(state):
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 0
        return new_state
    
    # check if monkey is low (used for backwards chaining)
    def check_post(state):
        return state['monkey_level'] == 0
    
    # move monkey to high (used for backwards chaining)
    def get_pre(state):
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 1
        new_state['box_location'] = state['monkey_location']
        return new_state
    
class Grab:

    # check if monkey is high and monkey_location == banana_location
    def check_pre(state):
        return state['monkey_location'] == state['banana_location'] and state['monkey_level'] == 1
    
    # grab banana
    def get_post(state):
        new_state = copy.deepcopy(state)
        new_state['has_banana'] = 1
        return new_state
    
    # check if monkey has banana (used for backwards chaining)
    def check_post(state):
        return state['has_banana'] == 1

    # remove banana (used for backwards chaining)
    def get_pre(state):
        new_state = copy.deepcopy(state)
        new_state['has_banana'] = 0
        new_state['monkey_location'] = state['banana_location']
        new_state['monkey_level'] = 1
        return new_state