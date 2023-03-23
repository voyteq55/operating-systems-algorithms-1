from collections import deque


def rr(processes: list, quantum):
    non_visible_processes = deque(processes)
    pending_processes = deque()
    finished_processes = []
    number_of_switches = 0
    time_left_within_quantum = quantum
    current_time = 0
    active_process = None

    def processes_left():
        return len(non_visible_processes) > 0 or len(pending_processes) > 0 or active_process is not None

    while processes_left():
        while len(non_visible_processes) > 0 and non_visible_processes[0].arrival_time == current_time:
            pending_processes.append(non_visible_processes.popleft())

        time_left_within_quantum -= 1

        if active_process is None and len(pending_processes) == 0:
            current_time += 1
            time_left_within_quantum = quantum
            continue

        if active_process is None:
            active_process = pending_processes.popleft()
            active_process.has_started = True

        active_process.execute()
        for process in pending_processes:
            if process.has_started:
                process.wait_between_switching()
            else:
                process.wait_as_pending()

        if active_process.is_done():
            finished_processes.append(active_process)
            if len(pending_processes) > 0:
                active_process = pending_processes.popleft()
            else:
                active_process = None
            time_left_within_quantum = quantum
            number_of_switches += 1
            current_time += 1
            continue

        if time_left_within_quantum == 0:
            pending_processes.append(active_process)
            active_process = pending_processes.popleft()
            time_left_within_quantum = quantum
            number_of_switches += 1

        current_time += 1

    results = {"finished": finished_processes, "switches": number_of_switches}

    return results



