from copy import copy
import numpy

queue_capacity = {}
queue_capacity["L1202_1349"] = 88
queue_capacity["L1202_3967"] = 138
queue_capacity["L1202_6013"] = 61
queue_capacity["L1216_1352"] = 13
queue_capacity["L1233_1352"] = 30
queue_capacity["L1349_1202"] = 89
queue_capacity["L1349_1353"] = 78
queue_capacity["L1349_1867"] = 63
queue_capacity["L1349_3621"] = 181
queue_capacity["L1352_1353"] = 60
queue_capacity["L1352_1867"] = 73
queue_capacity["L1353_1349"] = 88
queue_capacity["L1353_1352"] = 119
queue_capacity["L1353_6014"] = 24
queue_capacity["L1867_1349"] = 104
queue_capacity["L1867_1352"] = 128
queue_capacity["L1867_3621"] = 19
queue_capacity["L1867_3621"] = 62
queue_capacity["L1867_4574"] = 82
queue_capacity["L3621_1349"] = 75
queue_capacity["L3621_1867"] = 60
queue_capacity["L3966_1202"] = 101
queue_capacity["L4574_1867"] = 179
queue_capacity["L5840_6013"] = 40
queue_capacity["L6013_1202"] = 35
queue_capacity["L6013_5840"] = 24
queue_capacity["L6013_6014"] = 94
queue_capacity["L6014_1353"] = 23
queue_capacity["L6014_6013"] = 94
queue_capacity["L6159_1353"] = 24
queue_capacity["L6159_6014"] = 218


# Network B
queue_capacity["L1202b_1349b"] = 88
queue_capacity["L1202b_3967b"] = 138
queue_capacity["L1202b_6013b"] = 61
queue_capacity["L1216b_1352b"] = 13
queue_capacity["L1233b_1352b"] = 30
queue_capacity["L1349b_1202b"] = 89
queue_capacity["L1349b_1353b"] = 78
queue_capacity["L1349b_1867b"] = 63
queue_capacity["L1349b_3621b"] = 181
queue_capacity["L1352b_1353b"] = 60
queue_capacity["L1352b_1867b"] = 73
queue_capacity["L1353b_1349b"] = 88
queue_capacity["L1353b_1352b"] = 119
queue_capacity["L1353b_6014b"] = 24
queue_capacity["L1867b_1349b"] = 104
queue_capacity["L1867b_1352b"] = 128
queue_capacity["L1867b_3621b"] = 19
queue_capacity["L1867b_3621b"] = 62
queue_capacity["L1867b_4574b"] = 82
queue_capacity["L3621b_1349b"] = 75
queue_capacity["L3621b_1867b"] = 60
queue_capacity["L3966b_1202b"] = 101
queue_capacity["L4574b_1867b"] = 179
queue_capacity["L5840b_6013b"] = 40
queue_capacity["L6013b_1202b"] = 35
queue_capacity["L6013b_5840b"] = 24
queue_capacity["L6013b_6014b"] = 94
queue_capacity["L6014b_1353b"] = 23
queue_capacity["L6014b_6013b"] = 94
queue_capacity["L6159b_1353b"] = 24
queue_capacity["L6159b_6014b"] = 218

# Connects networks A and B
queue_capacity["L1352b_1233b"] = 80 # In Figure 3 (Mccluskey) but not PDDL
queue_capacity["L5840_1233b"] = 80  # Average capacity
queue_capacity["L1233b_5840"] = 80  # Average capacity

def print_change(from_queues, to_queues):
    print("change...")
    for q, load in from_queues.iteritems():
        if load != to_queues[q]:
            print(q, from_queues[q], to_queues[q])


def sum_load(queues):
    s = 0
    for load in queues.itervalues():
        s += load
    return s


def simulate(queues, max_flows):
    new_queues = copy(queues)
    for flow, rate in max_flows.iteritems():
        in_queue, out_queue = edges[flow]
        change = rate
        new_queues[in_queue] = new_queues[in_queue] - change
        new_queues[out_queue] = new_queues[out_queue] + change
    return new_queues


phase_max = {}
phase_min = {}
phase_intergreen = {}

phase_intergreen["S1202_s0"] = 0
phase_intergreen["S1202_s1"] = 0
phase_intergreen["S1202_s2"] = 0
phase_intergreen["S1202_s3"] = 0
phase_intergreen["S1202_s4"] = 5
phase_intergreen["S1202_s5"] = 0
phase_intergreen["S1202_s6"] = 5
phase_min["S1202_s0"] = 5
phase_min["S1202_s1"] = 5
phase_min["S1202_s2"] = 0
phase_min["S1202_s3"] = 5
phase_min["S1202_s4"] = 5
phase_min["S1202_s5"] = 0
phase_min["S1202_s6"] = 5
phase_max["S1202_s0"] = 40
phase_max["S1202_s1"] = 20
phase_max["S1202_s2"] = 10
phase_max["S1202_s3"] = 60
phase_max["S1202_s4"] = 70
phase_max["S1202_s5"] = 15
phase_max["S1202_s6"] = 50
phase_intergreen["S1349_s0"] = 5
phase_intergreen["S1349_s1"] = 5
phase_intergreen["S1349_s2"] = 10
phase_intergreen["S1349_s3"] = 10
phase_min["S1349_s0"] = 5
phase_min["S1349_s1"] = 5
phase_min["S1349_s2"] = 5
phase_min["S1349_s3"] = 10
phase_max["S1349_s0"] = 70
phase_max["S1349_s1"] = 70
phase_max["S1349_s2"] = 70
phase_max["S1349_s3"] = 75
phase_intergreen["S6014_s0"] = 5
phase_intergreen["S6014_s1"] = 10
phase_intergreen["S6014_s2"] = 0
phase_intergreen["S6014_s3"] = 5
phase_min["S6014_s0"] = 5
phase_min["S6014_s1"] = 5
phase_min["S6014_s2"] = 10
phase_min["S6014_s3"] = 5
phase_max["S6014_s0"] = 50
phase_max["S6014_s1"] = 40
phase_max["S6014_s2"] = 50
phase_max["S6014_s3"] = 45
phase_intergreen["S6013_s0"] = 5
phase_intergreen["S6013_s1"] = 10
phase_intergreen["S6013_s2"] = 5
phase_min["S6013_s0"] = 5
phase_min["S6013_s1"] = 5
phase_min["S6013_s2"] = 5
phase_max["S6013_s0"] = 90
phase_max["S6013_s1"] = 95
phase_max["S6013_s2"] = 95
phase_intergreen["S1353_s0"] = 10
phase_intergreen["S1353_s1"] = 10
phase_intergreen["S1353_s2"] = 5
phase_min["S1353_s0"] = 5
phase_min["S1353_s1"] = 5
phase_min["S1353_s2"] = 5
phase_max["S1353_s0"] = 55
phase_max["S1353_s1"] = 50
phase_max["S1353_s2"] = 50
phase_intergreen["S1352_s0"] = 5
phase_intergreen["S1352_s1"] = 25
phase_min["S1352_s0"] = 5
phase_min["S1352_s1"] = 5
phase_max["S1352_s0"] = 55
phase_max["S1352_s1"] = 40
phase_intergreen["S1867_s0"] = 0
phase_intergreen["S1867_s1"] = 20
phase_intergreen["S1867_s2"] = 10
phase_min["S1867_s0"] = 5
phase_min["S1867_s1"] = 5
phase_min["S1867_s2"] = 5
phase_max["S1867_s0"] = 65
phase_max["S1867_s1"] = 60
phase_max["S1867_s2"] = 60

# Network B
phase_intergreen["S1202b_s0"] = 0
phase_intergreen["S1202b_s1"] = 0
phase_intergreen["S1202b_s2"] = 0
phase_intergreen["S1202b_s3"] = 0
phase_intergreen["S1202b_s4"] = 5
phase_intergreen["S1202b_s5"] = 0
phase_intergreen["S1202b_s6"] = 5
phase_min["S1202b_s0"] = 5
phase_min["S1202b_s1"] = 5
phase_min["S1202b_s2"] = 0
phase_min["S1202b_s3"] = 5
phase_min["S1202b_s4"] = 5
phase_min["S1202b_s5"] = 0
phase_min["S1202b_s6"] = 5
phase_max["S1202b_s0"] = 40
phase_max["S1202b_s1"] = 20
phase_max["S1202b_s2"] = 10
phase_max["S1202b_s3"] = 60
phase_max["S1202b_s4"] = 70
phase_max["S1202b_s5"] = 15
phase_max["S1202b_s6"] = 50
phase_intergreen["S1349b_s0"] = 5
phase_intergreen["S1349b_s1"] = 5
phase_intergreen["S1349b_s2"] = 10
phase_intergreen["S1349b_s3"] = 10
phase_min["S1349b_s0"] = 5
phase_min["S1349b_s1"] = 5
phase_min["S1349b_s2"] = 5
phase_min["S1349b_s3"] = 10
phase_max["S1349b_s0"] = 70
phase_max["S1349b_s1"] = 70
phase_max["S1349b_s2"] = 70
phase_max["S1349b_s3"] = 75
phase_intergreen["S6014b_s0"] = 5
phase_intergreen["S6014b_s1"] = 10
phase_intergreen["S6014b_s2"] = 0
phase_intergreen["S6014b_s3"] = 5
phase_min["S6014b_s0"] = 5
phase_min["S6014b_s1"] = 5
phase_min["S6014b_s2"] = 10
phase_min["S6014b_s3"] = 5
phase_max["S6014b_s0"] = 50
phase_max["S6014b_s1"] = 40
phase_max["S6014b_s2"] = 50
phase_max["S6014b_s3"] = 45
phase_intergreen["S6013b_s0"] = 5
phase_intergreen["S6013b_s1"] = 10
phase_intergreen["S6013b_s2"] = 5
phase_min["S6013b_s0"] = 5
phase_min["S6013b_s1"] = 5
phase_min["S6013b_s2"] = 5
phase_max["S6013b_s0"] = 90
phase_max["S6013b_s1"] = 95
phase_max["S6013b_s2"] = 95
phase_intergreen["S1353b_s0"] = 10
phase_intergreen["S1353b_s1"] = 10
phase_intergreen["S1353b_s2"] = 5
phase_min["S1353b_s0"] = 5
phase_min["S1353b_s1"] = 5
phase_min["S1353b_s2"] = 5
phase_max["S1353b_s0"] = 55
phase_max["S1353b_s1"] = 50
phase_max["S1353b_s2"] = 50
phase_intergreen["S1352b_s0"] = 5
phase_intergreen["S1352b_s1"] = 25
phase_min["S1352b_s0"] = 5
phase_min["S1352b_s1"] = 5
phase_max["S1352b_s0"] = 55
phase_max["S1352b_s1"] = 40
phase_intergreen["S1867b_s0"] = 0
phase_intergreen["S1867b_s1"] = 20
phase_intergreen["S1867b_s2"] = 10
phase_min["S1867b_s0"] = 5
phase_min["S1867b_s1"] = 5
phase_min["S1867b_s2"] = 5
phase_max["S1867b_s0"] = 65
phase_max["S1867b_s1"] = 60
phase_max["S1867b_s2"] = 60

