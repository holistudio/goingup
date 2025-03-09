# Dev Log

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

