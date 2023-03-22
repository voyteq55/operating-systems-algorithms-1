import fcfs_algorithm
import process_generator
import copy

import sjf_algorithm


def start():
    for _ in range(20):
        processes = process_generator.generate_processes(10000)
        results_fcfs = fcfs_algorithm.fcfs(copy.deepcopy(processes))
        stats_fcfs = calculate_results(results_fcfs)
        print(stats_fcfs)

        results_sjf = sjf_algorithm.sjf(copy.deepcopy(processes))
        stats_sjf = calculate_results(results_sjf)
        print(stats_sjf)
        print()


def calculate_results(results):
    avg_time_waited_for_execution_start = 0
    avg_time_from_start_to_finish = 0

    finished_processes = results["finished"]
    for process in finished_processes:
        avg_time_waited_for_execution_start += process.time_waited_for_execution_start
        avg_time_from_start_to_finish += process.time_from_start_to_finish

    avg_time_waited_for_execution_start /= len(finished_processes)
    avg_time_from_start_to_finish /= len(finished_processes)
    avg_waiting_time = avg_time_waited_for_execution_start + avg_time_from_start_to_finish
    longest_waiting_time = max([process.time_waited_for_execution_start + process.time_from_start_to_finish for process in finished_processes])

    return avg_time_waited_for_execution_start, avg_time_from_start_to_finish, avg_waiting_time, longest_waiting_time, results["switches"]



