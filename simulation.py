import fcfs_algorithm
import sjf_algorithm
import rr_algorithm
import process_generator
import copy

NUMBER_OF_SIMULATIONS = 10
NUMBER_OF_PROCESSES = 5000

QUANTUM_1 = 15
QUANTUM_2 = 30


def start():
    def add_to_averages(algorithm_name, stats: tuple):
        final_averages[algorithm_name] = [x + (y / NUMBER_OF_SIMULATIONS) for x, y in zip(final_averages[algorithm_name], stats)]

    final_averages = {"fcfs": [0] * 5, "sjf": [0] * 5, "rr1": [0] * 5, "rr2": [0] * 5}

    for i in range(NUMBER_OF_SIMULATIONS):
        processes = process_generator.generate_processes(NUMBER_OF_PROCESSES)

        print("\nSymulacja nr " + str(i))
        results_fcfs = fcfs_algorithm.fcfs(copy.deepcopy(processes))
        stats_fcfs = calculate_simulation_results(results_fcfs)
        print("\nAlgorytm FCFS")
        show_simulation_stats(stats_fcfs)
        add_to_averages("fcfs", stats_fcfs)

        results_sjf = sjf_algorithm.sjf(copy.deepcopy(processes))
        stats_sjf = calculate_simulation_results(results_sjf)
        print("\nAlgorytm SJF (bez wywlaszczania)")
        show_simulation_stats(stats_sjf)
        add_to_averages("sjf", stats_sjf)

        results_rr_1 = rr_algorithm.rr(copy.deepcopy(processes), quantum=QUANTUM_1)
        stats_rr_1 = calculate_simulation_results(results_rr_1)
        print(f"\nAlgorytm rotacyjny z kwantem czasu k = {QUANTUM_1}")
        show_simulation_stats(stats_rr_1)
        add_to_averages("rr1", stats_rr_1)

        results_rr_2 = rr_algorithm.rr(copy.deepcopy(processes), quantum=QUANTUM_2)
        stats_rr_2 = calculate_simulation_results(results_rr_2)
        print(f"\nAlgorytm rotacyjny z kwantem czasu k = {QUANTUM_2}")
        show_simulation_stats(stats_rr_2)
        add_to_averages("rr2", stats_rr_2)

    print("\n\nPODSUMOWANIE\nWartosci srednie:")
    print("\nAlgorytm FCFS")
    show_simulation_stats(final_averages["fcfs"])
    print("\nAlgorytm SJF (bez wywlaszczania)")
    show_simulation_stats(final_averages["sjf"])
    print(f"\nAlgorytm rotacyjny z kwantem czasu k = {QUANTUM_1}")
    show_simulation_stats(final_averages["rr1"])
    print(f"\nAlgorytm rotacyjny z kwantem czasu k = {QUANTUM_2}")
    show_simulation_stats(final_averages["rr2"])


def calculate_simulation_results(results):
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

    return avg_waiting_time, avg_time_from_start_to_finish, avg_time_waited_for_execution_start, longest_waiting_time, results["switches"]


def show_simulation_stats(stats):
    print(f"{stats[0]} - Sredni laczny czas oczekiwania (od pojawienia sie procesu do zakonczenia)")
    print(f"{stats[1]} - Sredni czas od rozpoczenia do zakonczenia procesu")
    print(f"{stats[2]} - Sredni czas od pojawienia sie do rozpoczecia procesu")
    print(f"{stats[3]} - Najdluzszy laczny czas oczekiwania pojedynczego procesu")
    print(f"{stats[4]} - Laczna liczba przelaczen miedzy procesami")


