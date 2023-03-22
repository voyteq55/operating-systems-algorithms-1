from collections import deque


def fcfs(processes: list):
    non_visible_processes = deque(processes)
    pending_processes = deque()
    finished_processes = []
    number_of_switches = 0
    current_time = 0
    active_process = None

    def processes_left():
        return len(non_visible_processes) > 0 or len(pending_processes) > 0 or active_process is not None

    while processes_left():
        while len(non_visible_processes) > 0 and non_visible_processes[0].arrival_time == current_time:
            pending_processes.append(non_visible_processes.popleft())

        if active_process is not None and active_process.is_done():
            finished_processes.append(active_process)
            active_process = None
            number_of_switches += 1

        if len(pending_processes) > 0 and active_process is None:
            active_process = pending_processes.popleft()

        if active_process:
            active_process.execute()

        for process in pending_processes:
            process.wait_as_pending()

        current_time += 1

    results = {
        "finished": finished_processes,
        "pending": pending_processes,
        "active": active_process,
        "waiting_between_switches": [],
        "switches": number_of_switches
    }

    return results



