import numpy
import itertools
import copy
import heapq
import logging
import time
import os
import state
import transition


def h(queues, intersections, goal):
    h = visited.get((tuple(queues.iteritems()), tuple(intersections.iteritems())))
    if not h:
        h = state.heuristic(queues, goal)
    return h


def local(current_queues, current_intersections, intersection, actions):
    interval = 100
    min_f = []
    for phase in actions:
        successor_intersections = copy.copy(current_intersections)
        successor_intersections[intersection] = (phase, current_intersections[intersection][1] + interval)
        active_flows = state.get_rates(current_intersections, interval)
        #print(active_flows)
        max_flows = transition.maximize_flows(active_flows, current_queues)
        successor_queues = state.simulate(current_queues, max_flows)
        improved_h = h(successor_queues, successor_intersections, goal)
        cost = 1
        f = cost + improved_h
        heapq.heappush(min_f, (f, (intersection, phase)))
    try:
        best_phase = heapq.heappop(min_f)
    except IndexError:
        best_phase = None
    try:
        next_best_phase = heapq.heappop(min_f)
    except IndexError:
        next_best_phase = None
    return best_phase, next_best_phase

def get_intersection(best):
    f = best[0]
    intersection, phase = best[1]
    return intersection

def get_phase(best):
    f = best[0]
    intersection, phase = best[1]
    return phase

def visited_h(alternatives, current_state, visited, max_interval, best):
    min_h = float("inf")
    i = 0
    for phase in alternatives:
        next_best = copy.copy(best)
        next_best[i] = phase
        if phase:
            interval = phase[1][3]
            alternative_state = state.simulate(current_state, next_best, max(max_interval, interval))
            visited_h = h(alternative_state, visited)
            if visited_h < min_h:
                min_h = visited_h
        i += 1
    return min_h


def search(current_queues, current_intersections):
    next_intersections = {}
    alternatives = []
    max_interval = 100
    for intersection, actions in state.applicable_actions(current_intersections).iteritems():
        best, next_best = local(current_queues, current_intersections, intersection, actions)
        current_phase = current_intersections[intersection][0]
        current_time = current_intersections[intersection][1]
        next_phase = get_phase(best)
        new_time = current_time + max_interval
        if next_phase != current_phase:
            new_time = max_interval
        next_intersections[intersection] = (next_phase, new_time)
        alternatives.append(next_best)
    cost = 1
    next_best_h = cost + 1 #visited_h(alternatives, current_state, visited, max_interval, assignment)
    return next_intersections, next_best_h



def rta_star(initial_queues, initial_intersections):
    current_queues = initial_queues
    current_intersections = initial_intersections
    #execution_time = 0
    #max_search_time = 0
    interval = 100
    #print(current_queues)
    #print(goal)
    while not state.is_goal(goal, current_queues):
        #start_time = time.clock()
        next_intersections, new_h = search(current_queues, current_intersections)
        #end_time = time.clock()-start_time
        #if end_time > max_search_time:
        #    max_search_time = end_time
        #print(next_intersections)
        rates = state.get_rates(next_intersections, interval)
        #print(current_queues)
        max_flows = transition.maximize_flows(rates, current_queues)
        #print(max_flows)
        visited[(tuple(current_queues), tuple(current_intersections))] = new_h
        next_queues = state.simulate(current_queues, max_flows)
        state.print_change(current_queues, next_queues)
        current_queues = next_queues
        current_intersections = next_intersections

        #print(h(successor_state, visited), new_h)
        #print(visited)
        #execution_time += interval
        #print(next_intersections)
        #print(current_queues)
        #print("max search time per iteration so far (seconds): {0}".format(max_search_time))
    #print(current_state)
    #print("execution time (seconds): {0}".format(execution_time))
    #print("max search time per iteration (seconds): {0}".format(max_search_time))


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
    queues, intersections, goal = state.init_problem()
    #print(current_state)
    #print(actions)
    #print(goal)
    visited = dict()
    rta_star(queues, intersections)

