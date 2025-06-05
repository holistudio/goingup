import time 

import env

PAUSE = 1

environment = env.Environment()

def main():
    # intialize sim time
    t = 0

    # intialize terminal state
    terminal = False

    print('### START SIMULATION ###')
    # simulation loop
    while not terminal:
        print(f'TIMESTEP = {t}')

        environment.step()

        # increment sim time
        t += 1

        # wait PAUSE seconds
        time.sleep(PAUSE)

        # check terminal state
        if t > 10:
            terminal = True
            print('### END SIMULATION ###')
        

if __name__ == "__main__":
    main()