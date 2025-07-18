class Elevator(object):
    def __init__(self, ID, floors):
        """
        Input:
         - ID: unique identifier for this elevator instance
         - floors: a list of Floor objects

        Properties:
         - ID: unique identifier for this elevator instance
         - available_floors: a list of floors this elevator can go to
         TODO: Complete list based on properties implemented
        """
        
        self.ID = ID
        self._possible_status = ('stopped', 'moving')
        self.status = self._possible_status[0]
        
        self._possible_direction = ('none','up','down')
        self.direction = self._possible_direction[0]

        self.available_floors = floors
        self.current_floor = self.available_floors[0]
        self.target_floor = None

        self.button_states = [0 for i in floors]

        self._possible_door_state = ('open', 'closed')
        self.door_state = self._possible_door_state[0]
        self.passengers = []
        pass

    def get_status(self):
        return self.status
    
    def set_status(self, status_id):
        # TODO: check status_id for ValueError
        self.status = self._possible_status[status_id]
        return self.status
    
    def get_current_floor(self):
        return self.current_floor
    
    def set_current_floor(self, floor_idx):
        """
        Set current_floor to the Floor object within
        list of available_floors

        Input
         - floor_idx: Index within vailable_floors list
        """

        # TODO: check floor_idx for ValueError
        self.current_floor = self.available_floors[floor_idx]

        return self.current_floor
    
    def get_target_floor(self):
        return self.target_floor
    
    def set_target_floor(self, floor_idx):
        """
        Set target_floor to the Floor object within
        list of available_floors

        Input
         - floor_idx: Index within vailable_floors list
        """

        # If Elevator has no target Floor, set to None
        if floor_idx == None:
            self.target_floor = None
        else:
            # Otherwise assign a new target Floor
            # TODO: check floor_idx for ValueError
            self.target_floor = self.available_floors[floor_idx]

        return self.target_floor

    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction_id):
        # TODO: check direction_id for ValueError range (0-2)
        self.direction = self._possible_direction[direction_id]
        return self.direction
    
    def get_button_states(self):
        return self.button_states
    
    def set_button_states(self, i, val):
        if (val != 0) or (val != 1):
            raise ValueError('Invalid button state value. Only (0, 1) are valid values.')
        self.button_states[i] = val
        return self.button_states
    
    def move(self):
        """
        Move the Elevator one floor up or down based on
        its current direction.
        """

        # Get index of current Floor
        floor_idx = self.available_floors.index(self.current_floor)

        # Depending on current direction
        if self.direction == 'up':
            # Go up to the next available floor up
            self.set_current_floor(floor_idx+1)
        if self.direction == 'down':
            # Go up to the next available floor down
            self.set_current_floor(floor_idx-1)

        return self.current_floor
    
    def check_floor_stop(self):
        """
        Check if Elevator stops based on if any buttons 
        have been pressed.
        """

        # Get index of current Floor
        floor_idx = self.available_floors.index(self.current_floor)

        # Check if button for current Floor has been pressed
        button_check = self.button_states[floor_idx]
        if button_check == 1:
            return True
        else:
            return False
        
    def stop(self):
        self.set_status(0)
        return self.status
    
    def open_door(self):
        self.door_state = self._possible_door_state[0]
    
    def close_door(self):
        self.door_state = self._possible_door_state[1]

    def check_next_floor(self):
        """
        Check if there is another Floor to go to in 
        Elevator's current direction

        Return: 
        False if Elevator is at the bottom- or top-most Floor
        otherwise True.
        """

        # Get index of current Floor
        floor_idx = self.available_floors.index(self.current_floor)

        # If the direction is up, check index against available_floors list length
        if self.direction == 'up':
            return (floor_idx+1) < len(self.available_floors)
        
        # If the direction is up, check index against available_floors list length
        if self.direction == 'down':
            return (floor_idx-1) >= 0
        
        # TODO: Revisit, may make more sense to check if an elevator is moving or not
        raise ValueError("Elevator direction is not set to 'up' or 'down' values")
    
    def display(self):
        """
        Display the Elevator in terminal.
        Show if its moving and if so, in what direction
        """
        if self.direction == 'up':
            up_down = '↑'
        elif self.direction =='down':
            up_down = '↓'
        else:
            up_down = '='
        display_text = f'[{self.ID}{up_down}]'
        return display_text

    def update_state(self):

        if self.status == 'moving':
            need_to_stop = False
            # check if it needs to stop at this floor
            # check floor's button
            if self.direction == 'up' and self.current_floor.get_button_state()['up_button']:
                need_to_stop = True
            if self.direction == 'down' and self.current_floor.get_button_state()['down_button']:
                need_to_stop = True
            # check list of activated buttons inside elevator
            if self.check_floor_stop():
                need_to_stop = True
            
            if need_to_stop:
                self.stop()

                # deactivate the elevator button for the current floor
                floor_i = self.available_floors.index(self.current_floor)
                self.set_button_states(i=floor_i, val=0)

                floor_diff = self.target_floor.ID - self.current_floor.ID
                if floor_diff == 0:
                    # target floor reached
                    self.set_target_floor(None)
                    self.set_status(0)
                    self.set_direction(0)
            else:
                # if not move to the next floor in its direction
                if self.check_next_floor():
                    self.current_floor.set_elevator(elevator=self, on_off='off')
                    self.move()
                    self.current_floor.set_elevator(elevator=self)
                else:
                    self.stop()

        if self.status == 'stopped':
            # check if target floor assigned
            target_floor_assigned = (self.target_floor != None)

            # check if any buttons are activated
            buttons_active = False
            for b in self.button_states:
                if b == 1:
                    buttons_active = True
            
            need_to_move = target_floor_assigned or buttons_active

            # if so, start moving in the appropriate direction
            if need_to_move:
                self.set_status(1)
                floor_diff = self.target_floor.ID - self.current_floor.ID
                if floor_diff > 0:
                    self.set_direction(1) # go up
                elif floor_diff < 0:
                    self.set_direction(2) # go down
                else:
                    # target floor reached
                    self.set_target_floor(None)
                    self.set_status(0)
                    self.set_direction(0)
            else:
                # TODO: Open the door, let Agents in/out...
                pass
            
        # if (self.target_floor != None):
        #     print(f"Elevator{self.ID}: {self.current_floor.ID},{self.status},{self.target_floor.ID},{floor_diff},{self.target_floor.ID-self.current_floor.ID}")
        # else:
        #     print(f"Elevator{self.ID}: {self.current_floor.ID},{self.status},None")


def test():
    print('ELEVATOR CLASS TESTS')
    pass

if __name__ == "__main__":
    test()