phase_cycles = {}
phase_cycles["S1202_s0"] = "S1202_s1"
phase_cycles["S1202_s1"] = "S1202_s2"
phase_cycles["S1202_s2"] = "S1202_s3"
phase_cycles["S1202_s3"] = "S1202_s4"
phase_cycles["S1202_s4"] = "S1202_s5"
phase_cycles["S1202_s5"] = "S1202_s6"
phase_cycles["S1202_s6"] = "S1202_s0"
phase_cycles["S1349_s0"] = "S1349_s1"
phase_cycles["S1349_s1"] = "S1349_s2"
phase_cycles["S1349_s2"] = "S1349_s3"
phase_cycles["S1349_s3"] = "S1349_s0"
phase_cycles["S6014_s0"] = "S6014_s1"
phase_cycles["S6014_s1"] = "S6014_s2"
phase_cycles["S6014_s2"] = "S6014_s3"
phase_cycles["S6014_s3"] = "S6014_s0"
phase_cycles["S6013_s0"] = "S6013_s1"
phase_cycles["S6013_s1"] = "S6013_s2"
phase_cycles["S6013_s2"] = "S6013_s0"
phase_cycles["S1353_s0"] = "S1353_s1"
phase_cycles["S1353_s1"] = "S1353_s2"
phase_cycles["S1353_s2"] = "S1353_s0"
phase_cycles["S1352_s0"] = "S1352_s1"
phase_cycles["S1352_s1"] = "S1352_s0"
phase_cycles["S1867_s0"] = "S1867_s1"
phase_cycles["S1867_s1"] = "S1867_s2"
phase_cycles["S1867_s2"] = "S1867_s0"

# Network B

phase_cycles["S1202b_s0"] = "S1202b_s1"
phase_cycles["S1202b_s1"] = "S1202b_s2"
phase_cycles["S1202b_s2"] = "S1202b_s3"
phase_cycles["S1202b_s3"] = "S1202b_s4"
phase_cycles["S1202b_s4"] = "S1202b_s5"
phase_cycles["S1202b_s5"] = "S1202b_s6"
phase_cycles["S1202b_s6"] = "S1202b_s0"
phase_cycles["S1349b_s0"] = "S1349b_s1"
phase_cycles["S1349b_s1"] = "S1349b_s2"
phase_cycles["S1349b_s2"] = "S1349b_s3"
phase_cycles["S1349b_s3"] = "S1349b_s0"
phase_cycles["S6014b_s0"] = "S6014b_s1"
phase_cycles["S6014b_s1"] = "S6014b_s2"
phase_cycles["S6014b_s2"] = "S6014b_s3"
phase_cycles["S6014b_s3"] = "S6014b_s0"
phase_cycles["S6013b_s0"] = "S6013b_s1"
phase_cycles["S6013b_s1"] = "S6013b_s2"
phase_cycles["S6013b_s2"] = "S6013b_s0"
phase_cycles["S1353b_s0"] = "S1353b_s1"
phase_cycles["S1353b_s1"] = "S1353b_s2"
phase_cycles["S1353b_s2"] = "S1353b_s0"
phase_cycles["S1352b_s0"] = "S1352b_s1"
phase_cycles["S1352b_s1"] = "S1352b_s0"
phase_cycles["S1867b_s0"] = "S1867b_s1"
phase_cycles["S1867b_s1"] = "S1867b_s2"
phase_cycles["S1867b_s2"] = "S1867b_s0"

def applicable_actions(intersections, cycles=False):
    applicable = {}

    if cycles:
        for intersection, state in intersections.iteritems():
            phase = state[0]
            phase_time = state[1]
            #intergreen_ind = state[2]
            #int_time = state[3]
            if not applicable.get(intersection):
                applicable[intersection] = []
            if phase_time > phase_min[phase]:
                applicable[intersection].append(phase_cycles[phase])
            if phase_time < phase_max[phase]:
                applicable[intersection].append(phase)
    else:
        for intersection in intersections.iterkeys():
            applicable[intersection] = []
            for i in range(0, 6):
                phase = "{0}_s{1}".format(intersection, i)
                if phases.get(phase):
                    applicable[intersection].append(phase)

    return applicable




def get_intergreen(phase):
    return phase_intergreen.get(phase, 0)


def heuristic(queues, goal):
    current_state = []
    goal_state = []
    for queue, capacity in goal.iteritems():
        load = queues[queue]
        if load < capacity:
            load = capacity
        current_state.append(load)
        goal_state.append(capacity)
    h = numpy.linalg.norm(numpy.asarray(current_state) - numpy.asarray(goal_state))
    return h


def is_goal(goal, queues):
    for queue, capacity in goal.iteritems():
        load = queues[queue]
        if load > capacity:
            return False
    return True


def get_rates(current_intersections, previous_intersections={}, interval=10):
    rates = {}
    for flow in edges.iterkeys():
        rates[flow] = 0.0
    for intersection, phase in current_intersections.iteritems():
        phase_name = phase[0]
        previous_phase = previous_intersections[intersection][0]
        intergreen = 0
        if phase_name != previous_phase:
            intergreen = get_intergreen(previous_phase)
        for flow, rate in phases[phase_name]:
            rates[flow] = rate * (interval - min(intergreen, interval))
    for flow, rate in phases["fake"]:  # Because some flows are always on
        rates[flow] = rate * interval
    return rates


def init_problem(a, b, c):
    queues = init_queues(a, b, c)
    intersections = init_intersections()
    goal = init_goal()
    return queues, intersections, goal


def init_queues(a=300.0, b=152.0, c=357.0):
    queues = {}
    queues["L6013_1202"] = 0.0
    queues["L3966_1202"] = a #300.0  # Initially 300.0 per PDDL, capacity is 101
    queues["L1202_3967"] = 11.0
    queues["L1202_6013"] = 8.0
    queues["L1349_3621"] = 0.0
    queues["L1867_1349"] = 59.0
    queues["L1353_1349"] = 0.0
    queues["L1349_1353"] = 0.0
    queues["L3621_1349"] = b #152.0  # Initially 152.0 per PDDL, capacity is 75
    queues["L1349_1867"] = 3.0
    queues["L6159_6014"] = 15.0
    queues["L6013_6014"] = 14.0
    queues["L6014_6013"] = 2.0
    queues["L1353_6014"] = 1.0
    queues["L6014_1353"] = 5.0
    queues["L5840_6013"] = 2.0
    queues["L6013_5840"] = 0.0
    queues["L1352_1353"] = 1.0
    queues["L1353_1352"] = 0.0
    queues["L1352_1867"] = 65.0
    queues["L1867_1352"] = 4.0
    queues["L1867_3621"] = 0.0
    queues["L3621_1867"] = 29.0
    queues["L4574_1867"] = c #357.0  # Initially 357.0 per PDDL, capacity is 179
    queues["L1867_4574"] = 5.0
    queues["L1233_1352"] = 16.0
    queues["L1216_1352"] = 10.0
    queues["L6159_1353"] = 0.0
    queues["L1349_1202"] = 10.0
    queues["L1202_1349"] = 10.0
    queues["outside"] = 0

    # Network B
    queues["L6013b_1202b"] = 0.0
    queues["L3966b_1202b"] = 15.0 #15% of capacity
    queues["L1202b_3967b"] = 11.0
    queues["L1202b_6013b"] = 8.0
    queues["L1349b_3621b"] = 0.0
    queues["L1867b_1349b"] = 59.0
    queues["L1353b_1349b"] = 0.0
    queues["L1349b_1353b"] = 0.0
    queues["L3621b_1349b"] = 11.25 #15% of capacity
    queues["L1349b_1867b"] = 3.0
    queues["L6159b_6014b"] = 15.0
    queues["L6013b_6014b"] = 14.0
    queues["L6014b_6013b"] = 2.0
    queues["L1353b_6014b"] = 1.0
    queues["L6014b_1353b"] = 5.0
    queues["L5840b_6013b"] = 2.0
    queues["L6013b_5840b"] = 0.0
    queues["L1352b_1353b"] = 1.0
    queues["L1353b_1352b"] = 0.0
    queues["L1352b_1867b"] = 65.0
    queues["L1867b_1352b"] = 4.0
    queues["L1867b_3621b"] = 0.0
    queues["L3621b_1867b"] = 29.0
    queues["L4574b_1867b"] = 27.0 #15% of capacity
    queues["L1867b_4574b"] = 5.0
    queues["L1233b_1352b"] = 16.0
    queues["L1216b_1352b"] = 10.0
    queues["L6159b_1353b"] = 0.0
    queues["L1349b_1202b"] = 10.0
    queues["L1202b_1349b"] = 10.0

    # Connecting queues
    queues["L1352b_1233b"] = 12.0
    queues["L5840_1233b"] = 12.0
    queues["L1233b_5840"] = 12.0

    return queues

