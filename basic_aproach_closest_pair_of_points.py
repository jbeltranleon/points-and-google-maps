# Computing minimum distance between 2 points on a 2d plane
# https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2


def solution(x, y):
    print('--- solution ---'.upper())
    a = list(zip(x, y))  # This produces list of tuples
    print(x,y)
    print(f'Parejas de puntos {a}')
    ax = sorted(a, key=lambda x: x[0])  # Presorting x-wise
    ay = sorted(a, key=lambda x: x[1])  # Presorting y-wise

    print(f'sorted ax: {ax}\nsorted ay: {ay}')
    print('-call next func-\n\n'.upper())
    p1, p2, mi = closest_pair(ax, ay)  # Recursive D&C function
    print(f'\n\nNearest points: \np1 = {p1} and p2={p2}')
    print('----- end ------'.upper())
    return mi

def closest_pair(ax, ay):
    print('- closest_pair -'.upper())
    ln_ax = len(ax)  # It's quicker to assign variable
    print(f'len of ax = ln_ax = {ln_ax}')
    if ln_ax <= 3:
        print('*WARNING*: We are using a brute comparison')
        print('-call next func-\n\n'.upper())
        return brute(ax)  # A call to bruteforce comparison
    mid = ln_ax // 2  # Division without remainder, need int
    Qx = ax[:mid]  # Two-part split
    Rx = ax[mid:]
    # Determine midpoint on x-axis
    midpoint = ax[mid][0]  
    Qy = list()
    Ry = list()
    for x in ay:  # split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
           Qy.append(x)
        else:
           Ry.append(x)
    # Call recursively both arrays after split
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)
    # Determine smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)
    # Call function to account for points on the boundary
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
    # Determine smallest distance for the array
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3

def brute(ax):
    print('---- brute -----'.upper())
    print(f'ax vector = {ax}')
    print('-call next func-\n\n'.upper())
    mi = dist(ax[0], ax[1])
    print(f'mi = {mi}')
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        print('*WARNING*: The process just include 2 points')
        return p1, p2, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                print('**Alert** Process to iterate all of points')
                print('-call next func-\n\n'.upper())
                d = dist(ax[i], ax[j])
                print(f'd = {d}')
                if d < mi:  # Update min_dist and points
                    print('**Alert** Points are updated')
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi

import math
def dist(p1, p2):
    print('----- dist -----'.upper())
    print(f'p1={p1}\np2={p2}')
    # Equation of distance between two points
    print('d = √(x1-x2)^2 + (y1-y2)^2')
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)  # store length - quicker
    mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array
    # Create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta  # assign best value to delta
    ln_y = len(s_y)  # store length of subarray for quickness
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

import random
def test_case(length: int = 5):
    lst1 = [random.randint(-10**9, 10**9) for i in range(length)]
    lst2 = [random.randint(-10**9, 10**9) for i in range(length)]
    return lst1, lst2

if __name__ == "__main__":
    x = [30,20,60]
    y = [40,50,90]
    print(solution(x, y))

    

