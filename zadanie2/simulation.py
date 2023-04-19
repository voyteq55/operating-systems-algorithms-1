import copy

from algorithm import Algorithm
import request_generator
from fcfs_algorithm import FCFSAlgorithm

INITIAL_DISK_HEAD_POSITION = 500
MAX_DISK_CAPACITY = 1000
NUMBER_OF_REQUESTS = 500


def perform_simulation():

    requests = request_generator.generate_requests(NUMBER_OF_REQUESTS, MAX_DISK_CAPACITY)
    for r in requests:
        print(r)

    fcfs = FCFSAlgorithm(
        requests=copy.deepcopy(requests),
        initial_disk_head_position=INITIAL_DISK_HEAD_POSITION,
        max_disk_capacity=MAX_DISK_CAPACITY,
        real_time_requests_strategy=None
    )
    fcfs_results = fcfs.perform_accessing()
    finished = fcfs_results["finished"]
    for f in finished:
        print(f)
    print(fcfs_results)