edges = {}
edges["L1202_1349__L1349_1867"] = ("L1202_1349", "L1349_1867")
edges["L1202_1349__L1349_3621"] = ("L1202_1349", "L1349_3621")
edges["L1202_3967__outside"] = ("L1202_3967", "outside")
edges["L1202_6013__L6013_5840"] = ("L1202_6013", "L6013_5840")
edges["L1202_6013__L6013_6014"] = ("L1202_6013", "L6013_6014")
edges["L1216_1352__L1352_1867"] = ("L1216_1352", "L1352_1867")
edges["L1216_1352__outside"] = ("L1216_1352", "outside")
edges["L1233_1352__L1352_1353"] = ("L1233_1352", "L1352_1353")
edges["L1233_1352__L1352_1867"] = ("L1233_1352", "L1352_1867")
edges["L1233_1352__outside"] = ("L1233_1352", "outside")
edges["L1349_1202__L1202_3967"] = ("L1349_1202", "L1202_3967")
edges["L1349_1202__L1202_6013"] = ("L1349_1202", "L1202_6013")
edges["L1349_1353__L1353_1352"] = ("L1349_1353", "L1353_1352")
edges["L1349_1353__outside"] = ("L1349_1353", "outside")
edges["L1349_1867__L1867_1352"] = ("L1349_1867", "L1867_1352")
edges["L1349_1867__L1867_4574"] = ("L1349_1867", "L1867_4574")
edges["L1349_3621__outside"] = ("L1349_3621", "outside")
edges["L1352_1353__L1353_6014"] = ("L1352_1353", "L1353_6014")
edges["L1352_1353__L1353_6014"] = ("L1352_1353", "L1353_6014")
edges["L1352_1353__outside"] = ("L1352_1353", "outside")
edges["L1352_1353__outside"] = ("L1352_1353", "outside")
edges["L1352_1867__L1867_1349"] = ("L1352_1867", "L1867_1349")
edges["L1352_1867__L1867_3621"] = ("L1352_1867", "L1867_3621")
edges["L1352_1867__L1867_4574"] = ("L1352_1867", "L1867_4574")
edges["L1353_1349__L1349_1202"] = ("L1353_1349", "L1349_1202")
edges["L1353_1349__L1349_1867"] = ("L1353_1349", "L1349_1867")
edges["L1353_1349__L1349_3621"] = ("L1353_1349", "L1349_3621")
edges["L1353_1352__outside"] = ("L1353_1352", "outside")
edges["L1353_1352__outside"] = ("L1353_1352", "outside")
edges["L1353_6014__L6014_6013"] = ("L1353_6014", "L6014_6013")
edges["L1353_6014__outside"] = ("L1353_6014", "outside")
edges["L1867_1349__L1349_1202"] = ("L1867_1349", "L1349_1202")
edges["L1867_1349__L1349_1353"] = ("L1867_1349", "L1349_1353")
edges["L1867_1349__L1349_3621"] = ("L1867_1349", "L1349_3621")
edges["L1867_1352__L1352_1353"] = ("L1867_1352", "L1352_1353")
edges["L1867_1352__outside"] = ("L1867_1352", "outside")
edges["L1867_1352__outside"] = ("L1867_1352", "outside")
edges["L1867_3621__outside"] = ("L1867_3621", "outside")
edges["L1867_4574__outside"] = ("L1867_4574", "outside")
edges["L3621_1349__L1349_1202"] = ("L3621_1349", "L1349_1202")
edges["L3621_1349__L1349_1353"] = ("L3621_1349", "L1349_1353")
edges["L3621_1867__L1867_1349"] = ("L3621_1867", "L1867_1349")
edges["L3621_1867__L1867_1352"] = ("L3621_1867", "L1867_1352")
edges["L3621_1867__L1867_4574"] = ("L3621_1867", "L1867_4574")
edges["L3966_1202__L1202_1349"] = ("L3966_1202", "L1202_1349")
edges["L3966_1202__L1202_6013"] = ("L3966_1202", "L1202_6013")
edges["L4574_1867__L1867_1349"] = ("L4574_1867", "L1867_1349")
edges["L4574_1867__L1867_1352"] = ("L4574_1867", "L1867_1352")
edges["L4574_1867__L1867_3621"] = ("L4574_1867", "L1867_3621")
edges["L5840_6013__L6013_1202"] = ("L5840_6013", "L6013_1202")
edges["L5840_6013__L6013_6014"] = ("L5840_6013", "L6013_6014")
edges["L6013_1202__L1202_1349"] = ("L6013_1202", "L1202_1349")
edges["L6013_1202__L1202_3967"] = ("L6013_1202", "L1202_3967")
#edges["L6013_5840__outside"] = ("L6013_5840", "outside")
edges["L6013_5840__L5840_1233b"] = ("L6013_5840", "L5840_1233b")  # Connects to network B
edges["L6013_6014__L6014_1353"] = ("L6013_6014", "L6014_1353")
edges["L6013_6014__outside"] = ("L6013_6014", "outside")
edges["L6014_1353__L1353_1349"] = ("L6014_1353", "L1353_1349")
edges["L6014_1353__L1353_1352"] = ("L6014_1353", "L1353_1352")
edges["L6014_6013__L6013_1202"] = ("L6014_6013", "L6013_1202")
edges["L6014_6013__L6013_5840"] = ("L6014_6013", "L6013_5840")
edges["L6159_1353__L1353_1349"] = ("L6159_1353", "L1353_1349")
edges["L6159_1353__L1353_1352"] = ("L6159_1353", "L1353_1352")
edges["L6159_6014__L6014_1353"] = ("L6159_6014", "L6014_1353")
edges["L6159_6014__L6014_6013"] = ("L6159_6014", "L6014_6013")
edges["outside__L1216_1352"] = ("outside", "L1216_1352")
edges["outside__L1233_1352"] = ("outside", "L1233_1352")
edges["outside__L3621_1867"] = ("outside", "L3621_1867")
edges["outside__L5840_6013"] = ("outside", "L5840_6013")
edges["outside__L6159_1353"] = ("outside", "L6159_1353")
edges["outside__L6159_6014"] = ("outside", "L6159_6014")

