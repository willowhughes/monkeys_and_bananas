from Planner import Planner

def main():

    adj_matrix = [[0, 1, 1], 
                  [1, 0, 1], 
                  [1, 1, 0]]
    #initial_state = dict(monkey_location = 'A', monkey_level = "LOW", has_banana = False, banana_location = 'C', box_location = 'B')
    initial_state = dict(monkey_location = 0, monkey_level = "LOW", has_banana = False, banana_location = 2, box_location = 0)

    Planner.start(adj_matrix, initial_state)

def generate_adj_matrix(n, probability):
    pass


if __name__ == '__main__':
    main()