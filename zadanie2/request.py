class Request:

    def __init__(self, request_id, position, arrival_time=0, is_real_time=False, deadline_real_time=None):
        self.request_id = request_id
        self.arrival_time = arrival_time
        self.position = position
        self.time_waited = 0
        self.is_done = False
        self.is_real_time = is_real_time
        self.deadline_real_time = deadline_real_time

    def wait_as_pending(self):
        self.time_waited += 1
        if self.deadline_real_time is not None:
            self.deadline_real_time -= 1

    def execute(self):
        self.is_done = True

    def __str__(self):
        return f"{'(real time)' if self.is_real_time else ''}request: arrival time - {self.arrival_time}," \
               f" disk position - {self.position}, time waited - {self.time_waited}"

    # def __lt__(self, other):
    #     return self.time_needed_for_execution < other.time_needed_for_execution
