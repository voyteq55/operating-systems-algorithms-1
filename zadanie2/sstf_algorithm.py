import algorithm
from request import Request
from collections import deque


class SstfAlgorithm(algorithm.Algorithm):

    def __init__(self, requests, initial_disk_head_position, max_disk_capacity):
        super().__init__(requests, initial_disk_head_position, max_disk_capacity)

    def perform_accessing(self) -> dict:
        self.non_visible_requests = deque(self.non_visible_requests)
        next_request: Request = None
        while self.are_requests_left():
            while self.non_visible_requests and self.non_visible_requests[0].arrival_time == self.current_time:
                self.pending_requests.append(self.non_visible_requests.popleft())

            if not next_request and self.pending_requests:
                next_request = self.find_shortest_seek_time_request()

            if next_request:
                if next_request.position < self.disk_head_position:
                    self.disk_head_position -= 1
                elif next_request.position > self.disk_head_position:
                    self.disk_head_position += 1
                next_request.wait_as_pending()
                self.number_of_disk_head_movements += 1

                while next_request and next_request.position == self.disk_head_position:
                    next_request.execute()
                    self.finished_requests.append(next_request)
                    if self.pending_requests:
                        next_request = self.find_shortest_seek_time_request()
                    else:
                        next_request = None

            for request in self.pending_requests:
                request.time_waited += 1

            self.current_time += 1

        return {"finished": self.finished_requests, "disk_head_movements": self.number_of_disk_head_movements}

    def find_shortest_seek_time_request(self):
        self.pending_requests.sort(key=lambda request: abs(request.position - self.disk_head_position))
        return self.pending_requests.pop(0)