# Network B
edges["L1202b_1349b__L1349b_1867b"] = ("L1202b_1349b", "L1349b_1867b")
edges["L1202b_1349b__L1349b_3621b"] = ("L1202b_1349b", "L1349b_3621b")
edges["L1202b_3967b__outside"] = ("L1202b_3967b", "outside")
edges["L1202b_6013b__L6013b_5840b"] = ("L1202b_6013b", "L6013b_5840b")
edges["L1202b_6013b__L6013b_6014b"] = ("L1202b_6013b", "L6013b_6014b")
edges["L1216b_1352b__L1352b_1867b"] = ("L1216b_1352b", "L1352b_1867b")
edges["L1216b_1352b__outside"] = ("L1216b_1352b", "outside")
edges["L1233b_1352b__L1352b_1353b"] = ("L1233b_1352b", "L1352b_1353b")
edges["L1233b_1352b__L1352b_1867b"] = ("L1233b_1352b", "L1352b_1867b")
edges["L1233b_1352b__outside"] = ("L1233b_1352b", "outside")
edges["L1349b_1202b__L1202b_3967b"] = ("L1349b_1202b", "L1202b_3967b")
edges["L1349b_1202b__L1202b_6013b"] = ("L1349b_1202b", "L1202b_6013b")
edges["L1349b_1353b__L1353b_1352b"] = ("L1349b_1353b", "L1353b_1352b")
edges["L1349b_1353b__outside"] = ("L1349b_1353b", "outside")
edges["L1349b_1867b__L1867b_1352b"] = ("L1349b_1867b", "L1867b_1352b")
edges["L1349b_1867b__L1867b_4574b"] = ("L1349b_1867b", "L1867b_4574b")
edges["L1349b_3621b__outside"] = ("L1349b_3621b", "outside")
edges["L1352b_1353b__L1353b_6014b"] = ("L1352b_1353b", "L1353b_6014b")
edges["L1352b_1353b__L1353b_6014b"] = ("L1352b_1353b", "L1353b_6014b")
edges["L1352b_1353b__outside"] = ("L1352b_1353b", "outside")
edges["L1352b_1353b__outside"] = ("L1352b_1353b", "outside")
edges["L1352b_1867b__L1867b_1349b"] = ("L1352b_1867b", "L1867b_1349b")
edges["L1352b_1867b__L1867b_3621b"] = ("L1352b_1867b", "L1867b_3621b")
edges["L1352b_1867b__L1867b_4574b"] = ("L1352b_1867b", "L1867b_4574b")
edges["L1353b_1349b__L1349b_1202b"] = ("L1353b_1349b", "L1349b_1202b")
edges["L1353b_1349b__L1349b_1867b"] = ("L1353b_1349b", "L1349b_1867b")
edges["L1353b_1349b__L1349b_3621b"] = ("L1353b_1349b", "L1349b_3621b")
edges["L1353b_1352b__outside"] = ("L1353b_1352b", "outside")
edges["L1353b_1352b__outside"] = ("L1353b_1352b", "outside")
edges["L1353b_6014b__L6014b_6013b"] = ("L1353b_6014b", "L6014b_6013b")
edges["L1353b_6014b__outside"] = ("L1353b_6014b", "outside")
edges["L1867b_1349b__L1349b_1202b"] = ("L1867b_1349b", "L1349b_1202b")
edges["L1867b_1349b__L1349b_1353b"] = ("L1867b_1349b", "L1349b_1353b")
edges["L1867b_1349b__L1349b_3621b"] = ("L1867b_1349b", "L1349b_3621b")
edges["L1867b_1352b__L1352b_1353b"] = ("L1867b_1352b", "L1352b_1353b")
edges["L1867b_1352b__outside"] = ("L1867b_1352b", "outside")
edges["L1867b_1352b__outside"] = ("L1867b_1352b", "outside")
edges["L1867b_3621b__outside"] = ("L1867b_3621b", "outside")
edges["L1867b_4574b__outside"] = ("L1867b_4574b", "outside")
edges["L3621b_1349b__L1349b_1202b"] = ("L3621b_1349b", "L1349b_1202b")
edges["L3621b_1349b__L1349b_1353b"] = ("L3621b_1349b", "L1349b_1353b")
edges["L3621b_1867b__L1867b_1349b"] = ("L3621b_1867b", "L1867b_1349b")
edges["L3621b_1867b__L1867b_1352b"] = ("L3621b_1867b", "L1867b_1352b")
edges["L3621b_1867b__L1867b_4574b"] = ("L3621b_1867b", "L1867b_4574b")
edges["L3966b_1202b__L1202b_1349b"] = ("L3966b_1202b", "L1202b_1349b")
edges["L3966b_1202b__L1202b_6013b"] = ("L3966b_1202b", "L1202b_6013b")
edges["L4574b_1867b__L1867b_1349b"] = ("L4574b_1867b", "L1867b_1349b")
edges["L4574b_1867b__L1867b_1352b"] = ("L4574b_1867b", "L1867b_1352b")
edges["L4574b_1867b__L1867b_3621b"] = ("L4574b_1867b", "L1867b_3621b")
edges["L5840b_6013b__L6013b_1202b"] = ("L5840b_6013b", "L6013b_1202b")
edges["L5840b_6013b__L6013b_6014b"] = ("L5840b_6013b", "L6013b_6014b")
edges["L6013b_1202b__L1202b_1349b"] = ("L6013b_1202b", "L1202b_1349b")
edges["L6013b_1202b__L1202b_3967b"] = ("L6013b_1202b", "L1202b_3967b")
edges["L6013b_5840b__outside"] = ("L6013b_5840b", "outside")
edges["L6013b_6014b__L6014b_1353b"] = ("L6013b_6014b", "L6014b_1353b")
edges["L6013b_6014b__outside"] = ("L6013b_6014b", "outside")
edges["L6014b_1353b__L1353b_1349b"] = ("L6014b_1353b", "L1353b_1349b")
edges["L6014b_1353b__L1353b_1352b"] = ("L6014b_1353b", "L1353b_1352b")
edges["L6014b_6013b__L6013b_1202b"] = ("L6014b_6013b", "L6013b_1202b")
edges["L6014b_6013b__L6013b_5840b"] = ("L6014b_6013b", "L6013b_5840b")
edges["L6159b_1353b__L1353b_1349b"] = ("L6159b_1353b", "L1353b_1349b")
edges["L6159b_1353b__L1353b_1352b"] = ("L6159b_1353b", "L1353b_1352b")
edges["L6159b_6014b__L6014b_1353b"] = ("L6159b_6014b", "L6014b_1353b")
edges["L6159b_6014b__L6014b_6013b"] = ("L6159b_6014b", "L6014b_6013b")
edges["outside__L1216b_1352b"] = ("outside", "L1216b_1352b")
edges["L5840_1233b__L1233b_1352b"] = ("L5840_1233b", "L1233b_1352b")  # Connects to network B
edges["outside__L3621b_1867b"] = ("outside", "L3621b_1867b")
edges["outside__L5840b_6013b"] = ("outside", "L5840b_6013b")
edges["outside__L6159b_1353b"] = ("outside", "L6159b_1353b")
edges["outside__L6159b_6014b"] = ("outside", "L6159b_6014b")

# Connecting edges

edges["L1233b_5840__L5840_6013"] = ("L1233b_5840", "L5840_6013")
edges["L1352b_1233b__L1233b_5840"] = ("L1352b_1233b", "L1233b_5840")


phases = {}
if phases.get("S1202_s0"):
    phases["S1202_s0"].append(("L3966_1202__L1202_1349", 0.64522))
else:
    phases["S1202_s0"] = [("L3966_1202__L1202_1349", 0.64522)]
if phases.get("S1202_s1"):
    phases["S1202_s1"].append(("L3966_1202__L1202_1349", 0.64522))
else:
    phases["S1202_s1"] = [("L3966_1202__L1202_1349", 0.64522)]
if phases.get("S1202_s2"):
    phases["S1202_s2"].append(("L3966_1202__L1202_1349", 0.64522))
else:
    phases["S1202_s2"] = [("L3966_1202__L1202_1349", 0.64522)]
if phases.get("S1202_s3"):
    phases["S1202_s3"].append(("L3966_1202__L1202_1349", 0.64522))
else:
    phases["S1202_s3"] = [("L3966_1202__L1202_1349", 0.64522)]
if phases.get("S1202_s6"):
    phases["S1202_s6"].append(("L6013_1202__L1202_1349", 0.165))
else:
    phases["S1202_s6"] = [("L6013_1202__L1202_1349", 0.165)]
if phases.get("S1202_s3"):
    phases["S1202_s3"].append(("L1349_1202__L1202_3967", 0.825))
else:
    phases["S1202_s3"] = [("L1349_1202__L1202_3967", 0.825)]
if phases.get("S1202_s4"):
    phases["S1202_s4"].append(("L1349_1202__L1202_3967", 0.825))
else:
    phases["S1202_s4"] = [("L1349_1202__L1202_3967", 0.825)]
if phases.get("S1202_s0"):
    phases["S1202_s0"].append(("L6013_1202__L1202_3967", 0.41067))
else:
    phases["S1202_s0"] = [("L6013_1202__L1202_3967", 0.41067)]
if phases.get("S1202_s1"):
    phases["S1202_s1"].append(("L6013_1202__L1202_3967", 0.41067))
else:
    phases["S1202_s1"] = [("L6013_1202__L1202_3967", 0.41067)]
if phases.get("S1202_s5"):
    phases["S1202_s5"].append(("L6013_1202__L1202_3967", 0.41067))
else:
    phases["S1202_s5"] = [("L6013_1202__L1202_3967", 0.41067)]
if phases.get("S1202_s6"):
    phases["S1202_s6"].append(("L6013_1202__L1202_3967", 0.41067))
else:
    phases["S1202_s6"] = [("L6013_1202__L1202_3967", 0.41067)]
if phases.get("S1202_s2"):
    phases["S1202_s2"].append(("L1349_1202__L1202_6013", 0.11138))
else:
    phases["S1202_s2"] = [("L1349_1202__L1202_6013", 0.11138)]
if phases.get("S1202_s3"):
    phases["S1202_s3"].append(("L1349_1202__L1202_6013", 0.11138))
else:
    phases["S1202_s3"] = [("L1349_1202__L1202_6013", 0.11138)]
if phases.get("S1202_s4"):
    phases["S1202_s4"].append(("L1349_1202__L1202_6013", 0.11138))
else:
    phases["S1202_s4"] = [("L1349_1202__L1202_6013", 0.11138)]
if phases.get("S1202_s0"):
    phases["S1202_s0"].append(("L3966_1202__L1202_6013", 0.71739))
else:
    phases["S1202_s0"] = [("L3966_1202__L1202_6013", 0.71739)]
if phases.get("fake"):
    phases["fake"].append(("outside__L1216_1352", 0.075))
else:
    phases["fake"] = [("outside__L1216_1352", 0.075)]
if phases.get("fake"):
    phases["fake"].append(("outside__L1233_1352", 0.17667))
else:
    phases["fake"] = [("outside__L1233_1352", 0.17667)]
if phases.get("S1349_s0"):
    phases["S1349_s0"].append(("L1353_1349__L1349_1202", 0.01961))
else:
    phases["S1349_s0"] = [("L1353_1349__L1349_1202", 0.01961)]
if phases.get("S1349_s3"):
    phases["S1349_s3"].append(("L1353_1349__L1349_1202", 0.01961))
else:
    phases["S1349_s3"] = [("L1353_1349__L1349_1202", 0.01961)]
if phases.get("S1349_s1"):
    phases["S1349_s1"].append(("L1867_1349__L1349_1202", 0.79845))
else:
    phases["S1349_s1"] = [("L1867_1349__L1349_1202", 0.79845)]
if phases.get("S1349_s2"):
    phases["S1349_s2"].append(("L3621_1349__L1349_1202", 0.33333))
else:
    phases["S1349_s2"] = [("L3621_1349__L1349_1202", 0.33333)]
if phases.get("S1349_s1"):
    phases["S1349_s1"].append(("L1867_1349__L1349_1353", 0.03876))
else:
    phases["S1349_s1"] = [("L1867_1349__L1349_1353", 0.03876)]
if phases.get("S1349_s3"):
    phases["S1349_s3"].append(("L3621_1349__L1349_1353", 0.03333))
else:
    phases["S1349_s3"] = [("L3621_1349__L1349_1353", 0.03333)]
