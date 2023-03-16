import fcfs_algorithm
import process_generator


def start():
    processes = process_generator.generate_processes(100)
    for p in processes:
        print(p)
    fcfs_algorithm.fcfs(processes)
    for p in processes:
        print(p)
