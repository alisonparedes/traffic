
if __name__ == "__main__":
    import random
    for _ in range(20):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000 - a)
        c = 1000 - a - b
        print "{0}, {1}, {2}".format(a, b, c)
