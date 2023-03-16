from queue import Queue

FINISH_TIME = 100000


def fcfs(processes: list):

    processes.sort(key=lambda process: process.arrival_time)
    current_time = 0
    pending_processes = Queue()

    # while current_time < FINISH_TIME:
    #
    #
    #     current_time += 1
