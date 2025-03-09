class Floor():
    def __init__(self, ID):
        super.__init__(object)
        self.ID = ID
        self._floor_above = None
        self._floor_below = None
        self.occupants = []
        self.button_state ={
            "up_button": False,
            "down_button": False
        }
        pass
    
    def get_floor(self, relative='above'):
        if relative == 'above':
            return self._floor_above
        elif relative == 'below':
            return self._floor_below
        else:
            return 'Error: Invalid relative value. Only (above, below) are valid values.'
    
    def set_floor(self, floor, relative='above'):
        if isinstance(floor, Floor) or floor is None:
            if relative == 'above':
                self._floor_above = floor
            elif relative == 'below':
                self._floor_below = floor
            else:
                return 'Error: Invalid relative value. Only (above, below) are valid values.'
        else:
            raise TypeError("next must be an instance of Floor or None")

def test():
    print('FLOOR CLASS BASIC TEST')
    pass

if __name__ == "__main__":
    test()