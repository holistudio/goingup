# Class Definitions

## Elevator

The box that carries passengers to their desired floors

### Properties

 - `floor_location`
 - `direction`
 - `available_floors`: a list of floors the elevator can stop at
 - `button_states`
 - `door_state`
 - `passengers`: a dynamic list of agents on board

### Functions
 - `get_floor_location()`
 - `get_direction()`
 - `set_direction()`
 - `move()`
 - `check_floor_stop()`
 - `open_door()`
 - `close_door()`
 - `main_control()`: the main function that runs and determines what the elevator does at each timestep

## Agent 

### Properties

### Functions