'''States are represented by a set of queues.
Queues can be a tuple to make lookups fast (I hope).
They store integers.
So I can compare queues quickly.
I'm not sure if the sink needs to be in the queue.
Hash queues to store updated h(n)
How bad is hashing a tuple? '''


if __name__ == "__main__":
    better_h = dict()
    import numpy
    q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    goal = [0] * 20
    hashable_q = tuple(q)
    for _ in range(0, 1000000):
        better_h[hashable_q] = 1
        if not better_h.get(hashable_q):
            numpy.linalg.norm(goal - q)



