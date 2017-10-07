from numpy import *

if __name__ == "__main__":
    a = arange(9) - 4
    b = arange(9) - 4

    for _ in range(0, 1000):
        linalg.norm(a-b)

    goal = asarray([0, 0])
    x = asarray([0, 4])
    y = asarray([2, 2])
    print linalg.norm(x - goal)
    print linalg.norm(y - goal)