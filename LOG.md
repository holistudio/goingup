# Dev Log

## 2025-06-05

A basic question that keeps coming up in my head is "How should the states of the different classes/objects get updated?" In other words, in `env.step()` is it as simple as

```
def step():
   for elevator in elevators:
      elevator.update_state()
   for floor in floors:
      floor.update_state()
   for agent in agents:
      agent.update_state()
```

My current guess is "No, it's more complicated than that." The specific properties of each Elevator, Floor, and Agent has to be updated in a specific logic...but I don't know for sure.

One reason why it might be more complicated is because of "race conditions" between two elevators: Let's say the button going down is pressed on the 5th floor and then two elevators reach the 5th floor at the same time - ideally one elevator stops and serves the people on the 5th floor and the other one should just stop at the 5th floor and await commands from a control system.

For now, I'm focusing on writing enough getters and setters for each class's properties and will see when I finally put everything together how complicated it gets. Right now the Environment is manually setting the elevators' directions and then moving them until they hit a floor with an active button.

But this question will linger around until then, especially if I think there are some "checks" that each elevator should be doing on its own to decide what to do next - as if each elevator is its own "agent"...

Or maybe it's a mix of the two ideas:
 - ControlSystem may set a `target_floor` for each elevator to guide it to a particular floor where a person is waiting
 - But the `Elevator` object still checks on its own in the `update_state()` function whether to stop at a current floor, either because a person inside the elevator has selected a floor to stop at or a person on an intermediate floor on the way is also waiting.


Currently, that's how the the `Environment` and `Elevator` works:
 1. `Environment` sets a target floor for one of the elevators
 2. The elevator moves up automatically to that target floor and stops there via its `update_state()` function
 3. Since each Elevator has `current_floor` and `available_floors` properties, which are pointers to all `Floor` objects, this enables the Elevator's `update_state()` function to also updates the `Floor` object's list of elevators each time it moves out of one `Floor` and into another `Floor`.

So far only a test was made for one elevator moving up to the top floor. More tests should follow where two elevators move at the same time, to different target floors. 

## 2025-06-04

Finally circling back to this after some time, barely remembering what I worked on last and what I need to do next...

Looks like having a `Simulation` and `Environment` class separately makes more sense. That way the while loop of the `sim.py` can just look like this:

```
...
while (not terminal):
   env.step()
   t += 1
   ...
```

and all the complicated order of `Floor`, `Elevator`, `Agent` can happen inside `env.step()`

I can start on the bare minimum version of `env.step()` for now

## 2025-03-09

Added the Floor class and figured out how each Floor object can point to another Floor above and below it.

I'm realizing I have no idea/forgot how to write tests for basic class definitions/functions. For now, I wrote a single test function that defines 3 Floor objects and links them together so they point to each other.

As I thought about these pointers, I realized I didn't consider that the Floor should have a property pointing to the Elevator object, if the Elevator is on that Floor instance.

I'm still deciding whether I need both a `Simulation` class and an `Environment` class...
 - `Simulation` could handle just running the Environment one step at at time and take on the bulk of logging everything that happens at each timestep and displaying things on the terminal
 - `Environment` handles the proper order of updating each state of Elevator/Floor/Agent

Ah right...A Floor can have multiple elevators present...

Things are getting really complicated! Adding a TODO list...

## 2025-03-08

The goal: Make a simulation of people entering a building to go to a random floor, waiting for an elevator, staying for a while, and then coming back out. Display the environment only in the terminal. 

Had this idea brewing in my head for awhile now, ever since I entered into an elevator and thought about how the programming behind them works. The basic logic of an elevator seems simple enough. Is the current floor the same as a button someone pressed? If so, stop, else...

But what decides which elevator moves to serve the people waiting on each floor? How do the elevators work exactly?

Another part of this idea that attracts me is that the simulation displays everything in the terminal, much like a Multi-User Dungeon haha.

This is meant to be a silly project with no real world applications. But it should be a great learning exercise for:

 - Refreshing myself on how to do objected oriented programming and other best practices.
   - Abstraction: What are the best ways to organize all the code, especially if new subclasses/versions of Agents and ControlSystems need to be created?
   - Unit testing: What are basic ways to test this code?
 - Practice making the code readable/"professional" - hopefully since my mind isn't totally exhausted on just getting code to work or thinking about the ideas and has time to consider how the code can be more "elegant."
 - Learning C++...after I get this working in Python ;)

