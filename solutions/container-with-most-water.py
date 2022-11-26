def max_area(heights):
    l, r = 0, len(heights) - 1
    max_area = min(heights[r], heights[l]) * r - l
    while l <= r:
        if heights[l] >= heights[r]:
            min_ = heights[r]
            cur_area = min_ * (r - l)
            r -= 1

        elif heights[l] < heights[r]:
            min_ = heights[l]
            cur_area = min_ * (r - l)
            l += 1
        
        if cur_area > max_area:
            max_area = cur_area
    return max_area

print(max_area([1, 1]))
print(max_area([1,8,6,2,5,4,8,3,7]))

# refactor
def max_area(heights):
    l, r = 0, len(heights) - 1
    max_area = min(heights[r], heights[l]) * r - l
    while l <= r:
        if heights[l] >= heights[r]:
            cur_area = heights[r] * (r - l)
            r -= 1

        elif heights[l] < heights[r]:
            cur_area = heights[l] * (r - l)
            l += 1
        
        if cur_area > max_area:
            max_area = cur_area
    return max_area