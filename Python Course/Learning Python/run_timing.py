def run_time():
    """Asks the user repeatedly for numeric input. 
    Prints the average time and nums and runs."""
    sum_of_running = 0
    counter = 0
    while True:
            run_mode = input('Enter your run: ')
            if not run_mode:
                break
            sum_of_running = sum_of_running + int(run_mode)
            counter += 1
    return print(f'Average run is: {sum_of_running}, over {counter} runs')


run_time()
