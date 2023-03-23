import numpy as np
import math

from process import Process


def generate_processes(n_of_processes) -> list:
    processes = []
    current_arrival_time = 0
    current_process_id = 0
    for _ in range(n_of_processes):
        execution_time = generate_random_execution_time()
        arrival_time_delta = generate_random_arrival_time_delta()
        current_arrival_time += arrival_time_delta
        process_to_add = Process(
            process_id=current_process_id,
            arrival_time=current_arrival_time,
            time_needed_for_execution=execution_time
        )
        current_process_id += 1
        processes.append(process_to_add)
    return processes


def generate_random_execution_time():
    random_number = np.random.randint(10)
    if random_number == 9:
        execution_time = max(math.floor(np.random.normal(100, 10)), 1)
    elif random_number <= 1:
        execution_time = max(math.floor(np.random.normal(5, 1)), 1)
    else:
        execution_time = max(math.floor(np.random.normal(20, 5)), 1)

    return execution_time


def generate_random_arrival_time_delta():
    random_number = np.random.randint(10)
    if random_number == 9:
        arrival_time_delta = max(math.floor(np.random.normal(120, 10)), 1)
    elif random_number <= 1:
        arrival_time_delta = max(math.floor(np.random.normal(5, 1)), 1)
    else:
        arrival_time_delta = max(math.floor(np.random.normal(20, 5)), 1)

    return arrival_time_delta
