class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_count = collections.Counter(tasks).values()
        M = max(tasks_count)
        Mct = tasks_count.count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)
