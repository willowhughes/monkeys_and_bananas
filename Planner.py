from Operators import ClimbUp, Move, Push, Grab, ClimbDown

class Planner:
    """A backward-chaining planner for the Monkey and Banana problem."""

    def __init__(self):
        """Initialize the planner with an empty adjacency matrix."""
        self.adj_matrix = None

    def start(self, initial_state, goal_state, adj_matrix):
        """Start the planning process.

        Args:
            initial_state (dict): The starting state of the world
            goal_state (dict): The desired end state to achieve
            adj_matrix (list): 2D adjacency matrix representing room connections

        Returns:
            tuple: (plan, is_solution) where plan is a list of (action, args) pairs
                  and is_solution is a boolean indicating if a solution was found
        """
        self.adj_matrix = adj_matrix

        plan, is_solution = self.get_backwards_plan(initial_state, goal_state, [], set())
        plan.reverse()
        return plan, is_solution

    def get_backwards_plan(self, initial_state, goal_state, plan, prev_states):
        """Recursively search for a plan using backward chaining.

        Args:
            initial_state (dict): The starting state to reach
            goal_state (dict): The current state to plan backwards from
            plan (list): The current plan being built
            prev_states (set): Set of previously visited states to avoid cycles

        Returns:
            tuple: (plan, is_solution) where plan is a list of (action, args) pairs
                  and is_solution is a boolean indicating if a solution was found
        """
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
        """Get all possible actions that could have led to the current state.

        Args:
            state (dict): The current state to plan backwards from

        Returns:
            list: List of [action, *args] lists representing possible previous actions
        """
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
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] == 1:
                    if Move.check_pre(state, j):
                        actions.append([Move, i, j])  # Move from j to i in backwards chaining
                    if Push.check_pre(state, j):
                        actions.append([Push, i, j]) # Push from j to i in backwards chaining
        return actions