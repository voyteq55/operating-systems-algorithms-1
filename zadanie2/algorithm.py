class Algorithm:

    def __init__(self, requests, initial_disk_head_position, max_disk_capacity):
        self.requests = requests
        self.non_visible_requests = requests
        self.pending_requests = []
        self.finished_requests = []
        self.unfinished_requests = []
        self.number_of_disk_head_movements = 0
        self.disk_head_position = initial_disk_head_position
        self.max_disk_capacity = max_disk_capacity
        self.current_time = 0

    def perform_accessing(self) -> dict:
        pass

    def are_requests_left(self):
        return self.non_visible_requests or self.pending_requests
