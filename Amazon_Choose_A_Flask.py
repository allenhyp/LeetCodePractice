from typing import List

def choose_a_flask(num_orders: int, requirements: List[int], flask_types: int, markings: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    flask_map = {}
    for flask_type, marking in markings:
        if flask_type in flask_map:
            flask_map[flask_type].append(marking)
        else:
            flask_map[flask_type] = [marking]
    for flask_type in flask_map.keys():
        flask_map[flask_type].sort()
    
    def binary_search(markings, requirement):
        left, right = 0, len(markings)
        while left < right:
            mid = (left + right) // 2
            if markings[mid] == requirement:
                return mid
            elif markings[mid] < requirement:
                left = mid + 1
            else:
                right = mid - 1
        return right

    res, minWaste = -1, float('inf')
    for flask_type, flask_markings in flask_map.items():
        waste = 0
        for requirement in requirements:
            target = binary_search(flask_markings, requirement)
            if target >= len(flask_markings):
                waste = -1
                break
            else:
                waste += flask_markings[target] - requirement
        if waste != -1 and waste < minWaste:
            res = flask_type
            minWaste = waste
    return res

if __name__ == '__main__':
    num_orders = int(input())
    requirements = [int(x) for x in input().split()]
    flask_types = int(input())
    markings = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = choose_a_flask(num_orders, requirements, flask_types, markings)
    print(res)
