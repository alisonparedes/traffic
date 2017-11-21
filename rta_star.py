import numpy
import itertools
import copy
import heapq
import logging
import time
import os
import state
import transition
import random


def get_intersection(best):
    f = best[0]
    intersection, phase = best[1]
    return intersection


def get_phase(best):
    f = best[0]
    intersection, phase = best[1]
    return phase


def random_next(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    actions = state.applicable_actions(current_intersections, cycles=True)
    for intersection, domain in actions.iteritems():
        apply = random.randint(0, len(domain)-1)
        current_phase = current_intersections[intersection][0]
        current_time = current_intersections[intersection][1]
        new_time = current_time + interval
        if domain[apply] != current_phase:
            new_time = interval
        next_intersections[intersection] = (domain[apply], new_time)
    return next_intersections, next_best_h


def breadth_first_d1(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    #print(next_best_h)
    actions = state.applicable_actions(current_intersections, cycles=True)
    next_states = itertools.product(*actions.itervalues())
    for try_state in next_states:
        try_intersections = copy.copy(current_intersections)
        for phase in try_state:
            intersection = phase[0:5]
            current_phase = current_intersections[intersection][0]
            current_time = current_intersections[intersection][1]
            new_time = current_time + interval
            if phase != current_phase:
                new_time = interval
            try_intersections[phase[0:5]] = (phase, new_time)
        active_flows = state.get_rates(try_intersections, current_intersections, interval)
        max_flows = transition.maximize_flows(active_flows, current_queues)
        successor_queues = state.simulate(current_queues, max_flows)
        try_h = state.heuristic(successor_queues, goal)
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
            #print(next_best_h)
    return next_intersections, next_best_h


def breadth_first_d1_learn(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    #print(next_best_h)
    actions = state.applicable_actions(current_intersections, cycles=True)
    next_states = itertools.product(*actions.itervalues())
    for try_state in next_states:
        try_intersections = copy.copy(current_intersections)
        for phase in try_state:
            intersection = phase[0:5]
            current_phase = current_intersections[intersection][0]
            current_time = current_intersections[intersection][1]
            new_time = current_time + interval
            if phase != current_phase:
                new_time = interval
            try_intersections[phase[0:5]] = (phase, new_time)
        active_flows = state.get_rates(try_intersections, current_intersections, interval)
        max_flows = transition.maximize_flows(active_flows, current_queues)
        successor_queues = state.simulate(current_queues, max_flows)
        try_h = visited.get(classify_state(try_intersections), state.heuristic(successor_queues, goal))
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
            #print(next_best_h)
    return next_intersections, next_best_h


def prev_duration(intersection, new_phase, current_intersections):
    current_phase = current_intersections[intersection][0]
    if new_phase != current_phase:
        return 0
    current_duration = current_intersections[intersection][1]
    return current_duration


def beam_d2(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    depth_1 = expand_best(current_queues, current_intersections, interval)
    depth_2 = []
    for current_intersections, current_queues, _ in depth_1:
        depth_2 += expand(current_queues, current_intersections, interval)
    for _, try_queues, try_intersections in depth_2:
        try_h = state.heuristic(try_queues, goal)
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
    return next_intersections, next_best_h


def expand_best(current_queues, current_intersections, interval, beam_len=5):
    generated = []
    best = []
    actions = state.applicable_actions(current_intersections, cycles=True)
    next_states = itertools.product(*actions.itervalues())
    for try_state in next_states:
        try_intersections = copy.copy(current_intersections)
        for phase in try_state:
            intersection = phase[0:5]
            try_intersections[intersection] = (phase, prev_duration(intersection, phase, current_intersections) + interval)
        active_flows = state.get_rates(try_intersections, current_intersections, interval)
        max_flows = transition.maximize_flows(active_flows, current_queues)
        try_queues = state.simulate(current_queues, max_flows)
        #state.print_change(current_queues, try_queues)
        try_h = state.heuristic(try_queues, goal)
        heapq.heappush(best, (try_h, (try_intersections, try_queues, current_intersections)))
    i = 0
    while i < beam_len and i < len(best):
        min_h, min_state = heapq.heappop(best)
        generated.append(min_state)
        i += 1
    return generated


def breadth_first_d2(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    depth_1 = expand(current_queues, current_intersections, interval)
    depth_2 = []
    for current_intersections, current_queues, _ in depth_1:
        depth_2 += expand(current_queues, current_intersections, interval)
    for _, try_queues, try_intersections in depth_2:
        try_h = state.heuristic(try_queues, goal)
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
    return next_intersections, next_best_h


def expand(current_queues, current_intersections, interval):
    generated = []
    actions = state.applicable_actions(current_intersections, cycles=True)
    next_states = itertools.product(*actions.itervalues())
    for try_state in next_states:
        try_intersections = copy.copy(current_intersections)
        for phase in try_state:
            intersection = phase[0:5]
            try_intersections[intersection] = (phase, prev_duration(intersection, phase, current_intersections) + interval)
        active_flows = state.get_rates(try_intersections, current_intersections, interval)
        max_flows = transition.maximize_flows(active_flows, current_queues)
        try_queues = state.simulate(current_queues, max_flows)
        generated.append((try_intersections, try_queues, current_intersections))
    return generated


def expand_b8(current_queues, current_intersections, interval, cycles=True, learn=False):
    generated = []
    actions = state.applicable_actions(current_intersections, cycles)
    must_intersections = {intersection: (phase[0], phase[1] + interval) for intersection, phase in current_intersections.iteritems()}
    for intersection, phases in actions.iteritems():
        if len(phases) == 1:
            must_intersections[intersection] = (phases[0], prev_duration(intersection, phases[0], current_intersections) + interval)
    for intersection, phases in actions.iteritems():
        best_h = float("inf")
        best_intersections = None
        best_queues = None
        for phase in phases:
            if phase != must_intersections[intersection][0]:
                try_intersections = copy.copy(must_intersections)
                try_intersections[intersection] = (phase, prev_duration(intersection, phase, current_intersections) + interval)
                active_flows = state.get_rates(try_intersections, current_intersections, interval)
                max_flows = transition.maximize_flows(active_flows, current_queues)
                try_queues = state.simulate(current_queues, max_flows)
                if learn:
                    try_h = visited.get(classify_state(try_intersections), state.heuristic(try_queues, goal))
                else:
                    try_h = state.heuristic(try_queues, goal)
                if try_h < best_h:
                    best_h = try_h
                    best_intersections = try_intersections
                    best_queues = try_queues
        if best_h < float("inf"):
            generated.append((best_intersections, best_queues, current_intersections))


    if len(generated) == 0:
        active_flows = state.get_rates(must_intersections, current_intersections, interval)
        max_flows = transition.maximize_flows(active_flows, current_queues)
        try_queues = state.simulate(current_queues, max_flows)
        generated.append((must_intersections, try_queues, current_intersections))

    return generated


def breadth_first_b8(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    depth_1 = expand_b8(current_queues, current_intersections, interval)
    depth_2 = []
    for d1_intersections, d1_queues, _ in depth_1:
        depth_2 += expand_b8(d1_queues, d1_intersections, interval)
    for _, try_queues, try_intersections in depth_2:
        try_h = state.heuristic(try_queues, goal)
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
    return next_intersections, next_best_h


def greedy_b8(current_queues, current_intersections, interval=10, cycles=False):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    depth_1 = expand_b8(current_queues, current_intersections, interval, cycles)
    depth_2 = []
    for d1_intersections, d1_queues, _ in depth_1:
        depth_2 += expand_b8(d1_queues, d1_intersections, interval, cycles)
    for _, try_queues, try_intersections in depth_2:
        try_h = state.heuristic(try_queues, goal)
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
    return next_intersections, next_best_h


def greedy_b8_learn(current_queues, current_intersections, interval=10, cycles=False, learn=True):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    depth_1 = expand_b8(current_queues, current_intersections, interval, cycles, learn)
    depth_2 = []
    for d1_intersections, d1_queues, _ in depth_1:
        depth_2 += expand_b8(d1_queues, d1_intersections, interval, cycles, learn)
    for _, try_queues, try_intersections in depth_2:
        if learn:
            try_h = visited.get(classify_state(try_intersections), state.heuristic(try_queues, goal))
        else:
            try_h = state.heuristic(try_queues, goal)
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
    return next_intersections, next_best_h


def leader_first(current_queues, current_intersections, interval=10):
    successor_intersections = copy.copy(current_intersections)
    successor_queues = current_queues
    for intersection in current_intersections.iterkeys():
        #print(intersection)
        actions = state.applicable_actions(successor_intersections)
        current_phase = successor_intersections[intersection][0]
        current_time = successor_intersections[intersection][1]
        next_best_h = float("inf")
        next_intersections = None
        next_queues = None
        for phase in actions[intersection]:
            #print(phase)
            new_time = current_time + interval
            if phase != current_phase:
                new_time = interval
            try_intersections = copy.copy(successor_intersections)
            try_intersections[intersection] = (phase, new_time)
            active_flows = state.get_rates(try_intersections, successor_intersections, interval)
            max_flows = transition.maximize_flows(active_flows, successor_queues)
            try_queues = state.simulate(successor_queues, max_flows)
            try_h = visited.get(classify_state(try_intersections), state.heuristic(try_queues, goal))
            #try_h = state.heuristic(try_queues, goal)
            #print(try_h)
            if try_h < next_best_h:
                next_best_h = try_h
                next_intersections = try_intersections
                next_queues = try_queues
        successor_queues = next_queues
        successor_intersections = next_intersections
    return successor_intersections, next_best_h


def classify_state(intersections):
    return tuple(x for x, y in intersections.itervalues())


def rta_star(initial_queues, initial_intersections, search=random_next):
    current_queues = initial_queues
    current_intersections = initial_intersections
    execution_time = 0
    #max_search_time = 0
    interval = 10
    #search = leader_first
    #search = random_next
    #search = breadth_first_d1
    #search = breadth_first_d2
    #search = breadth_first_b8
    #print(current_queues)
    #print(goal)
    while not state.is_goal(goal, current_queues):
        start_time = time.clock()
        next_intersections, new_h = search(current_queues, current_intersections)
        end_time = time.clock()-start_time
        print(end_time)
        #print(next_intersections)
        rates = state.get_rates(next_intersections, current_intersections, interval)
        #print(current_queues)
        max_flows = transition.maximize_flows(rates, current_queues)
        #print(max_flows)
        next_queues = state.simulate(current_queues, max_flows)
        #print(next_intersections)
        #state.print_change(current_queues, next_queues)
        visited[classify_state(current_intersections)] = new_h + 1
        current_queues = next_queues
        current_intersections = next_intersections
        #print(state.heuristic(next_queues, goal))
        #print(visited)
        execution_time += interval
        #print(next_intersections)
        #print(current_queues)
        #print("max search time per iteration so far (seconds): {0}".format(max_search_time))
    #print(current_state)
    #print("execution time (seconds): {0}".format(execution_time))
    #print("max search time per iteration (seconds): {0}".format(max_search_time))
    return execution_time


def quick_domain(in_queues, out_queues, exceptions):
    rates = (1, )
    phases = []
    for phase in itertools.product(in_queues, out_queues, rates):
        in_queue = phase[0]
        out_queue = phase[1]
        rate = phase[2]
        if exceptions.get((in_queue, out_queue)):
            rate = 0
        phases.append((in_queue, out_queue, rate))
    return phases

if __name__ == "__main__":

    '''
    domains = []
    domains.append((quick_domain([1, 2, 3, 4], [5, 24, 28, 29], {(3, 5): True, (4, 24): True, (1, 28): True, (2, 29): True}), [1, 2, 3, 4]))
    domains.append((quick_domain([5, 6, 7, 8], [3, 9, 20, 30], {(6, 30): True, (5, 3): True, (7, 9): True, (8, 20): True}), [5, 6, 7, 8]))
    domains.append((quick_domain([9, 10, 11, 12],  [7, 13, 31], {(9, 7): True, (12, 13): True, (10, 31): True}), [9, 10, 11, 12]))
    domains.append((quick_domain([13, 14, 15], [12, 17, 32], {(13, 12): True, (14, 32): True, (15, 17): True}), [13, 14, 15]))
    domains.append((quick_domain([16, 17, 18], [15, 21, 27], {(17, 15): True, (16, 21): True}), [16, 17, 18]))
    domains.append((quick_domain([19, 20, 21, 22], [8, 16, 25, 33], {(20, 8): True, (21, 16): True, (22, 33): True, (19, 25): True}), [19, 20, 21, 22]))
    domains.append((quick_domain([23, 24, 25, 26], [19, 4, 34, 35], {(24, 4): True, (25, 19): True, (26, 34): True, (23, 35): True}), [23, 24, 25, 26]))
    domains.append((quick_domain([27], [0], dict()), [27]))
    domains.append((quick_domain([28], [0], dict()), [28]))
    domains.append((quick_domain([29], [0], dict()), [29]))
    domains.append((quick_domain([30, 31], [0], dict()), [30, 31]))
    domains.append((quick_domain([32], [0], dict()), [32]))
    domains.append((quick_domain([33, 34], [0], dict()), [33, 34]))
    domains.append((quick_domain([35], [0], dict()), [35]))
    sink = 1
    queues = 35 + sink
    #print(domains)
    '''
    import datetime
    #a, b, c, search_alg = 300.0, 152.0, 357.0, breadth_first_d1  #Example from PDDL
    #a, b, c, search_alg = 200, 152.0, 357.0, breadth_first_d1
    #a, b, c, search_alg = 891, 75, 34, breadth_first_d1
    #a, b, c, search_alg = 411, 539, 50, breadth_first_d1
    #a, b, c, search_alg = 487, 491, 22, breadth_first_d1
    #a, b, c, search_alg = 149, 572, 279, breadth_first_d1
    #a, b, c, search_alg = 835, 39, 126, breadth_first_d1
    #a, b, c, search_alg = 388, 252, 360, breadth_first_d1
    #a, b, c, search_alg = 178, 660, 162, breadth_first_d1
    #a, b, c, search_alg = 266, 317, 417, breadth_first_d1
    #a, b, c, search_alg = 940, 13, 47, breadth_first_d1
    #a, b, c, search_alg = 763, 122, 115, breadth_first_d1
    #a, b, c, search_alg = 491, 45, 464, breadth_first_d1
    #a, b, c, search_alg = 568, 327, 105, breadth_first_d1
    #a, b, c, search_alg = 713, 92, 195, breadth_first_d1
    #a, b, c, search_alg = 401, 98, 501, breadth_first_d1
    #a, b, c, search_alg = 308, 327, 365, breadth_first_d1
    #a, b, c, search_alg = 862, 48, 90, breadth_first_d1
    #a, b, c, search_alg = 133, 209, 658, breadth_first_d1
    #a, b, c, search_alg = 456, 421, 123, breadth_first_d1
    #a, b, c, search_alg = 44, 32, 924, breadth_first_d1


    #a, b, c, search_alg = 200, 152.0, 357.0, random_next
    #a, b, c, search_alg = 891, 75, 34, random_next
    #a, b, c, search_alg = 411, 539, 50, random_next
    #a, b, c, search_alg = 487, 491, 22, random_next
    #a, b, c, search_alg = 149, 572, 279, random_next
    #a, b, c, search_alg = 835, 39, 126, random_next
    #a, b, c, search_alg = 388, 252, 360, random_next
    #a, b, c, search_alg = 178, 660, 162, random_next
    #a, b, c, search_alg = 266, 317, 417, random_next
    #a, b, c, search_alg = 940, 13, 47, random_next
    #a, b, c, search_alg = 763, 122, 115, random_next
    #a, b, c, search_alg = 491, 45, 464, random_next
    #a, b, c, search_alg = 568, 327, 105, random_next
    #a, b, c, search_alg = 713, 92, 195, random_next
    #a, b, c, search_alg = 401, 98, 501, random_next
    #a, b, c, search_alg = 308, 327, 365, random_next
    #a, b, c, search_alg = 862, 48, 90, random_next
    #a, b, c, search_alg = 133, 209, 658, random_next
    #a, b, c, search_alg = 456, 421, 123, random_next
    #a, b, c, search_alg = 44, 32, 924, random_next


    #a, b, c, search_alg = 200, 152.0, 357.0, breadth_first_b8
    #a, b, c, search_alg = 891, 75, 34, breadth_first_b8
    #a, b, c, search_alg = 411, 539, 50, breadth_first_b8
    #a, b, c, search_alg = 487, 491, 22, breadth_first_b8
    #a, b, c, search_alg = 149, 572, 279, breadth_first_b8
    #a, b, c, search_alg = 835, 39, 126, breadth_first_b8
    #a, b, c, search_alg = 388, 252, 360, breadth_first_b8
    #a, b, c, search_alg = 178, 660, 162, breadth_first_b8
    #a, b, c, search_alg = 266, 317, 417, breadth_first_b8
    #a, b, c, search_alg = 940, 13, 47, breadth_first_b8
    #a, b, c, search_alg = 763, 122, 115, breadth_first_b8
    #a, b, c, search_alg = 491, 45, 464, breadth_first_b8
    #a, b, c, search_alg = 568, 327, 105, breadth_first_b8
    #a, b, c, search_alg = 713, 92, 195, breadth_first_b8
    #a, b, c, search_alg = 401, 98, 501, breadth_first_b8
    #a, b, c, search_alg = 308, 327, 365, breadth_first_b8
    #a, b, c, search_alg = 862, 48, 90, breadth_first_b8
    #a, b, c, search_alg = 133, 209, 658, breadth_first_b8
    #a, b, c, search_alg = 456, 421, 123, breadth_first_b8
    #a, b, c, search_alg = 44, 32, 924, breadth_first_b8


    #a, b, c, search_alg = 200, 152.0, 357.0, breadth_first_d1_learn
    #a, b, c, search_alg = 891, 75, 34, breadth_first_d1_learn
    #a, b, c, search_alg = 411, 539, 50, breadth_first_d1_learn
    #a, b, c, search_alg = 487, 491, 22, breadth_first_d1_learn
    #a, b, c, search_alg = 149, 572, 279, breadth_first_d1_learn
    #a, b, c, search_alg = 835, 39, 126, breadth_first_d1_learn
    #a, b, c, search_alg = 388, 252, 360, breadth_first_d1_learn
    #a, b, c, search_alg = 178, 660, 162, breadth_first_d1_learn
    #a, b, c, search_alg = 266, 317, 417, breadth_first_d1_learn
    #a, b, c, search_alg = 940, 13, 47, breadth_first_d1_learn
    #a, b, c, search_alg = 763, 122, 115, breadth_first_d1_learn
    #a, b, c, search_alg = 491, 45, 464, breadth_first_d1_learn
    #a, b, c, search_alg = 568, 327, 105, breadth_first_d1_learn
    #a, b, c, search_alg = 713, 92, 195, breadth_first_d1_learn
    #a, b, c, search_alg = 401, 98, 501, breadth_first_d1_learn
    #a, b, c, search_alg = 308, 327, 365, breadth_first_d1_learn
    #a, b, c, search_alg = 862, 48, 90, breadth_first_d1_learn
    #a, b, c, search_alg = 133, 209, 658, breadth_first_d1_learn
    #a, b, c, search_alg = 456, 421, 123, breadth_first_d1_learn
    #a, b, c, search_alg = 44, 32, 924, breadth_first_d1_learn


    #a, b, c, search_alg = 200, 152.0, 357.0, breadth_first_d2
    #a, b, c, search_alg = 891, 75, 34, breadth_first_d2
    #a, b, c, search_alg = 411, 539, 50, breadth_first_d2
    #a, b, c, search_alg = 487, 491, 22, breadth_first_d2
    #a, b, c, search_alg = 149, 572, 279, breadth_first_d2
    #a, b, c, search_alg = 835, 39, 126, breadth_first_d2
    #a, b, c, search_alg = 388, 252, 360, breadth_first_d2
    #a, b, c, search_alg = 178, 660, 162, breadth_first_d2
    #a, b, c, search_alg = 266, 317, 417, breadth_first_d2
    #a, b, c, search_alg = 940, 13, 47, breadth_first_d2
    #a, b, c, search_alg = 763, 122, 115, breadth_first_d2
    #a, b, c, search_alg = 491, 45, 464, breadth_first_d2
    #a, b, c, search_alg = 568, 327, 105, breadth_first_d2
    #a, b, c, search_alg = 713, 92, 195, breadth_first_d2
    #a, b, c, search_alg = 401, 98, 501, breadth_first_d2
    #a, b, c, search_alg = 308, 327, 365, breadth_first_d2
    #a, b, c, search_alg = 862, 48, 90, breadth_first_d2
    #a, b, c, search_alg = 133, 209, 658, breadth_first_d2
    #a, b, c, search_alg = 456, 421, 123, breadth_first_d2
    #a, b, c, search_alg = 44, 32, 924, breadth_first_d2

    #a, b, c, search_alg = 200, 152.0, 357.0, beam_d2
    a, b, c, search_alg = 891, 75, 34, beam_d2
    #a, b, c, search_alg = 411, 539, 50, breadth_first_d2
    #a, b, c, search_alg = 487, 491, 22, breadth_first_d2
    #a, b, c, search_alg = 149, 572, 279, breadth_first_d2
    #a, b, c, search_alg = 835, 39, 126, breadth_first_d2
    #a, b, c, search_alg = 388, 252, 360, breadth_first_d2
    #a, b, c, search_alg = 178, 660, 162, breadth_first_d2
    #a, b, c, search_alg = 266, 317, 417, breadth_first_d2
    #a, b, c, search_alg = 940, 13, 47, breadth_first_d2
    #a, b, c, search_alg = 763, 122, 115, breadth_first_d2
    #a, b, c, search_alg = 491, 45, 464, breadth_first_d2
    #a, b, c, search_alg = 568, 327, 105, breadth_first_d2
    #a, b, c, search_alg = 713, 92, 195, breadth_first_d2
    #a, b, c, search_alg = 401, 98, 501, breadth_first_d2
    #a, b, c, search_alg = 308, 327, 365, breadth_first_d2
    #a, b, c, search_alg = 862, 48, 90, breadth_first_d2
    #a, b, c, search_alg = 133, 209, 658, breadth_first_d2
    #a, b, c, search_alg = 456, 421, 123, breadth_first_d2
    #a, b, c, search_alg = 44, 32, 924, breadth_first_d2

    #a, b, c, search_alg = 200, 152.0, 357.0, greedy_b8
    #a, b, c, search_alg = 891, 75, 34, greedy_b8
    #a, b, c, search_alg = 411, 539, 50, greedy_b8
    #a, b, c, search_alg = 487, 491, 22, greedy_b8
    #a, b, c, search_alg = 149, 572, 279, greedy_b8
    #a, b, c, search_alg = 835, 39, 126, greedy_b8
    #a, b, c, search_alg = 388, 252, 360, greedy_b8
    #a, b, c, search_alg = 178, 660, 162, greedy_b8
    #a, b, c, search_alg = 266, 317, 417, greedy_b8
    #a, b, c, search_alg = 940, 13, 47, greedy_b8
    #a, b, c, search_alg = 763, 122, 115, greedy_b8
    #a, b, c, search_alg = 491, 45, 464, greedy_b8
    #a, b, c, search_alg = 568, 327, 105, greedy_b8
    #a, b, c, search_alg = 713, 92, 195, greedy_b8
    #a, b, c, search_alg = 401, 98, 501, greedy_b8
    #a, b, c, search_alg = 308, 327, 365, greedy_b8
    #a, b, c, search_alg = 862, 48, 90, greedy_b8
    #a, b, c, search_alg = 133, 209, 658, greedy_b8
    #a, b, c, search_alg = 456, 421, 123, greedy_b8
    #a, b, c, search_alg = 44, 32, 924, greedy_b8


    #a, b, c, search_alg = 200, 152.0, 357.0, greedy_b8_learn
    #a, b, c, search_alg = 891, 75, 34, greedy_b8
    #a, b, c, search_alg = 411, 539, 50, greedy_b8
    #a, b, c, search_alg = 487, 491, 22, greedy_b8
    #a, b, c, search_alg = 149, 572, 279, greedy_b8
    #a, b, c, search_alg = 835, 39, 126, greedy_b8
    #a, b, c, search_alg = 388, 252, 360, greedy_b8
    #a, b, c, search_alg = 178, 660, 162, greedy_b8
    #a, b, c, search_alg = 266, 317, 417, greedy_b8
    #a, b, c, search_alg = 940, 13, 47, greedy_b8
    #a, b, c, search_alg = 763, 122, 115, greedy_b8
    #a, b, c, search_alg = 491, 45, 464, greedy_b8
    #a, b, c, search_alg = 568, 327, 105, greedy_b8
    #a, b, c, search_alg = 713, 92, 195, greedy_b8
    #a, b, c, search_alg = 401, 98, 501, greedy_b8
    #a, b, c, search_alg = 308, 327, 365, greedy_b8
    #a, b, c, search_alg = 862, 48, 90, greedy_b8
    #a, b, c, search_alg = 133, 209, 658, greedy_b8
    #a, b, c, search_alg = 456, 421, 123, greedy_b8
    #a, b, c, search_alg = 44, 32, 924, greedy_b8

    queues, intersections, goal = state.init_problem(a, b, c)
    visited = dict()
    execution_time = rta_star(queues, intersections, search_alg)
    print "{0}, {1}, {2}, {3}, {4}".format(a, b, c, search_alg.__name__, execution_time)


