class Request:

    def __init__(self, request_id, position, arrival_time=0, is_real_time=False):
        self.request_id = request_id
        self.arrival_time = arrival_time
        self.position = position
        self.time_waited = 0
        self.is_done = False
        self.is_real_time = is_real_time

    def wait_as_pending(self):
        self.time_waited += 1

    def execute(self):
        self.is_done = True

    def __str__(self):
        return f"request: arrival time - {self.arrival_time}," \
               f" disk position - {self.position}, time waited - {self.time_waited}"

    # def __lt__(self, other):
    #     return self.time_needed_for_execution < other.time_needed_for_execution
