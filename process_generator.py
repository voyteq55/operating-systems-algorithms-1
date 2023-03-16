import numpy as np
import math

from process import Process


def generate_processes(n_of_processes) -> list:
    processes = []
    current_arrival_time = 0
    current_process_id = 0
    for _ in range(n_of_processes):
        execution_time = max(math.floor(np.random.normal(20, 10)), 1)
        arrival_time_delta = max(math.floor(np.random.normal(19, 5)), 1)
        current_arrival_time += arrival_time_delta
        process_to_add = Process(
            process_id=current_process_id,
            arrival_time=current_arrival_time,
            time_needed_for_execution=execution_time
        )
        current_process_id += 1
        processes.append(process_to_add)
    return processes

