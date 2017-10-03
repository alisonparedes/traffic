if __name__ == "__main__":
    import numpy
    import itertools
    import copy
    import math

    visited = dict()

    q = numpy.asarray([1])
    domain = ((1, None), )
    phase_assignments = itertools.product(*domain)
    flows = dict()
    flows[1] = ((0, -1, 0.5), )
    goal = numpy.asarray([0])
    t = 1


    current_state = q
    arg_min = None
    min_f = float("inf")
    next_min_f = min_f

    for assignment in phase_assignments:
        new_q = copy.copy(q)

        for phase_key in assignment:

            if phase_key:
                phase = flows[phase_key]

                for flow in phase:
                    rate = flow[2]
                    from_q = flow[0]
                    to_q = flow[1]

                    change = math.floor(rate * t)
                    new_q[from_q] = q[from_q] - change
                    if new_q > 0:
                        new_q[to_q] = q[to_q] + change

        hashable_q = tuple(new_q)
        h = visited.get(hashable_q)
        if not h:
            h = numpy.linalg.norm(new_q - goal)
        f = h
        if f < min_f:
            arg_min = assignment
            next_min_f = min_f
            min_f = f

    visited[tuple(current_state)] =  next_min_f
    print arg_min