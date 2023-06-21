height = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [4,2,0,3,2,5]

def trap(height):
    l, r = 0, len(height) - 1
    lmax, rmax = height[l], height[r]
    A = 0
    while l < r:
        if lmax <= rmax:
            l += 1
            lmax = max(lmax, height[l])
            A += lmax - height[l]
        else:
            r -= 1
            rmax = max(rmax, height[r])
            A += rmax - height[r]
    return A

print(trap(height))
print(trap(h2))