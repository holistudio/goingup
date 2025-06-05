from elevator import Elevator

class Floor(object):
    def __init__(self, ID):
        self.ID = ID
        self._floor_above = None
        self._floor_below = None
        self.occupants = []
        self.button_state ={
            "up_button": False,
            "down_button": False
        }
        self.current_elevators = []
        pass
    
    def get_floor(self, relative='above'):
        if relative == 'above':
            return self._floor_above
        elif relative == 'below':
            return self._floor_below
        else:
            raise ValueError('Invalid "relative" value. Only (above, below) are valid values.')
    
    def set_floor(self, floor, relative='above'):
        if isinstance(floor, Floor) or floor is None:
            if relative == 'above':
                self._floor_above = floor
            elif relative == 'below':
                self._floor_below = floor
            else:
                raise ValueError('Invalid "relative" value. Only (above, below) are valid values.')
        else:
            raise TypeError('"floor" must be an instance of Floor or None')
    
    def get_elevator(self, id):
        found_i = -1
        elevator = None

        # check current list of elevators for one with matching ID
        for i,elev in enumerate(self.current_elevators):
            if id == elev.ID:
                found_i = i
                elevator = elev
        return elevator, found_i
    
    def set_elevator(self, elevator, on_off='on'):
        if isinstance(elevator, Elevator) or elevator is None:
            # check if elevator already exists in current_elevators
            # if so, find its position index
            elev, found_i = self.get_elevator(id=elevator.ID)
            
            if on_off == 'on':
                # if the elevator isn't on the floor, append to the list of current_elevators
                if found_i == -1:
                    self.current_elevators.append(elevator)
                else:
                    raise LookupError('Attempting to add an elevator already on this floor.')
            elif on_off == 'off':
                # if the elevator isn't on the floor, remove from the list at the found position index
                if found_i != -1:
                    self.current_elevators.pop(found_i)
                else:
                    raise LookupError('Attempting to remove an elevator not on this floor.')
            else:
                raise ValueError('Invalid "On_off" value. Only (on, off) are valid values.')
        else:
            raise TypeError('"elevator" must be an instance of Elevator or None')

def test_floor_pointers():
    # Create 3 Floors
    floor_list = []
    for i in range(3):
        floor_list.append(Floor(ID=i))

    # Assign pointers to floor above and below
    # Assign pointers to floor above
    for i in range(2):
        floor_list[i].set_floor(floor_list[i+1])
    # Assign pointers to floor below
    for i in range(1,3):
        floor_list[i].set_floor(floor_list[i-1], relative='below')
    
    # Print out each Floor's level, floor above and below
    for floor_obj in floor_list:
        floor_above = floor_obj.get_floor(relative='above')
        floor_below = floor_obj.get_floor(relative='below')

        floor_above_id = floor_above.ID if (floor_above != None) else None
        floor_below_id = floor_below.ID if (floor_below != None) else None

        print(f"Floor {floor_obj.ID}: Floor above={floor_above_id}, Floor below={floor_below_id}")

def test():
    print('FLOOR CLASS TESTS')
    test_floor_pointers()
    pass

if __name__ == "__main__":
    test()