# two pointer algo
def maxArea(height: list[int]) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = area if area > max_area else max_area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == '__main__':
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(heights))
