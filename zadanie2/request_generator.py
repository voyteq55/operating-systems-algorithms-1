import random
import math
import numpy as np
from request import Request

PROBABILITY_OF_LONG_ARRIVAL_TIME_DELTA = 0.2
PROBABILITY_OF_SHORT_ARRIVAL_TIME_DELTA = 0.2
PROBABILITY_OF_REAL_TIME_REQUEST = 0.3


def generate_requests(n_of_requests, max_disk_capacity, include_real_time=False) -> list:
    requests = []
    current_arrival_time = 0
    current_request_id = 0
    for _ in range(n_of_requests):
        arrival_time_delta = generate_random_arrival_time_delta()
        current_arrival_time += arrival_time_delta
        position = random.randint(1, max_disk_capacity)
        is_real_time = False
        deadline_real_time = None
        if include_real_time:
            random_number = random.random()
            if random_number <= PROBABILITY_OF_REAL_TIME_REQUEST:
                is_real_time = True
                deadline_real_time = generate_random_arrival_time_delta()
        request_to_add = Request(
            request_id=current_request_id,
            position=position,
            arrival_time=current_arrival_time,
            is_real_time=is_real_time,
            deadline_real_time=deadline_real_time
        )
        current_request_id += 1
        requests.append(request_to_add)
    return requests


def generate_random_arrival_time_delta():
    random_number = random.random()
    if random_number >= 1 - PROBABILITY_OF_LONG_ARRIVAL_TIME_DELTA:
        arrival_time_delta = max(math.floor(np.random.normal(500, 100)), 1)
    elif random_number <= PROBABILITY_OF_SHORT_ARRIVAL_TIME_DELTA:
        arrival_time_delta = max(math.floor(np.random.normal(100, 20)), 1)
    else:
        arrival_time_delta = max(math.floor(np.random.normal(250, 50)), 1)

    return arrival_time_delta
