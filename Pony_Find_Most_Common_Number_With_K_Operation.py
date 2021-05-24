def FindMostCommonNumberWithKOpteration(arr, k):
    arr.sort()
    number, count = arr[0], 0
    i, m = 0, k
    for j in range(1, len(arr)):
        m -= (arr[j] - arr[j - 1]) * (j - i)
        while i <= j and m < 0:
            m += arr[j] - arr[i]
            i += 1
        if j - i + 1 > count:
            number, count = arr[j], j - i + 1
    return number, count

if __name__ == "__main__":
    arr = [6, 3, 0, 4, 2]
    k = 7
    print(FindMostCommonNumberWithKOpteration(arr, k))
