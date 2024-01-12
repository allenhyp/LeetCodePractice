from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        maximum = maxCount = 0
        for task in tasks:
            counter[task] += 1
            if maximum == counter[task]:
                maxCount += 1
            elif maximum < counter[task]:
                maximum = counter[task]
                maxCount = 1
        partCount = maximum - 1
        partLength = n - (maxCount - 1)
        emptySlots = partCount * partLength
        availableTasks = len(tasks) - maximum * maxCount
        idles = max(0, emptySlots - availableTasks)
        return len(tasks) + idles
        
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = list(collections.Counter(tasks).values())
        max_cnt = max(task_cnt)
        max_tasks = task_cnt.count(max_cnt)
        return max(len(tasks), (max_cnt - 1) * (n + 1) + max_tasks)
