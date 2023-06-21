height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height):
    l, r = 0, len(height) - 1
    lh, rh = 0, 0
    A, lA, rA = 0, 0, 0
    while l <= r:
        if height[l] >= height[lh]:
            A += min(height[l], height[lh]) * (l - lh - 1) - lA
            lh = l
            l += 1
        elif height[l] < height[lh]:
            lA += height[l]
            l += 1
        if height[r] >= height[rh]:
            A += min(height[r], height[rh]) * (rh - r - 1) - rA
            rh = r
            r -= 1
        elif height[r] < height[rh]:
            rA += height[r]
            r -= 1
    return A

print(trap(height))