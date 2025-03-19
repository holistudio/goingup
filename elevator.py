class Elevator(object):
    def __init__(self, ID):
        self.ID = ID
        self._possible_status = ('stopped', 'moving')
        self.status = self._possible_status[0]
        self.floor_location = 0
        self._possible_direction = ('none','up','down')
        self.direction = self._possible_direction[0]
        self.available_floors = []
        self.button_states = []
        self._possible_door_state = ('open', 'closed')
        self.door_state = self._possible_door_state[0]
        self.passengers = []
        pass

def test():
    print('ELEVATOR CLASS TESTS')
    pass

if __name__ == "__main__":
    test()