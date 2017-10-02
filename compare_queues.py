from numpy import *

if __name__ == "__main__":
    a = arange(9) - 4
    b = arange(9) - 4

    for _ in range(0, 1000000):
        linalg.norm(a-b)