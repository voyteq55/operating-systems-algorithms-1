import algorithm
from collections import deque


class CScanFDScanAlgorithm(algorithm.Algorithm):

    def __init__(self, requests, initial_disk_head_position, max_disk_capacity):
        super().__init__(requests, initial_disk_head_position, max_disk_capacity)
        self.pending_real_time_requests = []

    def perform_accessing(self) -> dict:
        self.non_visible_requests = deque(self.non_visible_requests)
        self.pending_requests = [None] * (self.max_disk_capacity + 1)
        self.disk_head_position = 1
        while self.are_requests_left():
            while self.non_visible_requests and self.non_visible_requests[0].arrival_time == self.current_time:
                request_to_add_to_pending = self.non_visible_requests.popleft()
                if request_to_add_to_pending.is_real_time:
                    self.pending_real_time_requests.append(request_to_add_to_pending)
                else:
                    self.add_to_pending(request_to_add_to_pending)

            self.pending_real_time_requests.sort(key=lambda real_time_request: real_time_request.deadline_real_time)
            while self.pending_real_time_requests and self.pending_real_time_requests[0].deadline_real_time < abs(self.pending_real_time_requests[0].position - self.disk_head_position):
                self.unfinished_requests.append(self.pending_real_time_requests.pop(0))

            if self.pending_real_time_requests:
                if self.pending_real_time_requests[0].position < self.disk_head_position:
                    self.disk_head_position -= 1
                elif self.pending_real_time_requests[0].position > self.disk_head_position:
                    self.disk_head_position += 1

                if self.disk_head_position == self.pending_real_time_requests[0].position:
                    self.pending_real_time_requests[0].execute()
                    self.finished_requests.append(self.pending_real_time_requests.pop(0))
            else:
                if self.disk_head_position == self.max_disk_capacity:
                    self.disk_head_position = 0
                self.disk_head_position += 1

            if self.pending_requests[self.disk_head_position] is not None:
                for request in self.pending_requests[self.disk_head_position]:
                    request.execute()
                    self.finished_requests.append(request)
                self.pending_requests[self.disk_head_position] = None

            for request_list in self.pending_requests:
                if request_list:
                    for request in request_list:
                        request.wait_as_pending()

            for request in self.pending_real_time_requests:
                request.wait_as_pending()
                if request.deadline_real_time == 0:
                    self.unfinished_requests.append(request)
                    self.pending_real_time_requests.remove(request)

            self.current_time += 1
            self.number_of_disk_head_movements += 1

        return {"finished": self.finished_requests, "unfinished": self.unfinished_requests, "disk_head_movements": self.number_of_disk_head_movements}

    def add_to_pending(self, request):
        if self.pending_requests[request.position]:
            self.pending_requests[request.position].append(request)
        else:
            self.pending_requests[request.position] = [request]

    def are_requests_left(self) -> bool:
        def are_pending(requests):
            for request_list in requests:
                if request_list:
                    return True
            return False
        return self.non_visible_requests or self.pending_real_time_requests or are_pending(self.pending_requests)

    def __str__(self):
        return "C-SCAN (FD-SCAN)"
