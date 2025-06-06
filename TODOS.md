# TODOS

- [X] System Design Diagram: What things get passed to which objects so that the entire thing works with the control system

- [X] Consider defining a separate Environment class that the Simulation runs

- [X] Simple Environment class with a step function.
- [X] Environment records timestep and returns a terminal condition.

- [ ] Test simulation (no ControlSystem or Agent): Get two Elevators to move up and down 6 Floors.
  - [X] Code Elevator class for handling button states
  - [X] Code Elevator class for handling Floors only
  - [X] Modify Floor to take on multiple Elevators
  - [X] Create 2 elevators and 6 floors when Environment initiates
  - [ ] Somehow pass the Floor's button states to the Elevator, so it can decide whether or not to stop.
  - [ ] Artificially set the elevator's `target_floor` to the 6th floor
  - [ ] Elevators should automatically move up to the 6th floor
  - [ ] For now, they should stop - need a ControlSystem to tell the Elevator when to move down

- [ ] Agent class: Always checks if there is an elevator going down and targets the ground floor 0.

- [ ] Test simulation (no ControlSystem): Place Agent on the top floor. It should wait until it sees an elevator going down then get on and go down the ground floor.


- [ ] ControlSystem class

- [ ] Review coding patterns for basic testing of Elevator and Floor classes
  - [ ] Write basic tests for Floor class