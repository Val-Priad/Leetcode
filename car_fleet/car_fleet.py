"""https://leetcode.com/problems/car-fleet/description/"""

def car_fleet(target: int, position:list[int], speed:list[int]) -> int:
    # first step we add to current position speed of each car
    while position:
        for i in range(len(position)):
            position[i] += speed[i]
        while position:
            idx = 1
            if position[idx-1] >= position[idx]:
                position.pop(idx)
                position.pop(idx-1)

