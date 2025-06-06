from floor import Floor
from elevator import Elevator

class Environment(object):
    def __init__(self, num_floors, num_elevs, max_t=10):
        self.t = 0 # environment timestep
        self.max_t = max_t # maximum timesteps of the env/simulation
        self.terminal = False # terminal state of env/simulation

        self.floors = []
        self.elevators = []

        def init_floors(self, num_floors):
            print('# ENV INITIATING FLOORS #')
            print(' ')
            for i in range(num_floors):
                self.floors.append(Floor(ID=i))

            # Assign pointers to floor above and below
            # Assign pointers to floor above
            for i in range(num_floors-1):
                self.floors[i].set_floor(self.floors[i+1])
            # Assign pointers to floor below
            for i in range(1,num_floors):
                self.floors[i].set_floor(self.floors[i-1], relative='below')
        
        def print_floors(self):
            # Print out each Floor's level, floor above and below
            for floor_obj in self.floors:
                floor_above = floor_obj.get_floor(relative='above')
                floor_below = floor_obj.get_floor(relative='below')

                floor_above_id = floor_above.ID if (floor_above != None) else None
                floor_below_id = floor_below.ID if (floor_below != None) else None

                print(f"Floor {floor_obj.ID}: Floor above={floor_above_id}, Floor below={floor_below_id}")
                print(f"Elevators: {[elev.ID for elev in floor_obj.current_elevators]}")
        
        def init_elevators(self, num_elevs):
            print(' ')
            print('# ENV INITIATING ELEVATORS #')
            print(' ')

            # Create elevators
            for i in range(num_elevs):
                self.elevators.append(Elevator(ID=i,floors=[floor for floor in self.floors]))
            
            # Assign elevator to their default floor
            for elev in self.elevators:
                elev_floor = elev.get_current_floor()
                # print(f'Elevator {elev.ID}, Floor={elev_floor}')
                for floor in self.floors:
                    if floor.ID == elev_floor.ID:
                        floor.set_elevator(elevator=elev)
                        break

        init_floors(self, num_floors)
        # print_floors(self)
        init_elevators(self,num_elevs)
        print_floors(self)
        print('')

        def elev_floor_test(self):
            # get the first elevator
            test_elev = self.elevators[0]
            # set its target floor to the top floor
            test_elev.set_target_floor(floor_idx=-1)
            pass

        elev_floor_test(self)
        pass

    def step(self):
        print(f'# ENV STEP =  {self.t} #')
        
        # TODO: Add environment object updates here

        # Update elevators
        for elev in self.elevators:
            elev.update_state()

        # End of updates to environment objects

        for floor_obj in self.floors:
            floor_above = floor_obj.get_floor(relative='above')
            floor_below = floor_obj.get_floor(relative='below')

            floor_above_id = floor_above.ID if (floor_above != None) else None
            floor_below_id = floor_below.ID if (floor_below != None) else None

            print(f"Floor {floor_obj.ID}: Floor above={floor_above_id}, Floor below={floor_below_id}")
            print(f"Elevators: {[elev.ID for elev in floor_obj.current_elevators]}")

        self.t += 1 # increment timestep

        # stop simulation if timstep exceeds max_t
        if self.t >= self.max_t:
            self.terminal = True
        print('')
        return self.terminal