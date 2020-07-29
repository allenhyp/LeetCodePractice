class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = list(collections.Counter(tasks).values())
        max_cnt = max(task_cnt)
        max_tasks = task_cnt.count(max_cnt)
        return max(len(tasks), (max_cnt - 1) * (n + 1) + max_tasks)
