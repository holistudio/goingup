class Elevator(object):
    def __init__(self, ID, floors):
        """
        Properties:
         - ID: unique identifier for this elevator instance
         - floors: a list of floors this elevator can go to
        """
        self.ID = ID
        self._possible_status = ('stopped', 'moving')
        self.status = self._possible_status[0]
        
        self._possible_direction = ('none','up','down')
        self.direction = self._possible_direction[0]

        self.available_floors = floors
        self.floor_location = self.available_floors[0]
        self.target_floor = None

        self.button_states = [0 for i in floors]

        self._possible_door_state = ('open', 'closed')
        self.door_state = self._possible_door_state[0]
        self.passengers = []
        pass

    def get_status(self):
        return self.status
    
    def set_status(self, status_id):
        self.status = self._possible_status[status_id]
        return self.status
    
    def get_floor_location(self):
        return self.floor_location
    
    def set_floor_location(self, floor_id):
        self.floor_location = self.available_floors[floor_id]
        return self.floor_location
    
    def get_target_floor(self):
        return self.target_floor
    
    def set_target_floor(self, floor_id):
        self.target_floor = floor_id
        return self.target_floor

    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction_id):
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
        floor_idx = self.available_floors.index(self.floor_location)
        if self.direction == 'up':
            self.set_floor_location(floor_idx+1)
        if self.direction == 'down':
            self.set_floor_location(floor_idx-1)
        return self.floor_location
    
    def check_floor_stop(self):
        button_check = self.button_states[self.floor_location]
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
        floor_idx = self.available_floors.index(self.floor_location)
        if self.direction == 'up':
            return (floor_idx+1) < len(self.available_floors)
        if self.direction == 'down':
            return (floor_idx-1) >= 0
        pass

    def update_state(self, floor_button_state):
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
                floor_diff = self.target_floor - self.floor_location
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
            
        if self.status == 'moving':
            need_to_stop = False
            # check if it needs to stop at this floor
            # check floor's button
            if self.direction == 'up' and floor_button_state['up_button']:
                need_to_stop = True
            if self.direction == 'down' and floor_button_state['down_button']:
                need_to_stop = True
            # check list of activated buttons inside elevator
            if self.check_floor_stop():
                need_to_stop = True
            
            if need_to_stop:
                self.stop()
                
                # deactivate the elevator button for the current floor
                floor_i = self.available_floors.index(self.floor_location)
                self.set_button_states(i=floor_i, val=0)
            else:
                # if not move to the next floor in its direction
                if self.check_next_floor():
                    self.move()
                else:
                    self.stop()


def test():
    print('ELEVATOR CLASS TESTS')
    pass

if __name__ == "__main__":
    test()