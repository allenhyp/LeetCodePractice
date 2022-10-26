package main

func checkSubarraySum(nums []int, k int) bool {
	visited := map[int]int{0: -1}
	subSum := 0
	for i, num := range nums {
		subSum = (subSum + num) % k
		if v, ok := visited[subSum]; ok {
			if i-v > 1 {
				return true
			}
		} else {
			visited[subSum] = i
		}
	}
	return false
}
