import time 

TIMESTEP = 1

def main():
    # intialize sim time
    t = 0

    # intialize terminal state
    terminal = False

    print('### START SIMULATION ###')
    # simulation loop
    while not terminal:
        print(f'TIMESTEP = {t}')

        # increment sim time
        t += 1

        # wait TIMESTEP
        time.sleep(TIMESTEP)

        # check terminal state
        if t > 10:
            terminal = True
            print('### END SIMULATION ###')
        

if __name__ == "__main__":
    main()