if phases.get("S1349_s0"):
    phases["S1349_s0"].append(("L1202_1349__L1349_1867", 0.73030))
else:
    phases["S1349_s0"] = [("L1202_1349__L1349_1867", 0.73030)]
if phases.get("S1349_s1"):
    phases["S1349_s1"].append(("L1202_1349__L1349_1867", 0.73030))
else:
    phases["S1349_s1"] = [("L1202_1349__L1349_1867", 0.73030)]
if phases.get("S1349_s2"):
    phases["S1349_s2"].append(("L1353_1349__L1349_1867", 0.35))
else:
    phases["S1349_s2"] = [("L1353_1349__L1349_1867", 0.35)]
if phases.get("S1349_s0"):
    phases["S1349_s0"].append(("L1202_1349__L1349_3621", 0.08))
else:
    phases["S1349_s0"] = [("L1202_1349__L1349_3621", 0.08)]
if phases.get("S1349_s1"):
    phases["S1349_s1"].append(("L1202_1349__L1349_3621", 0.08))
else:
    phases["S1349_s1"] = [("L1202_1349__L1349_3621", 0.08)]
if phases.get("S1349_s3"):
    phases["S1349_s3"].append(("L1353_1349__L1349_3621", 0.16667))
else:
    phases["S1349_s3"] = [("L1353_1349__L1349_3621", 0.16667)]
if phases.get("S1349_s1"):
    phases["S1349_s1"].append(("L1867_1349__L1349_3621", 0.00388))
else:
    phases["S1349_s1"] = [("L1867_1349__L1349_3621", 0.00388)]
if phases.get("S1352_s1"):
    phases["S1352_s1"].append(("L1233_1352__L1352_1353", 0.27778))
else:
    phases["S1352_s1"] = [("L1233_1352__L1352_1353", 0.27778)]
if phases.get("S1352_s0"):
    phases["S1352_s0"].append(("L1867_1352__L1352_1353", 0.08333))
else:
    phases["S1352_s0"] = [("L1867_1352__L1352_1353", 0.08333)]
if phases.get("S1352_s0"):
    phases["S1352_s0"].append(("L1216_1352__L1352_1867", 0.15385))
else:
    phases["S1352_s0"] = [("L1216_1352__L1352_1867", 0.15385)]
if phases.get("S1352_s1"):
    phases["S1352_s1"].append(("L1233_1352__L1352_1867", 0.19192))
else:
    phases["S1352_s1"] = [("L1233_1352__L1352_1867", 0.19192)]
if phases.get("S1353_s0"):
    phases["S1353_s0"].append(("L6014_1353__L1353_1349", 0.24643))
else:
    phases["S1353_s0"] = [("L6014_1353__L1353_1349", 0.24643)]
if phases.get("S1353_s1"):
    phases["S1353_s1"].append(("L6159_1353__L1353_1349", 0.0525))
else:
    phases["S1353_s1"] = [("L6159_1353__L1353_1349", 0.0525)]
if phases.get("S1353_s1"):
    phases["S1353_s1"].append(("L1349_1353__L1353_1352", 0.0075))
else:
    phases["S1353_s1"] = [("L1349_1353__L1353_1352", 0.0075)]
if phases.get("S1353_s0"):
    phases["S1353_s0"].append(("L6014_1353__L1353_1352", 0.075))
else:
    phases["S1353_s0"] = [("L6014_1353__L1353_1352", 0.075)]
if phases.get("S1353_s1"):
    phases["S1353_s1"].append(("L6159_1353__L1353_1352", 0.03))
else:
    phases["S1353_s1"] = [("L6159_1353__L1353_1352", 0.03)]
if phases.get("S1353_s0"):
    phases["S1353_s0"].append(("L1352_1353__L1353_6014", 0.48837))
else:
    phases["S1353_s0"] = [("L1352_1353__L1353_6014", 0.48837)]
if phases.get("S1353_s2"):
    phases["S1353_s2"].append(("L1352_1353__L1353_6014", 0.72414))
else:
    phases["S1353_s2"] = [("L1352_1353__L1353_6014", 0.72414)]
if phases.get("S1867_s2"):
    phases["S1867_s2"].append(("L1352_1867__L1867_1349", 0.33333))
else:
    phases["S1867_s2"] = [("L1352_1867__L1867_1349", 0.33333)]
if phases.get("S1867_s2"):
    phases["S1867_s2"].append(("L3621_1867__L1867_1349", 0.125))
else:
    phases["S1867_s2"] = [("L3621_1867__L1867_1349", 0.125)]
if phases.get("S1867_s1"):
    phases["S1867_s1"].append(("L4574_1867__L1867_1349", 0.73077))
else:
    phases["S1867_s1"] = [("L4574_1867__L1867_1349", 0.73077)]
if phases.get("S1867_s0"):
    phases["S1867_s0"].append(("L1349_1867__L1867_1352", 0.07547))
else:
    phases["S1867_s0"] = [("L1349_1867__L1867_1352", 0.07547)]
if phases.get("S1867_s1"):
    phases["S1867_s1"].append(("L1349_1867__L1867_1352", 0.07547))
else:
    phases["S1867_s1"] = [("L1349_1867__L1867_1352", 0.07547)]
if phases.get("S1867_s2"):
    phases["S1867_s2"].append(("L3621_1867__L1867_1352", 0.25))
else:
    phases["S1867_s2"] = [("L3621_1867__L1867_1352", 0.25)]
if phases.get("S1867_s1"):
    phases["S1867_s1"].append(("L4574_1867__L1867_1352", 0.03419))
else:
    phases["S1867_s1"] = [("L4574_1867__L1867_1352", 0.03419)]
if phases.get("S1867_s2"):
    phases["S1867_s2"].append(("L1352_1867__L1867_3621", 0.21875))
else:
    phases["S1867_s2"] = [("L1352_1867__L1867_3621", 0.21875)]
if phases.get("S1867_s1"):
    phases["S1867_s1"].append(("L4574_1867__L1867_3621", 0.04273))
else:
    phases["S1867_s1"] = [("L4574_1867__L1867_3621", 0.04273)]
if phases.get("S1867_s0"):
    phases["S1867_s0"].append(("L1349_1867__L1867_4574", 0.76730))
else:
    phases["S1867_s0"] = [("L1349_1867__L1867_4574", 0.76730)]
if phases.get("S1867_s1"):
    phases["S1867_s1"].append(("L1349_1867__L1867_4574", 0.76730))
else:
    phases["S1867_s1"] = [("L1349_1867__L1867_4574", 0.76730)]
if phases.get("S1867_s2"):
    phases["S1867_s2"].append(("L1352_1867__L1867_4574", 0.11458))
else:
    phases["S1867_s2"] = [("L1352_1867__L1867_4574", 0.11458)]
if phases.get("S1867_s2"):
    phases["S1867_s2"].append(("L3621_1867__L1867_4574", 0.21875))
else:
    phases["S1867_s2"] = [("L3621_1867__L1867_4574", 0.21875)]
if phases.get("fake"):
    phases["fake"].append(("outside__L3621_1867", 0.085))
else:
    phases["fake"] = [("outside__L3621_1867", 0.085)]
if phases.get("fake"):
    phases["fake"].append(("outside__L5840_6013", 0.08333))
else:
    phases["fake"] = [("outside__L5840_6013", 0.08333)]
if phases.get("S6013_s2"):
    phases["S6013_s2"].append(("L5840_6013__L6013_1202", 0.16667))
else:
    phases["S6013_s2"] = [("L5840_6013__L6013_1202", 0.16667)]
if phases.get("S6013_s1"):
    phases["S6013_s1"].append(("L6014_6013__L6013_1202", 0.51010))
else:
    phases["S6013_s1"] = [("L6014_6013__L6013_1202", 0.51010)]
if phases.get("S6013_s0"):
    phases["S6013_s0"].append(("L1202_6013__L6013_5840", 0.19774))
else:
    phases["S6013_s0"] = [("L1202_6013__L6013_5840", 0.19774)]
if phases.get("S6013_s1"):
    phases["S6013_s1"].append(("L1202_6013__L6013_5840", 0.19774))
else:
    phases["S6013_s1"] = [("L1202_6013__L6013_5840", 0.19774)]
if phases.get("S6013_s1"):
    phases["S6013_s1"].append(("L6014_6013__L6013_5840", 0.02020))
else:
    phases["S6013_s1"] = [("L6014_6013__L6013_5840", 0.02020)]
if phases.get("S6013_s0"):
    phases["S6013_s0"].append(("L1202_6013__L6013_6014", 0.14972))
else:
    phases["S6013_s0"] = [("L1202_6013__L6013_6014", 0.14972)]
if phases.get("S6013_s1"):
    phases["S6013_s1"].append(("L1202_6013__L6013_6014", 0.14972))
else:
    phases["S6013_s1"] = [("L1202_6013__L6013_6014", 0.14972)]
if phases.get("S6013_s2"):
    phases["S6013_s2"].append(("L5840_6013__L6013_6014", 0.06349))
else:
    phases["S6013_s2"] = [("L5840_6013__L6013_6014", 0.06349)]
if phases.get("S6014_s0"):
    phases["S6014_s0"].append(("L6013_6014__L6014_1353", 0.05625))
else:
    phases["S6014_s0"] = [("L6013_6014__L6014_1353", 0.05625)]
if phases.get("S6014_s1"):
    phases["S6014_s1"].append(("L6159_6014__L6014_1353", 0.4))
else:
    phases["S6014_s1"] = [("L6159_6014__L6014_1353", 0.4)]
if phases.get("S6014_s3"):
    phases["S6014_s3"].append(("L1353_6014__L6014_6013", 0.10714))
