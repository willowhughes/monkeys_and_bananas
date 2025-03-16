from Planner import Planner
from WorldState import WorldState

def main():
    starting_banana_location = 2
    starting_box_location = 0
    starting_monkey_location = 0
    initial_state = dict(monkey_location = starting_monkey_location, banana_location = starting_banana_location, box_location = starting_box_location, monkey_level = 0, has_banana = 0)
    goal_state = dict(monkey_location = -1, banana_location = starting_banana_location, box_location = -1, monkey_level = -1, has_banana = 1)
    # goal_state = dict(monkey_location = 2, banana_location = 2, box_location = 2, monkey_level = 0, has_banana = 0)
    
    planner = Planner()
    planner.start(initial_state, goal_state)

def generate_adj_matrix(n, probability):
    pass

if __name__ == '__main__':
    main()