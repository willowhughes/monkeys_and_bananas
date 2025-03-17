import random
from Planner import Planner

class Driver:
    """Main driver class for setting up and running the problem."""

    def run(self):
        """Execute the main program.
        
        Gets user input, generates the world, runs the planner,
        and displays the results.
        """
        num_rooms, monkey_start_location, box_start_location, banana_start_location, prob = self.get_user_input()

        adj_matrix = self.generate_adj_matrix(num_rooms, prob)
        for row in adj_matrix:
            print(row)
        
        initial_state = dict(
            monkey_location=monkey_start_location,
            banana_location=banana_start_location,
            box_location=box_start_location,
            monkey_level=0,
            has_banana=0
        )

        # -1 means unknown. Only knowledge of the goal state is has_banana and banana_location
        goal_state = dict(
            monkey_location=-1,
            banana_location=banana_start_location,
            box_location=-1,
            monkey_level=-1,
            has_banana=1
        )

        planner = Planner()
        plan, is_solution = planner.start(initial_state, goal_state, adj_matrix)
        if is_solution:
            print("\nPlan:")
            for action, args in plan:
                print(action.__name__, args)
        else:
            print("\nNo plan found")
        print("\n========================================================")

    def generate_adj_matrix(self, n, prob):
        """Generate a random adjacency matrix for room connections.

        Args:
            n (int): Number of rooms
            prob (float): Probability of a connection between any two rooms

        Returns:
            list: 2D adjacency matrix where 1 indicates a one-way connection
        """
        adj_matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and random.random() < prob:
                    adj_matrix[i][j] = 1
        return adj_matrix

    def get_user_input(self):
        """Get and validate all user input for problem setup.

        Gets number of rooms, starting locations for monkey, box, and banana,
        and probability of room connections.

        Returns:
            tuple: (num_rooms, monkey_start, box_start, banana_start, prob)
                  containing validated input values
        """
        print("========================================================\n")
        while True:
            print("Select the number of rooms:\n==> ", end='')
            num_rooms = int(input())
            if num_rooms < 1:
                print("The number of rooms must be greater than 0")
            else:
                break

        while True:
            print("Select the room the monkey starts in:")
            for i in range(num_rooms):
                    print(f"[{i}] Room {i}")
            print("==> ", end='')
            monkey_start_location = int(input())
            if monkey_start_location < 0 or monkey_start_location >= num_rooms:
                print("The monkey must start in a valid room")
            else:
                break

        while True:
            print("Select the room the box starts in:")
            for i in range(num_rooms):
                print(f"[{i}] Room {i}")
            print("==> ", end='')
            box_start_location = int(input())
            if box_start_location < 0 or box_start_location >= num_rooms:
                print("The box must start in a valid room")
            else:
                break

        while True:
            print("Select the room the bananas starts in:")
            for i in range(num_rooms):
                print(f"[{i}] Room {i}")
            print("==> ", end='')
            banana_start_location = int(input())
            if banana_start_location < 0 or banana_start_location >= num_rooms:
                print("The banana must start in a valid room")
            else:
                break

        while True:
            print("Select the probability of a one way door between rooms (0-1):\n==> ", end='')
            prob = float(input())
            if prob < 0 or prob > 1:
                print("The probability must be between 0 and 1")
            else:
                break

        return num_rooms, monkey_start_location, box_start_location, banana_start_location, prob