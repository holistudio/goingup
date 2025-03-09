class Floor():
    def __init__(self, ID):
        super.__init__(object)
        self.ID = ID
        self.floor_above = None
        self.floor_below = None
        self.occupants = []
        self.button_state ={
            "up_button": False,
            "down_button": False
        }
        pass
    
    def get_floor(self, relative='above'):
        if relative == 'above':
            return self.floor_above
        elif relative == 'below':
            return self.floor_below
        else:
            return 'Error: Invalid relative value. Only (above, below) are valid values.'

def test():
    print('FLOOR CLASS BASIC TEST')
    pass

if __name__ == "__main__":
    test()