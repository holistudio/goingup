# TODOS
- [ ] System Design Diagram: What things get passed to which objects so that the entire thing works with the control system
  - [ ] Consider defining a separate Environment class that the Simulation runs

- [ ] Code Elevator class for handling Floors only
- [ ] Modify Floor to take on multiple Elevators

- [ ] Test simulation (no ControlSystem or Agent): Get two Elevators to move up and down 6 Floors.

- [ ] Agent class: Always checks if there is an elevator going down and targets the ground floor 0.

- [ ] Test simulation (no ControlSystem): Place Agent on the top floor. It should wait until it sees an elevator going down then get on and go down the ground floor.


- [ ] ControlSystem class

- [ ] Review coding patterns for basic testing of Elevator and Floor classes
  - [ ] Write basic tests for Floor class