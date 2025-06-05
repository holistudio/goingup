class Environment(object):
    def __init__(self, max_t=10):
        self.t = 0 # environment timestep
        self.max_t = max_t # maximum timesteps of the env/simulation
        self.terminal = False # terminal state of env/simulation
        pass

    def step(self):
        print(f'# ENV STEP =  {self.t} #')
        
        # TODO: Add environment object updates here

        # End of updates to environment objects

        self.t += 1 # increment timestep

        # stop simulation if timstep exceeds max_t
        if self.t >= self.max_t:
            self.terminal = True

        return self.terminal