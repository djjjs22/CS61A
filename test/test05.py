def abs_min_index(s):

    # s = ［-4，-3，-2，3，2，4]
    # min(map(abs,s))

    abs_min = min(map(abs,s))
    return  [i for i in range(len(s)) if abs(s[i]) == abs_min]

s = [-4,-3,-2,3,2,4]
print(abs_min_index(s))

def largest_adj_sum(s):
    # >>  largest_adj_sum（ ［-4, -3, -2, 3, 2, 4］）
    # > 6
    # >>  largest_adj_sum（［-4, 3, -2, -3, 2, -4］）
    # > 1

    max(s[i] + s[i + 1] for i in range(len(s) - 1))

