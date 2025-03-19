class Elevator(object):
    def __init__(self, ID):
        self.ID = ID
        self._possible_status = ('stopped', 'moving')
        self.status = self._possible_status[0]
        
        self._possible_direction = ('none','up','down')
        self.direction = self._possible_direction[0]

        self.available_floors = [0]
        self.floor_location = self.available_floors[0]

        self.button_states = [0]

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
    
    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction_id):
        self.direction = self._possible_direction[direction_id]
        return self.direction
    
    def move(self):
        self.set_status(1)
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

def test():
    print('ELEVATOR CLASS TESTS')
    pass

if __name__ == "__main__":
    test()