class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n, t = len(image), len(image[0]), image[sr][sc]
        if t == newColor:
            return image
        def fill(i, j):
            if 0 <= i < m and 0 <= j < n and image[i][j] == t:
                image[i][j] = newColor
                fill(i - 1, j)
                fill(i, j - 1)
                fill(i + 1, j)
                fill(i, j + 1)
        fill(sr, sc)
        return image
