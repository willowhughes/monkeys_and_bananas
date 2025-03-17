import copy

class Move:
    """Action for moving the monkey between rooms."""

    @staticmethod
    def check_pre(state, src_room):
        """Check if monkey can move from source room (can be used for backward planning)

        Args:
            state (dict): Current state of the world
            src_room (int): Room monkey is moving from

        Returns:
            bool: True if monkey is low and in source room
        """
        return state['monkey_location'] == src_room and state['monkey_level'] == 0

    @staticmethod
    def get_post(state, dst_room):
        """Calculate state after moving monkey to destination room (can be used for backward planning)

        Args:
            state (dict): Current state of the world
            dst_room (int): Room to move monkey to

        Returns:
            dict: New state after moving monkey
        """
        new_state = copy.deepcopy(state)
        new_state['monkey_location'] = dst_room
        return new_state


class Push:
    """Action for pushing the box between rooms."""

    @staticmethod
    def check_pre(state, src_room):
        """Check if monkey can push box from source room.

        Args:
            state (dict): Current state of the world
            src_room (int): Room to push from

        Returns:
            bool: True if monkey is low and in same room as box
        """
        return (state['monkey_location'] == src_room and 
                state['monkey_level'] == 0 and 
                state['box_location'] == src_room)

    @staticmethod
    def get_post(state, dst_room):
        """Calculate state after pushing box to destination room.

        Args:
            state (dict): Current state of the world
            dst_room (int): Room to push box to

        Returns:
            dict: New state after pushing box
        """
        new_state = copy.deepcopy(state)
        new_state['monkey_location'] = dst_room
        new_state['box_location'] = dst_room
        return new_state


class ClimbUp:
    """Action for monkey climbing up onto the box."""

    @staticmethod
    def check_pre(state):
        """Check if monkey can climb up.

        Args:
            state (dict): Current state of the world

        Returns:
            bool: True if monkey is low and in same room as box
        """
        return state['monkey_location'] == state['box_location'] and state['monkey_level'] == 0

    @staticmethod
    def get_post(state):
        """Calculate state after monkey climbs up.

        Args:
            state (dict): Current state of the world

        Returns:
            dict: New state after climbing up
        """
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 1
        return new_state

    @staticmethod
    def check_post(state):
        """Check if monkey could have just climbed up.

        Args:
            state (dict): Current state of the world

        Returns:
            bool: True if monkey is high
        """
        return state['monkey_level'] == 1

    @staticmethod
    def get_pre(state):
        """Calculate state before monkey climbed up (for backward planning).

        Args:
            state (dict): Current state of the world

        Returns:
            dict: Previous state before climbing up
        """
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 0
        if state['box_location'] == -1:
            new_state['box_location'] = state['monkey_location']
        return new_state


class ClimbDown:
    """Action for monkey climbing down from the box."""

    @staticmethod
    def check_pre(state):
        """Check if monkey can climb down.

        Args:
            state (dict): Current state of the world

        Returns:
            bool: True if monkey is high and in same room as box
        """
        return state['monkey_location'] == state['box_location'] and state['monkey_level'] == 1

    @staticmethod
    def get_post(state):
        """Calculate state after monkey climbs down.

        Args:
            state (dict): Current state of the world

        Returns:
            dict: New state after climbing down
        """
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 0
        return new_state

    @staticmethod
    def check_post(state):
        """Check if monkey could have just climbed down.

        Args:
            state (dict): Current state of the world

        Returns:
            bool: True if monkey is low
        """
        return state['monkey_level'] == 0

    @staticmethod
    def get_pre(state):
        """Calculate state before monkey climbed down (for backward planning).

        Args:
            state (dict): Current state of the world

        Returns:
            dict: Previous state before climbing down
        """
        new_state = copy.deepcopy(state)
        new_state['monkey_level'] = 1
        return new_state


class Grab:
    """Action for monkey grabbing the banana."""

    @staticmethod
    def check_pre(state):
        """Check if monkey can grab banana.

        Args:
            state (dict): Current state of the world

        Returns:
            bool: True if monkey is high and in same room as banana
        """
        return state['monkey_location'] == state['banana_location'] and state['monkey_level'] == 1

    @staticmethod
    def get_post(state):
        """Calculate state after monkey grabs banana.

        Args:
            state (dict): Current state of the world

        Returns:
            dict: New state after grabbing banana
        """
        new_state = copy.deepcopy(state)
        new_state['has_banana'] = 1
        return new_state

    @staticmethod
    def check_post(state):
        """Check if monkey could have just grabbed banana.

        Args:
            state (dict): Current state of the world

        Returns:
            bool: True if monkey has banana
        """
        return state['has_banana'] == 1

    @staticmethod
    def get_pre(state):
        """Calculate state before monkey grabbed banana (for backward planning).

        Args:
            state (dict): Current state of the world

        Returns:
            dict: Previous state before grabbing banana
        """
        new_state = copy.deepcopy(state)
        new_state['has_banana'] = 0
        new_state['monkey_location'] = state['banana_location']
        new_state['monkey_level'] = 1
        return new_state