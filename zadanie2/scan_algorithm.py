import algorithm
from collections import deque


class ScanAlgorithm(algorithm.Algorithm):

    def __init__(self, requests, initial_disk_head_position, max_disk_capacity):
        super().__init__(requests, initial_disk_head_position, max_disk_capacity)

    def perform_accessing(self) -> dict:
        self.non_visible_requests = deque(self.non_visible_requests)
        self.pending_requests = [None] * (self.max_disk_capacity + 1)
        head_is_moving_right = False  # is false because it changes immediately after first iteration to True
        self.disk_head_position = 1
        while self.are_requests_left():
            while self.non_visible_requests and self.non_visible_requests[0].arrival_time == self.current_time:
                request_to_add_to_pending = self.non_visible_requests.popleft()
                self.add_to_pending(request_to_add_to_pending)

            if self.pending_requests[self.disk_head_position] is not None:
                for request in self.pending_requests[self.disk_head_position]:
                    request.execute()
                    self.finished_requests.append(request)
                self.pending_requests[self.disk_head_position] = None

            for request_list in self.pending_requests:
                if request_list:
                    for request in request_list:
                        request.wait_as_pending()

            self.current_time += 1
            if self.disk_head_position == 1 or self.disk_head_position == self.max_disk_capacity:
                head_is_moving_right = not head_is_moving_right

            if head_is_moving_right:
                self.disk_head_position += 1
            else:
                self.disk_head_position -= 1
            self.number_of_disk_head_movements += 1

        return {"finished": self.finished_requests, "disk_head_movements": self.number_of_disk_head_movements}

    def add_to_pending(self, request):
        if self.pending_requests[request.position]:
            self.pending_requests[request.position].append(request)
        else:
            self.pending_requests[request.position] = [request]

    def are_requests_left(self):
        def are_pending(requests):
            for request_list in requests:
                if request_list:
                    return True
            return False
        return self.non_visible_requests or are_pending(self.pending_requests)

    def __str__(self):
        return "SCAN"
