def number_of_items(s: str, ranges: List[List[int]]) -> List[int]:
    # Idea: Use three arrays to achieve what Treemap stores but has a faster run-time
    # 012345678 idx
    # **|**|*|*
    # --2225577 left
    # 22255577- right
    # 000002233 preSum
    # Runtime: O(n + s)
    n = len(s)
    containerStart = -1
    count, presum, left, right = 0, [0] * n, [0] * n, [0] * n
    for i in range(n):
        if s[i] == '|':
            containerStart = i
            presum[i] = count
        elif containerStart >= 0:
            count += 1
            presum[i] = presum[i - 1] if i > 0 else 0
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            right[i] = i
        else:
            right[i] = right[i + 1] if i < n - 1 else -1
    for i in range(n):
        if s[i] == '|':
            left[i] = i
        else:
            left[i] = left[i - 1] if i > 0 else -1
    res = []
    for r in ranges:
        rightIdx = left[r[1]]
        leftIdx = right[r[0]]
        if rightIdx != -1 and leftIdx != -1 and leftIdx < rightIdx:
            res.append(presum[rightIdx] - presum[leftIdx])
        else:
            res.append(0)
    
    return res

if __name__ == '__main__':
    s = input()
    ranges = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = number_of_items(s, ranges)
    print(' '.join(map(str, res)))
