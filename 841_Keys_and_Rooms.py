class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = set()
        keys = [0]
        while keys:
            room = keys.pop()
            for key in rooms[room]:
                if key in opened:
                    continue
                keys.append(key)
            opened.add(room)
        return len(opened) == len(rooms)
