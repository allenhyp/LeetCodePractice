from heapq import heapify, heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ready = [i for i in range(n)]
        heapify(ready)
        using = []
        usage = [0] * n
        for start_time, end_time in sorted(meetings):
            while using and using[0][0] <= start_time:
                finish_time, room_number = heappop(using)
                heappush(ready, room_number)

            if ready:
                room_number = heappop(ready)
                heappush(using, (end_time, room_number))
            else:
                finish_time, room_number = heappop(using)
                heappush(using, (end_time + finish_time - start_time, room_number))
            usage[room_number] += 1

        most_used_room = most_used_times = 0
        for number, times in enumerate(usage):
            if times > most_used_times:
                most_used_room = number
                most_used_times = times
        return most_used_room
