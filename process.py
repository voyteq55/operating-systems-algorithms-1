class Process:

    def __init__(self, process_id, arrival_time=0, time_needed_for_execution=1):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.time_needed_for_execution = time_needed_for_execution
        self.time_left = self.time_needed_for_execution
        self.time_waited_for_execution_start = 0
        self.time_from_start_to_finish = 0

    def is_done(self):
        return self.time_left <= 0

    def __str__(self):
        return f"process: arrival time - {self.arrival_time}," \
               f" time needed for execution - {self.time_needed_for_execution}"
