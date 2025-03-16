from Operators import ClimbUp, Move, Push, Grab, ClimbDown

class Planner:

    adj_matrix = [[0, 1, 1], 
                  [1, 0, 1], 
                  [1, 1, 0]]

    def start(self, initial_state, goal_state):
        print("Initial state: ", initial_state)
        print()
        print(self.get_actions(initial_state))
        print()
        print(self.get_backwards_actions(goal_state))
        print()
        print("Goal state: ", goal_state)
        next = Grab.get_pre(goal_state)
        print(next)
        print(self.get_backwards_actions(next))
        next = ClimbUp.get_pre(next)
        print(next)
        print(self.get_backwards_actions(next))

        # plan, is_solution = self.get_plan(initial_state, goal_state, [], [])
    '''
    # dfs brute force 
    def get_plan(self, inital_state, goal_state, plan, prev_states):
        if inital_state == goal_state:
            return plan, True # success
        
        actions = self.get_actions(goal_state)
        # actions is a list of ordered pairs where [0] is the action and [1] is the arguments to that action
        # how do I store the action and the args?
        if not actions:
            return plan, False
        
        for action, args in actions:
            if len(args) == 0: # For ClimbUp, ClimbDown, and Grab which take only state
                new_goal_state = action.get_post(goal_state)
            else: # For Move and Push which take state and room arguments
                new_goal_state = action.get_post(goal_state, *args)
            
            plan, is_solution = self.get_plan(inital_state, new_goal_state, plan.deepcopy().append(action, args), prev_states)
            if is_solution:
                return plan, True

        return plan, False
    '''

    

    def get_actions(self, state):
        actions = []
        if ClimbUp.check_pre(state):
            actions.append([ClimbUp, []])
        if ClimbDown.check_pre(state):
            actions.append([ClimbDown, []])
        if Grab.check_pre(state):
            actions.append([Grab, []])
        for i in range(len(Planner.adj_matrix)):
            for j in range(len(Planner.adj_matrix[i])):
                if Planner.adj_matrix[i][j] == 1:
                    if Move.check_pre(state, i):
                        # print("move ", i, "->", j)
                        actions.append([Move, i, j])
                    if Push.check_pre(state, i):
                        # print("move ", i, "->", j)
                        actions.append([Push, i, j])

        return actions
    
    def get_backwards_actions(self, state):
        actions = []
        # Check if grab could have been the last action
        if Grab.check_post(state):
            actions.append([Grab, []]) 
        # Check if climb up could have been the last action
        if ClimbUp.check_post(state):
            actions.append([ClimbUp, []]) 
        # Check if climb down could have been the last action
        if ClimbDown.check_post(state):
            actions.append([ClimbDown, []])
        # For Move and Push, we need to check connections between rooms
        for i in range(len(Planner.adj_matrix)):
            for j in range(len(Planner.adj_matrix[i])):
                if Planner.adj_matrix[i][j] == 1:
                    if Move.check_pre(state, j):
                        # print("move ", i, "<-", j)
                        actions.append([Move, i, j])
                    if Push.check_pre(state, j):
                        # print("move ", i, "<-", j)
                        actions.append([Push, i, j])
        
        return actions


    def print_state(state):
        print("Monkey location: " + str(state["monkey_location"]) 
              + "\nBanana location: " + str(state["banana_location"]) 
              + "\nBox location: " + str(state["box_location"] 
              + "\nMonkey level " + str(state["monkey_level"]) 
              + "\nHas banana?: " + str(state["has_banana"])))