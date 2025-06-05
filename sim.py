import time 

import env

PAUSE = 1

environment = env.Environment()

def main():

    # intialize terminal state
    terminal = False

    print('### START SIMULATION ###')
    # simulation loop
    while not terminal:
        
        terminal = environment.step()

        # wait PAUSE seconds
        time.sleep(PAUSE)

    print('### END SIMULATION ###')
        

if __name__ == "__main__":
    main()