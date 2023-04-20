import copy

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
NUMBER_OF_SIMULATIONS = 5


def perform_simulations():
    total_simulations_statistics = []
    for _ in range(6):
        total_simulations_statistics.append({"name": "", "finished": [], "disk_head_movements": 0, "unfinished": []})

    for simulation_index in range(NUMBER_OF_SIMULATIONS):
        requests = request_generator.generate_requests(NUMBER_OF_REQUESTS, MAX_DISK_CAPACITY, include_real_time=True)

        fcfs = FcfsAlgorithm(copy.deepcopy(requests), INITIAL_DISK_HEAD_POSITION, MAX_DISK_CAPACITY)
        sstf = SstfAlgorithm(copy.deepcopy(requests), INITIAL_DISK_HEAD_POSITION, MAX_DISK_CAPACITY)
        scan = ScanAlgorithm(copy.deepcopy(requests), INITIAL_DISK_HEAD_POSITION, MAX_DISK_CAPACITY)
        cscan = CScanAlgorithm(copy.deepcopy(requests), INITIAL_DISK_HEAD_POSITION, MAX_DISK_CAPACITY)
        cscan_edf = CScanEdfAlgorithm(copy.deepcopy(requests), INITIAL_DISK_HEAD_POSITION, MAX_DISK_CAPACITY)
        cscan_fdscan = CScanFDScanAlgorithm(copy.deepcopy(requests), INITIAL_DISK_HEAD_POSITION, MAX_DISK_CAPACITY)

        algorithms = [fcfs, sstf, scan, cscan, cscan_edf, cscan_fdscan]

        print(f"\n\nSymulacja nr {simulation_index + 1}")
        for algorithm, total_algorithm_stats in zip(algorithms, total_simulations_statistics):
            results = algorithm.perform_accessing()
            total_algorithm_stats["name"] = str(algorithm)
            save_to_total_statistics(results, total_algorithm_stats)
            show_algorithm_statistics(algorithm, results["finished"], results["disk_head_movements"], results.get("unfinished", None))

    show_total_simulations_statistics(total_simulations_statistics)


def save_to_total_statistics(results, total_algorithm_statistics):
    total_algorithm_statistics["finished"].extend(results["finished"])
    total_algorithm_statistics["disk_head_movements"] += results["disk_head_movements"]
    total_algorithm_statistics["unfinished"].extend(results.get("unfinished", []))


def show_algorithm_statistics(text, finished_requests, disk_head_movements, unfinished_requests=None):
    average_wait_time = sum([request.time_waited for request in finished_requests]) / len(finished_requests)
    print(f"\n{text}")
    print(f"Sredni czas oczekiwania zgloszenia: {average_wait_time}")
    print(f"Laczne przesuniecia glowicy dysku: {disk_head_movements}")
    if unfinished_requests:
        print(f"Liczba niewykonanych zgloszen czasu rzeczywistego: {len(unfinished_requests)}")


def show_total_simulations_statistics(total_simulations_statistics):
    print("\nPODSUMOWANIE")
    for algorithm_stats in total_simulations_statistics:
        finished_requests = algorithm_stats["finished"]
        unfinished_requests = algorithm_stats["unfinished"]
        average_wait_time = sum([request.time_waited for request in finished_requests]) / (len(finished_requests) * NUMBER_OF_SIMULATIONS)
        print(f"\n{algorithm_stats['name']}")
        print(f"Sredni czas oczekiwania zgloszenia: {average_wait_time}")
        print(f"Laczne przesuniecia glowicy dysku: {algorithm_stats['disk_head_movements']}")
        if unfinished_requests:
            print(f"Liczba niewykonanych zgloszen czasu rzeczywistego: {len(unfinished_requests) / NUMBER_OF_SIMULATIONS}")


