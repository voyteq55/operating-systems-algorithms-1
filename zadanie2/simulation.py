import copy

from algorithm import Algorithm
import request_generator
from fcfs_algorithm import FcfsAlgorithm
from sstf_algorithm import SstfAlgorithm
from scan_algorithm import ScanAlgorithm
from cscan_algorithm import CScanAlgorithm
from cscan_edf_algorithm import CScanEdfAlgorithm
from cscan_fdscan_algorithm import CScanFDScanAlgorithm

INITIAL_DISK_HEAD_POSITION = 500
MAX_DISK_CAPACITY = 1000
NUMBER_OF_REQUESTS = 1000


def perform_simulation():

    requests = request_generator.generate_requests(NUMBER_OF_REQUESTS, MAX_DISK_CAPACITY, include_real_time=True)
    for r in requests:
        print(r)

    sstf = CScanEdfAlgorithm(
        requests=copy.deepcopy(requests),
        initial_disk_head_position=INITIAL_DISK_HEAD_POSITION,
        max_disk_capacity=MAX_DISK_CAPACITY
    )
    fcfs_results = sstf.perform_accessing()
    finished = fcfs_results["finished"]
    for f in finished:
        print(f)
    print(fcfs_results["disk_head_movements"])
    print(f"suma czasu ocz. - {sum([x.time_waited for x in finished])}")
    print(f"skonczone - {len(finished)}")
    print(f"niesskonczone - {len(fcfs_results['unfinished'])}")
