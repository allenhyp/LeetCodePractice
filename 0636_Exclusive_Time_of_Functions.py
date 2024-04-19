class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        record = [0] * n
        stack = []
        current_time = 0

        for log in logs:
            id, op, timestamp = log.split(':')
            id, timestamp = int(id), int(timestamp)
            
            if op == 'start':
                if len(stack) > 0:
                    record[stack[-1]] += timestamp - current_time
                stack.append(id)
                current_time = timestamp
            else:
                record[stack.pop()] += timestamp - current_time + 1
                current_time = timestamp + 1

        return record
