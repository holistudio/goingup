# Class Definitions

## Elevator

The box that carries passengers to their desired floors

### Properties

 - `ID`
 - `status`: `(stopped, moving)`
 - `floor_location`
 - `direction`
 - `available_floors`: a list of floors the elevator can stop at
 - `target_floor`: the last floor the elevator will stop at (before an `Agent` presses a button inside or another target_floor is assigned by the `ControlSystem`)
 - `button_states`: a list of 0s or 1 of buttons that are active on the elevator panel. expected that the list of `button_states` is always the same size as `available_floors`
 - `door_state`
 - `passengers`: a dynamic list of agents on board

### Functions
 - `get_status()`
 - `set_status(status_id)`
 - `get_floor_location()`
 - `set_floor_location(floor_id)`
 - `get_target_floor()`
 - `set_target_floor(floor_id)`
 - `get_direction()`
 - `set_direction()`
 - `get_button_states()`
 - `set_button_states()`
 - `move()`
 - `check_floor_stop()`
 - `stop()`
 - `open_door()`
 - `close_door()`
 - `check_next_floor()`: checks if the elevator can move up/down a floor or it has reached the top/bottom floor.
 - `update_state()`: the main function that runs and determines what the elevator does at each timestep


## Floor

A container for agents waiting for the elevator

### Properties

 - `ID`: also the floor level. `ID=0` is the ground floor/lobby.
 - `floor_above`: points to the Floor object above this floor. `None` if it's the top floor.
 - `floor_below`: points to the Floor object below this floor. `None` for the ground floor.
 - `occupants`: a dynamic list of Agents on that particular floor
 - `button_state`: `{"up_button", "down_button"}`: dictionary of booleans showing whether up/down buttons are activated or not
 - `current_elevators`: list of the Elevators on this floor. Empty list if no Elevator on this floor.

### Functions

 - `get_floor(relative)`: gets the Floor object above/below this floor
 - `set_floor(relative, floor)`: gets the Floor object above/below this floor
 - `get_occupants()`
 - `check_occupants()`: check to see if Agents have left the floor or new Agents have entered it based on their `floor_location` and `status` property.
 - `set_occupants()`: updates list of occupants based on `check_occupants()`
 - `get_button_state()`
 - `set_button_state(key)`: sets the status of the up/down button, where key=up/down button.
 - `get_elevator(id)`
 - `set_elevator(elevator)`
 - `update_state()`: main function that updates the list of occupants and button_state.

## ControlSystem

A dedicated object that tracks floor button statuses to decide which elevators to move in which direction towards a ultimate `target_floor` destination. 

## Agent 

A person that enters the building, gets to their desired floor on the elevator, stays for a while, then uses the elevator again to get out of the building on the ground floor.

### Properties
 
 - `ID`
 - `status`: `(waiting, in elevator, doing business)`
 - `current_floor`: points to the current Floor object
 - `current_elevator`: points to the current Elevator object Agent is in. `None` if not in elevator.
 - `target_floor_location`
 - `stay_time`: tracks how long the person is at their desired floor after they get out of the elevator
 - `stay_duration`: how long the person stays at their desired floor
 - `wait_times`: tuple of how long the person has been waiting for the elevator at ground floor and at the target floor after their stay duration
 - `total_stay_period`: tracks the total amount of time person is in the building

### Functions

 - `get_status()`
 - `set_status(index)`
 - `get_floor_location()`
 - `set_floor_location(floor_id)`
 - `update_floor_location(floor_id)`
 - `check_elevators()`
 - `check_floor_buttons()`
 - `press_floor_button(key)`
 - `enter_elevator(elevator_id)`
 - `check_elevator_buttons(elevator_id)`
 - `press_elevator_button(floor_id)`
 - `check_target_floor()`: checks if the person is at their desired floor
 - `exit_elevator()`
 - `get_stay_time()`
 - `set_stay_time()`
 - `update_wait_time(index)`: update the wait time, where index is based on whether the person is at the ground floor or their target floor waiting for the elevator.
 - `update_total_stay()`
 - `update_state()`: the main function that controls how the person moves or waits for the elevator.

## Environment

A dedicated object to communicate interactions between Agents and Floor/Elevators.

### Properties

 - `num_elevators`
 - `num_floors`
 - `timestep`

### Functions
 - `init()`: Creates all the things
 - `step()`: Moves all the things one timestep forward