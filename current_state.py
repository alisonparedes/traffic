if __name__ == "__main__":
    queues = (10, 0, 0, 0)

    # Phases, times and capacities are constraints on next states. They affect which actions are available in the current state and consiquently
    # Time to goal so I think they need to be part of the state definition. Hmm.... They affect the simulation. Should help prevent some cycles.
    phases = (1, )
    times = (10, )
    capacity = (-9, 1, 1, 1)

    # Phase cycles never change. Do this once.
    phase_cycles = dict()
    phase_cycles[(1, 1)] = 2

    phase_min = dict()
    phase_min[(1, 1)] = 5

    phase_max = dict()
    phase_max[(1, 1)] = 10

    phase_intergreen = dict()
    phase_intergreen[(1, 1)] = 5

    phase_rate = dict()
    phase_rate[(1, 1)] = 0.21875

    phase_queues = dict()
    phase_queues[(1, 1)] = (1, 2)

    # Capacities never change. Do this once.
    max_capacity = dict()
    max_capacity[1] = 35
    max_capacity[2] = 101
    max_capacity[3] = 138
    max_capacity[4] = 61

    goal = (0, 0, 0, 0)

    visited = dict()

    import numpy
    for _ in range(100000):
        h = numpy.linalg.norm(numpy.asarray(queues) - numpy.asarray(goal))
        visited[(queues, phases, times)] = h
    print h
    print visited

    for i, phase in phases:
        phase_queues[(i, phase)]