else:
    phases["S6014_s3"] = [("L1353_6014__L6014_6013", 0.10714)]
if phases.get("S6014_s0"):
    phases["S6014_s0"].append(("L6159_6014__L6014_6013", 0.37105))
else:
    phases["S6014_s0"] = [("L6159_6014__L6014_6013", 0.37105)]
if phases.get("S6014_s1"):
    phases["S6014_s1"].append(("L6159_6014__L6014_6013", 0.37105))
else:
    phases["S6014_s1"] = [("L6159_6014__L6014_6013", 0.37105)]
if phases.get("fake"):
    phases["fake"].append(("outside__L6159_1353", 0.01667))
else:
    phases["fake"] = [("outside__L6159_1353", 0.01667)]
if phases.get("fake"):
    phases["fake"].append(("outside__L6159_6014", 0.15167))
else:
    phases["fake"] = [("outside__L6159_6014", 0.15167)]
if phases.get("fake"):
    phases["fake"].append(("L1202_3967__outside", 0.49333))
else:
    phases["fake"] = [("L1202_3967__outside", 0.49333)]
if phases.get("S1352_s0"):
    phases["S1352_s0"].append(("L1216_1352__outside", 0.10256))
else: phases["S1352_s0"] = [("L1216_1352__outside", 0.10256)]
if phases.get("S1352_s1"):
    phases["S1352_s1"].append(("L1233_1352__outside", 0.06061))
else:
    phases["S1352_s1"] = [("L1233_1352__outside", 0.06061)]
if phases.get("S1353_s1"):
    phases["S1353_s1"].append(("L1349_1353__outside", 0.045))
else:
    phases["S1353_s1"] = [("L1349_1353__outside", 0.045)]
if phases.get("fake"):
    phases["fake"].append(("L1349_3621__outside", 0.075))
else:
    phases["fake"] = [("L1349_3621__outside", 0.075)]
if phases.get("S1353_s0"):
    phases["S1353_s0"].append(("L1352_1353__outside", 0.19535))
else:
    phases["S1353_s0"] = [("L1352_1353__outside", 0.19535)]
if phases.get("S1353_s2"):
    phases["S1353_s2"].append(("L1352_1353__outside", 0.28966))
else:
    phases["S1353_s2"] = [("L1352_1353__outside", 0.28966)]
if phases.get("S1352_s1"):
    phases["S1352_s1"].append(("L1353_1352__outside", 0.05556))
else:
    phases["S1352_s1"] = [("L1353_1352__outside", 0.05556)]
if phases.get("S1352_s1"):
    phases["S1352_s1"].append(("L1353_1352__outside", 0.00505))
else:
    phases["S1352_s1"] = [("L1353_1352__outside", 0.00505)]
if phases.get("S6014_s2"):
    phases["S6014_s2"].append(("L1353_6014__outside", 0.01714))
else:
    phases["S6014_s2"] = [("L1353_6014__outside", 0.01714)]
if phases.get("S6014_s3"):
    phases["S6014_s3"].append(("L1353_6014__outside", 0.01714))
else:
    phases["S6014_s3"] = [("L1353_6014__outside", 0.01714)]
if phases.get("S1352_s0"):
    phases["S1352_s0"].append(("L1867_1352__outside", 0.14744))
else:
    phases["S1352_s0"] = [("L1867_1352__outside", 0.14744)]
if phases.get("S1352_s0"):
    phases["S1352_s0"].append(("L1867_1352__outside", 0.25641))
else:
    phases["S1352_s0"] = [("L1867_1352__outside", 0.25641)]
if phases.get("fake"):
    phases["fake"].append(("L1867_3621__outside", 0.04833))
else:
    phases["fake"] = [("L1867_3621__outside", 0.04833)]
if phases.get("fake"):
    phases["fake"].append(("L1867_4574__outside", 0.46833))
else:
    phases["fake"] = [("L1867_4574__outside", 0.46833)]
#if phases.get("fake"):
#    phases["fake"].append(("L6013_5840__outside", 0.13833))
#else:
#    phases["fake"] = [("L6013_5840__outside", 0.13833)]
if phases.get("S6014_s0"):
    phases["S6014_s0"].append(("L6013_6014__outside", 0.31875))
else:
    phases["S6014_s0"] = [("L6013_6014__outside", 0.31875)]

# Network B

if phases.get("S1202b_s0"):
    phases["S1202b_s0"].append(("L3966b_1202b__L1202b_1349b", 0.64522))
else:
    phases["S1202b_s0"] = [("L3966b_1202b__L1202b_1349b", 0.64522)]
if phases.get("S1202b_s1"):
    phases["S1202b_s1"].append(("L3966b_1202b__L1202b_1349b", 0.64522))
else:
    phases["S1202b_s1"] = [("L3966b_1202b__L1202b_1349b", 0.64522)]
if phases.get("S1202b_s2"):
    phases["S1202b_s2"].append(("L3966b_1202b__L1202b_1349b", 0.64522))
else:
    phases["S1202b_s2"] = [("L3966b_1202b__L1202b_1349b", 0.64522)]
if phases.get("S1202b_s3"):
    phases["S1202b_s3"].append(("L3966b_1202b__L1202b_1349b", 0.64522))
else:
    phases["S1202b_s3"] = [("L3966b_1202b__L1202b_1349b", 0.64522)]
if phases.get("S1202b_s6"):
    phases["S1202b_s6"].append(("L6013b_1202b__L1202b_1349b", 0.165))
else:
    phases["S1202b_s6"] = [("L6013b_1202b__L1202b_1349b", 0.165)]
if phases.get("S1202b_s3"):
    phases["S1202b_s3"].append(("L1349b_1202b__L1202b_3967b", 0.825))
else:
    phases["S1202b_s3"] = [("L1349b_1202b__L1202b_3967b", 0.825)]
if phases.get("S1202b_s4"):
    phases["S1202b_s4"].append(("L1349b_1202b__L1202b_3967b", 0.825))
else:
    phases["S1202b_s4"] = [("L1349b_1202b__L1202b_3967b", 0.825)]
if phases.get("S1202b_s0"):
    phases["S1202b_s0"].append(("L6013b_1202b__L1202b_3967b", 0.41067))
else:
    phases["S1202b_s0"] = [("L6013b_1202b__L1202b_3967b", 0.41067)]
if phases.get("S1202b_s1"):
    phases["S1202b_s1"].append(("L6013b_1202b__L1202b_3967b", 0.41067))
else:
    phases["S1202b_s1"] = [("L6013b_1202b__L1202b_3967b", 0.41067)]
if phases.get("S1202b_s5"):
    phases["S1202b_s5"].append(("L6013b_1202b__L1202b_3967b", 0.41067))
else:
    phases["S1202b_s5"] = [("L6013b_1202b__L1202b_3967b", 0.41067)]
if phases.get("S1202b_s6"):
    phases["S1202b_s6"].append(("L6013b_1202b__L1202b_3967b", 0.41067))
else:
    phases["S1202b_s6"] = [("L6013b_1202b__L1202b_3967b", 0.41067)]
if phases.get("S1202b_s2"):
    phases["S1202b_s2"].append(("L1349b_1202b__L1202b_6013b", 0.11138))
else:
    phases["S1202b_s2"] = [("L1349b_1202b__L1202b_6013b", 0.11138)]
if phases.get("S1202b_s3"):
    phases["S1202b_s3"].append(("L1349b_1202b__L1202b_6013b", 0.11138))
else:
    phases["S1202b_s3"] = [("L1349b_1202b__L1202b_6013b", 0.11138)]
if phases.get("S1202b_s4"):
    phases["S1202b_s4"].append(("L1349b_1202b__L1202b_6013b", 0.11138))
else:
    phases["S1202b_s4"] = [("L1349b_1202b__L1202b_6013b", 0.11138)]
if phases.get("S1202b_s0"):
    phases["S1202b_s0"].append(("L3966b_1202b__L1202b_6013b", 0.71739))
else:
    phases["S1202b_s0"] = [("L3966b_1202b__L1202b_6013b", 0.71739)]
if phases.get("fake"):
    phases["fake"].append(("outside__L1216b_1352b", 0.075))
else:
    phases["fake"] = [("outside__L1216b_1352b", 0.075)]
if phases.get("fake"):
    phases["fake"].append(("L5840_1233b__L1233b_1352b", 0.17667))  # Connects
else:
    phases["fake"] = [("L5840_1233b__L1233b_1352b", 0.17667)]
if phases.get("S1349b_s0"):
    phases["S1349b_s0"].append(("L1353_1349b__L1349b_1202b", 0.01961))
else:
    phases["S1349b_s0"] = [("L1353b_1349b__L1349b_1202b", 0.01961)]
if phases.get("S1349b_s3"):
    phases["S1349b_s3"].append(("L1353b_1349b__L1349b_1202b", 0.01961))
else:
    phases["S1349b_s3"] = [("L1353b_1349b__L1349b_1202b", 0.01961)]
if phases.get("S1349b_s1"):
    phases["S1349b_s1"].append(("L1867b_1349b__L1349b_1202b", 0.79845))
else:
    phases["S1349b_s1"] = [("L1867b_1349b__L1349b_1202b", 0.79845)]
if phases.get("S1349b_s2"):
    phases["S1349b_s2"].append(("L3621b_1349b__L1349b_1202b", 0.33333))
else:
    phases["S1349b_s2"] = [("L3621b_1349b__L1349b_1202b", 0.33333)]
if phases.get("S1349b_s1"):
    phases["S1349b_s1"].append(("L1867b_1349b__L1349b_1353b", 0.03876))
else:
    phases["S1349b_s1"] = [("L1867b_1349b__L1349b_1353b", 0.03876)]
