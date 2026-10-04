from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    int1, int2, int3 = triplet
    total = int1 + int2 + int3
    return total


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    w, h, c = box_dimensions
    return w*h*c
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
