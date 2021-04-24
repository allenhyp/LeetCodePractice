def closestOccurance(s, queries):
    n = len(s)
    last = {}                                               # Last occurance index of the character
    closest = [-1] * n                                      # Closest occurance, updated in every iteration 
    for i, c in enumerate(s):                               # Time complexity: O(n), space complexity: O(n)
        if c in last:
            if closest[last[c]] == -1:
                closest[last[c]] = i
            else:
                left = abs(closest[last[c]] - last[c])
                right = abs(last[c] - i)
                if left > right:
                    closest[last[c]] = i
            closest[i] = last[c]
        last[c] = i

    ret = []
    for q in queries:                                       # Time needed for every query: O(1)
        if 0 <= q < n:
            ret.append(closest[q])
        else:
            ret.append(-1)

    return ret                                              # Total time complexity: O(n + queries)


s = 'hackerrarrank'
queries = [4, 5, 6, 7, 8, 11]
print(closestOccurance(s, queries))