if phases.get("S1349b_s3"):
    phases["S1349b_s3"].append(("L3621b_1349b__L1349b_1353b", 0.03333))
else:
    phases["S1349b_s3"] = [("L3621b_1349b__L1349b_1353b", 0.03333)]
if phases.get("S1349b_s0"):
    phases["S1349b_s0"].append(("L1202b_1349b__L1349b_1867b", 0.73030))
else:
    phases["S1349b_s0"] = [("L1202b_1349b__L1349b_1867b", 0.73030)]
if phases.get("S1349b_s1"):
    phases["S1349b_s1"].append(("L1202b_1349b__L1349b_1867b", 0.73030))
else:
    phases["S1349b_s1"] = [("L1202b_1349b__L1349b_1867b", 0.73030)]
if phases.get("S1349b_s2"):
    phases["S1349b_s2"].append(("L1353b_1349b__L1349b_1867b", 0.35))
else:
    phases["S1349b_s2"] = [("L1353b_1349b__L1349b_1867b", 0.35)]
if phases.get("S1349b_s0"):
    phases["S1349b_s0"].append(("L1202b_1349b__L1349b_3621b", 0.08))
else:
    phases["S1349b_s0"] = [("L1202b_1349b__L1349b_3621b", 0.08)]
if phases.get("S1349b_s1"):
    phases["S1349b_s1"].append(("L1202b_1349b__L1349b_3621b", 0.08))
else:
    phases["S1349b_s1"] = [("L1202b_1349b__L1349b_3621b", 0.08)]
if phases.get("S1349b_s3"):
    phases["S1349b_s3"].append(("L1353b_1349b__L1349b_3621b", 0.16667))
else:
    phases["S1349b_s3"] = [("L1353b_1349b__L1349b_3621b", 0.16667)]
if phases.get("S1349b_s1"):
    phases["S1349b_s1"].append(("L1867b_1349b__L1349b_3621b", 0.00388))
else:
    phases["S1349b_s1"] = [("L1867b_1349b__L1349b_3621b", 0.00388)]
if phases.get("S1352b_s1"):
    phases["S1352b_s1"].append(("L1233b_1352b__L1352b_1353b", 0.27778))
else:
    phases["S1352b_s1"] = [("L1233b_1352b__L1352b_1353b", 0.27778)]
if phases.get("S1352b_s0"):
    phases["S1352b_s0"].append(("L1867b_1352b__L1352b_1353b", 0.08333))
else:
    phases["S1352b_s0"] = [("L1867b_1352b__L1352b_1353b", 0.08333)]
if phases.get("S1352b_s0"):
    phases["S1352b_s0"].append(("L1216b_1352b__L1352b_1867b", 0.15385))
else:
    phases["S1352b_s0"] = [("L1216b_1352b__L1352b_1867b", 0.15385)]
if phases.get("S1352b_s1"):
    phases["S1352b_s1"].append(("L1233b_1352b__L1352b_1867b", 0.19192))
else:
    phases["S1352b_s1"] = [("L1233b_1352b__L1352b_1867b", 0.19192)]
if phases.get("S1353b_s0"):
    phases["S1353b_s0"].append(("L6014b_1353b__L1353b_1349b", 0.24643))
else:
    phases["S1353b_s0"] = [("L6014b_1353b__L1353b_1349b", 0.24643)]
if phases.get("S1353b_s1"):
    phases["S1353b_s1"].append(("L6159b_1353b__L1353b_1349b", 0.0525))
else:
    phases["S1353b_s1"] = [("L6159b_1353b__L1353b_1349b", 0.0525)]
if phases.get("S1353b_s1"):
    phases["S1353b_s1"].append(("L1349b_1353b__L1353b_1352b", 0.0075))
else:
    phases["S1353b_s1"] = [("L1349b_1353b__L1353b_1352b", 0.0075)]
if phases.get("S1353b_s0"):
    phases["S1353b_s0"].append(("L6014b_1353b__L1353b_1352b", 0.075))
else:
    phases["S1353b_s0"] = [("L6014b_1353b__L1353b_1352b", 0.075)]
if phases.get("S1353b_s1"):
    phases["S1353b_s1"].append(("L6159b_1353b__L1353b_1352b", 0.03))
else:
    phases["S1353b_s1"] = [("L6159b_1353b__L1353b_1352b", 0.03)]
if phases.get("S1353b_s0"):
    phases["S1353b_s0"].append(("L1352b_1353b__L1353b_6014b", 0.48837))
else:
    phases["S1353b_s0"] = [("L1352b_1353b__L1353b_6014b", 0.48837)]
if phases.get("S1353b_s2"):
    phases["S1353b_s2"].append(("L1352b_1353b__L1353b_6014b", 0.72414))
else:
    phases["S1353b_s2"] = [("L1352b_1353b__L1353b_6014b", 0.72414)]
if phases.get("S1867b_s2"):
    phases["S1867b_s2"].append(("L1352b_1867b__L1867b_1349b", 0.33333))
else:
    phases["S1867b_s2"] = [("L1352b_1867b__L1867b_1349b", 0.33333)]
if phases.get("S1867b_s2"):
    phases["S1867b_s2"].append(("L3621b_1867b__L1867b_1349b", 0.125))
else:
    phases["S1867b_s2"] = [("L3621b_1867b__L1867b_1349b", 0.125)]
if phases.get("S1867b_s1"):
    phases["S1867b_s1"].append(("L4574b_1867b__L1867b_1349b", 0.73077))
else:
    phases["S1867b_s1"] = [("L4574b_1867b__L1867b_1349b", 0.73077)]
if phases.get("S1867b_s0"):
    phases["S1867b_s0"].append(("L1349b_1867b__L1867b_1352b", 0.07547))
else:
    phases["S1867b_s0"] = [("L1349b_1867b__L1867b_1352b", 0.07547)]
if phases.get("S1867b_s1"):
    phases["S1867b_s1"].append(("L1349b_1867b__L1867b_1352b", 0.07547))
else:
    phases["S1867b_s1"] = [("L1349b_1867b__L1867b_1352b", 0.07547)]
if phases.get("S1867b_s2"):
    phases["S1867b_s2"].append(("L3621b_1867b__L1867b_1352b", 0.25))
else:
    phases["S1867b_s2"] = [("L3621b_1867b__L1867b_1352b", 0.25)]
if phases.get("S1867b_s1"):
    phases["S1867b_s1"].append(("L4574b_1867b__L1867b_1352b", 0.03419))
else:
    phases["S1867b_s1"] = [("L4574b_1867b__L1867b_1352b", 0.03419)]
if phases.get("S1867b_s2"):
    phases["S1867b_s2"].append(("L1352b_1867b__L1867b_3621b", 0.21875))
else:
    phases["S1867b_s2"] = [("L1352b_1867b__L1867b_3621b", 0.21875)]
if phases.get("S1867b_s1"):
    phases["S1867b_s1"].append(("L4574b_1867b__L1867b_3621b", 0.04273))
else:
    phases["S1867b_s1"] = [("L4574b_1867b__L1867b_3621b", 0.04273)]
if phases.get("S1867b_s0"):
    phases["S1867b_s0"].append(("L1349b_1867b__L1867b_4574b", 0.76730))
else:
    phases["S1867b_s0"] = [("L1349b_1867b__L1867b_4574b", 0.76730)]
if phases.get("S1867b_s1"):
    phases["S1867b_s1"].append(("L1349b_1867b__L1867b_4574b", 0.76730))
else:
    phases["S1867b_s1"] = [("L1349b_1867b__L1867b_4574b", 0.76730)]
if phases.get("S1867b_s2"):
    phases["S1867b_s2"].append(("L1352b_1867b__L1867b_4574b", 0.11458))
else:
    phases["S1867b_s2"] = [("L1352b_1867b__L1867b_4574b", 0.11458)]
if phases.get("S1867b_s2"):
    phases["S1867b_s2"].append(("L3621b_1867b__L1867b_4574b", 0.21875))
else:
    phases["S1867b_s2"] = [("L3621b_1867b__L1867b_4574b", 0.21875)]
if phases.get("fake"):
    phases["fake"].append(("outside__L3621b_1867b", 0.085))
else:
    phases["fake"] = [("outside__L3621b_1867b", 0.085)]
if phases.get("fake"):
    phases["fake"].append(("outside__L5840b_6013b", 0.08333))
else:
    phases["fake"] = [("outside__L5840b_6013b", 0.08333)]
if phases.get("S6013b_s2"):
    phases["S6013b_s2"].append(("L5840b_6013b__L6013b_1202b", 0.16667))
else:
    phases["S6013b_s2"] = [("L5840b_6013b__L6013b_1202b", 0.16667)]
if phases.get("S6013b_s1"):
    phases["S6013b_s1"].append(("L6014b_6013b__L6013b_1202b", 0.51010))
else:
    phases["S6013b_s1"] = [("L6014b_6013b__L6013b_1202b", 0.51010)]
if phases.get("S6013b_s0"):
    phases["S6013b_s0"].append(("L1202b_6013b__L6013b_5840b", 0.19774))
else:
    phases["S6013b_s0"] = [("L1202b_6013b__L6013b_5840b", 0.19774)]
if phases.get("S6013b_s1"):
    phases["S6013b_s1"].append(("L1202b_6013b__L6013b_5840b", 0.19774))
else:
    phases["S6013b_s1"] = [("L1202b_6013b__L6013b_5840b", 0.19774)]
if phases.get("S6013b_s1"):
    phases["S6013b_s1"].append(("L6014b_6013b__L6013b_5840b", 0.02020))
else:
    phases["S6013b_s1"] = [("L6014b_6013b__L6013b_5840b", 0.02020)]
