from Operators import ClimbUp, Move, Push, Grab, ClimbDown

class Planner:

    # 7 by 7 adjacency matrix
    adj_matrix = [[0, 1, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 1, 0],
                  [0, 0, 1, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 1, 0]]
    # adj_matrix = [[0, 1, 1], 
    #               [1, 0, 1], 
    #               [1, 1, 0]]

    def start(self, initial_state, goal_state):

        plan, is_solution = self.get_backwards_plan(initial_state, goal_state, [], set())
        plan.reverse()
        for action, args in plan:
            print(action.__name__, args)

        # plan, is_solution = self.get_plan(initial_state, goal_state, [], [])

    '''
    get_backwards_plan(self, initial_state, goal_state, plan, prev_states):
        hash the state
        
        if state is in previous states return plan, False
            
        Add current state to visited states
        
        if goal state == inital return plan, True
        
        actions = get backwards actions
        if actions is empty return plan, False
        
        for action_info in actions:
            # Extract action and args based on the format of action_info
            action = action_info[0]
            args = action_info[1:] if len(action_info) > 1 else []
            
            # Use different methods to get precondition based on action type
            if action in [Grab, ClimbUp, ClimbDown]:
                predecessor_state = action.get_pre(goal_state)
            else:  # Move and Push
                predecessor_state = action.get_post(goal_state, args[0])
            
            new_plan = plan + [(action, args)] # Create a new plan by adding the current action
            
            # Recursive call with the new plan and updated prev_states
            result_plan, is_solution = self.get_backwards_plan(initial_state, predecessor_state, new_plan, new_prev_states)
            if is_solution:
                return result_plan, True

        return plan, False
    '''

    def get_backwards_plan(self, initial_state, goal_state, plan, prev_states):
        state_hash = tuple(goal_state.values()) # Convert dictionary to hashable representation - just the values in a tuple
        
        if state_hash in prev_states: # Check if we've already visited this state
            return plan, False
            
        # Add current state to visited states
        new_prev_states = prev_states.copy()
        new_prev_states.add(state_hash)
        
        if initial_state == goal_state:
            return plan, True # success
        
        actions = self.get_backwards_actions(goal_state)
        if not actions:
            return plan, False
        
        for action_info in actions:
            # Extract action and args based on the format of action_info
            action = action_info[0]
            args = action_info[1:] if len(action_info) > 1 else []
            
            # Use different methods to get precondition based on action type
            if action in [Grab, ClimbUp, ClimbDown]:
                predecessor_state = action.get_pre(goal_state)
            else:  # Move and Push
                predecessor_state = action.get_post(goal_state, args[0])
            
            new_plan = plan + [(action, args)] # Create a new plan by adding the current action
            
            # Recursive call with the new plan and updated prev_states
            result_plan, is_solution = self.get_backwards_plan(initial_state, predecessor_state, new_plan, new_prev_states)
            if is_solution:
                return result_plan, True

        return plan, False
    
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