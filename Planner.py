from Operators import ClimbUp

class Planner:

    def start(adj_matrix, initial_state):

        state = initial_state
        print("Initial state: ", state)

        # new_state = Operators.climb_up(state)
        # if new_state != None:
        #     print("climbing up")
        # else:
        #     print("can't climb up")

        if ClimbUp.check_pre(state):
            new_state = ClimbUp.get_post(state)
            print("climbing up")
            print("final state: ", new_state)
        else:
            print("can't climb up")
        


    # dfs brute force 
    def get_plan(state, plan):
        if state['has_banana'] == True:
            return plan, True # success
        
        actions = get_actions(start_state, ...)
        # actions is a list of ordered pairs where [0] is the action and [1] is the arguments to that action
        # how do I store the action and the args?
        if not actions:
            return plan, False
        
        for action, args in actions:
            next_state = action(args) # how should I apply a certain action?
            # possible example?: next_state = Move.get_post(args)
            plan, is_solution = get_plan(next_state, plan.deepcopy().append(action, args))
            if is_solution:
                return plan, True

        return plan, False