if phases.get("S6013b_s0"):
    phases["S6013b_s0"].append(("L1202b_6013b__L6013b_6014b", 0.14972))
else:
    phases["S6013b_s0"] = [("L1202b_6013b__L6013b_6014b", 0.14972)]
if phases.get("S6013b_s1"):
    phases["S6013b_s1"].append(("L1202b_6013b__L6013b_6014b", 0.14972))
else:
    phases["S6013b_s1"] = [("L1202b_6013b__L6013b_6014b", 0.14972)]
if phases.get("S6013b_s2"):
    phases["S6013b_s2"].append(("L5840b_6013b__L6013b_6014b", 0.06349))
else:
    phases["S6013b_s2"] = [("L5840b_6013b__L6013b_6014b", 0.06349)]
if phases.get("S6014b_s0"):
    phases["S6014b_s0"].append(("L6013b_6014b__L6014b_1353b", 0.05625))
else:
    phases["S6014b_s0"] = [("L6013b_6014b__L6014b_1353b", 0.05625)]
if phases.get("S6014b_s1"):
    phases["S6014b_s1"].append(("L6159b_6014b__L6014b_1353b", 0.4))
else:
    phases["S6014b_s1"] = [("L6159b_6014b__L6014b_1353b", 0.4)]
if phases.get("S6014b_s3"):
    phases["S6014b_s3"].append(("L1353b_6014b__L6014b_6013b", 0.10714))
else:
    phases["S6014b_s3"] = [("L1353b_6014b__L6014b_6013b", 0.10714)]
if phases.get("S6014b_s0"):
    phases["S6014b_s0"].append(("L6159b_6014b__L6014b_6013b", 0.37105))
else:
    phases["S6014b_s0"] = [("L6159b_6014b__L6014b_6013b", 0.37105)]
if phases.get("S6014b_s1"):
    phases["S6014b_s1"].append(("L6159b_6014b__L6014b_6013b", 0.37105))
else:
    phases["S6014b_s1"] = [("L6159b_6014b__L6014b_6013b", 0.37105)]
if phases.get("fake"):
    phases["fake"].append(("outside__L6159b_1353b", 0.01667))
else:
    phases["fake"] = [("outside__L6159b_1353b", 0.01667)]
if phases.get("fake"):
    phases["fake"].append(("outside__L6159b_6014b", 0.15167))
else:
    phases["fake"] = [("outside__L6159b_6014b", 0.15167)]
if phases.get("fake"):
    phases["fake"].append(("L1202b_3967b__outside", 0.49333))
else:
    phases["fake"] = [("L1202b_3967b__outside", 0.49333)]
if phases.get("S1352b_s0"):
    phases["S1352b_s0"].append(("L1216b_1352b__outside", 0.10256))
else: phases["S1352b_s0"] = [("L1216b_1352b__outside", 0.10256)]
if phases.get("S1352b_s1"):
    phases["S1352b_s1"].append(("L1233b_1352b__outside", 0.06061))
else:
    phases["S1352b_s1"] = [("L1233b_1352b__outside", 0.06061)]
if phases.get("S1353b_s1"):
    phases["S1353b_s1"].append(("L1349b_1353b__outside", 0.045))
else:
    phases["S1353b_s1"] = [("L1349b_1353b__outside", 0.045)]
if phases.get("fake"):
    phases["fake"].append(("L1349b_3621b__outside", 0.075))
else:
    phases["fake"] = [("L1349b_3621b__outside", 0.075)]
if phases.get("S1353b_s0"):
    phases["S1353b_s0"].append(("L1352b_1353b__outside", 0.19535))
else:
    phases["S1353b_s0"] = [("L1352b_1353b__outside", 0.19535)]
if phases.get("S1353b_s2"):
    phases["S1353b_s2"].append(("L1352b_1353b__outside", 0.28966))
else:
    phases["S1353b_s2"] = [("L1352b_1353b__outside", 0.28966)]
if phases.get("S1352b_s1"):
    phases["S1352b_s1"].append(("L1353b_1352b__outside", 0.05556))
else:
    phases["S1352b_s1"] = [("L1353b_1352b__outside", 0.05556)]
if phases.get("S1352b_s1"):
    phases["S1352b_s1"].append(("L1353b_1352b__outside", 0.00505))
else:
    phases["S1352b_s1"] = [("L1353b_1352b__outside", 0.00505)]
if phases.get("S6014b_s2"):
    phases["S6014b_s2"].append(("L1353b_6014b__outside", 0.01714))
else:
    phases["S6014b_s2"] = [("L1353b_6014b__outside", 0.01714)]
if phases.get("S6014b_s3"):
    phases["S6014b_s3"].append(("L1353b_6014b__outside", 0.01714))
else:
    phases["S6014b_s3"] = [("L1353b_6014b__outside", 0.01714)]
if phases.get("S1352b_s0"):
    phases["S1352b_s0"].append(("L1867b_1352b__outside", 0.14744))
else:
    phases["S1352b_s0"] = [("L1867b_1352b__outside", 0.14744)]
if phases.get("S1352b_s0"):
    phases["S1352b_s0"].append(("L1867b_1352b__outside", 0.25641))
else:
    phases["S1352b_s0"] = [("L1867b_1352b__outside", 0.25641)]
if phases.get("fake"):
    phases["fake"].append(("L1867b_3621b__outside", 0.04833))
else:
    phases["fake"] = [("L1867b_3621b__outside", 0.04833)]
if phases.get("fake"):
    phases["fake"].append(("L1867b_4574b__outside", 0.46833))
else:
    phases["fake"] = [("L1867b_4574b__outside", 0.46833)]
if phases.get("fake"):
    phases["fake"].append(("L6013b_5840b__outside", 0.13833))
else:
    phases["fake"] = [("L6013b_5840b__outside", 0.13833)]
if phases.get("S6014b_s0"):
    phases["S6014b_s0"].append(("L6013b_6014b__outside", 0.31875))
else:
    phases["S6014b_s0"] = [("L6013b_6014b__outside", 0.31875)]


# Connecting edges
if phases.get("fake"):
    phases["fake"].append(("L6013_5840__L5840_1233b", 0.25730))
else:
    phases["fake"] = [("L6013_5840__L5840_1233b", 0.25730)]

if phases.get("fake"):
    phases["fake"].append(("L1233b_5840__L5840_6013", 0.25730))
else:
    phases["fake"] = [("L1233b_5840__L5840_6013", 0.25730)]

if phases.get("fake"):
    phases["fake"].append(("L5840_1233b__L1233b_1352b", 0.25730))
else:
    phases["fake"] = [("L5840_1233b__L1233b_1352b", 0.25730)]
if phases.get("fake"):
    phases["fake"].append(("L1352b_1233b__L1233b_5840", 0.25730))
else:
    phases["fake"] = [("L1352b_1233b__L1233b_5840", 0.25730)]


def init_intersections():
    intersections = {}
    intersections["S1202"] = ("S1202_s0", 0)
    intersections["S1349"] = ("S1349_s0", 0)
    intersections["S1352"] = ("S1352_s0", 0)
    intersections["S1353"] = ("S1353_s0", 0)
    intersections["S1867"] = ("S1867_s0", 0)
    intersections["S6013"] = ("S6013_s0", 0)
    intersections["S6014"] = ("S6014_s0", 0)

    #Bigger network
    intersections["S1202b"] = ("S1202b_s0", 0)
    intersections["S1349b"] = ("S1349b_s0", 0)
    intersections["S1352b"] = ("S1352b_s0", 0)
    intersections["S1353b"] = ("S1353b_s0", 0)
    intersections["S1867b"] = ("S1867b_s0", 0)
    intersections["S6013b"] = ("S6013b_s0", 0)
    intersections["S6014b"] = ("S6014b_s0", 0)
    return intersections


def init_goal():
    goal = {}
    goal["L4574_1867"] = 50.0
    goal["L3966_1202"] = 50.0
    goal["L3621_1349"] = 50.0
    return goal


def connect(east_west, north_south):
    intersections = []
    m = east_west
    n = north_south
    for i in range(n):
        for j in range(m):
            in_queues = []
            out_queues = []
            exceptions = dict()
            for q in range(4):
                queue = j*4+q+1+i*n*4
                in_queues.append(queue)
            north = (i-1)*m*4+j*4+4
            if north < 0:
                north = 0
            south = (i+1)*m*4+j*4+2
            if south > m*n*4:
                south = 0
            east = i*m*4+j*4+5
            if in_queues[3]%(m*4) == 0:
                east = 0
            west = i*m*4+j*4-1
            if in_queues[0]%(m*4) == 1:
                west = 0
            out_queues = list(set([north, south, east, west]))
            if len(out_queues) == 4:
                exceptions[(in_queues[0], west)] = True
                exceptions[(in_queues[1], north)] = True
                exceptions[(in_queues[2], east)] = True
                exceptions[(in_queues[3], south)] = True
            else:
                if in_queues[0] == 1:
                    exceptions[(in_queues[2], east)] = True
                    exceptions[(in_queues[3], south)] = True
                elif in_queues[3] == m*4:
                    exceptions[(in_queues[0], west)] = True
                    exceptions[(in_queues[3], south)] = True
                elif in_queues[0] == m*4*(n-1)+1:
                    exceptions[(in_queues[1], north)] = True
                    exceptions[(in_queues[2], east)] = True
                else: #in_queues[3] == m*n:
                    exceptions[(in_queues[0], west)] = True
                    exceptions[(in_queues[1], north)] = True
            intersections.append((in_queues, out_queues, exceptions))
    queues = n * m * 4
    sink = 1
    return queues + sink, intersections

if __name__ == "__main__":
    pass






