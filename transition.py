# from gurobipy import *
from scipy.optimize import linprog
import numpy as np
import time

def maximize_flows(rates={}, queues={}, lp_solver=0):

    if lp_solver == 0:
        start_time = time.clock()

        x_index = {}

        x_index['L1202_1349__L1349_1867'] = 0
        x_index['L1202_1349__L1349_3621'] = 1
        x_index['L1202_3967__outside'] = 2
        x_index['L1202_6013__L6013_5840'] = 3
        x_index['L1202_6013__L6013_6014'] = 4
        x_index['L1216_1352__L1352_1867'] = 5
        x_index['L1216_1352__outside'] = 6
        x_index['L1233_1352__L1352_1353'] = 7
        x_index['L1233_1352__L1352_1867'] = 8
        x_index['L1233_1352__outside'] = 9
        x_index['L1349_1202__L1202_3967'] = 10
        x_index['L1349_1202__L1202_6013'] = 11
        x_index['L1349_1353__L1353_1352'] = 12
        x_index['L1349_1353__outside'] = 13
        x_index['L1349_1867__L1867_1352'] = 14
        x_index['L1349_1867__L1867_4574'] = 15
        x_index['L1349_3621__outside'] = 16
        x_index['L1352_1353__L1353_6014'] = 17
        #x_index['L1352_1353__L1353_6014'] = 18
        x_index['L1352_1353__outside'] = 18
        #x_index['L1352_1353__outside'] = 20
        x_index['L1352_1867__L1867_1349'] = 19
        x_index['L1352_1867__L1867_3621'] = 20
        x_index['L1352_1867__L1867_4574'] = 21
        x_index['L1353_1349__L1349_1202'] = 22
        x_index['L1353_1349__L1349_1867'] = 23
        x_index['L1353_1349__L1349_3621'] = 24
        x_index['L1353_1352__outside'] = 25
        #x_index['L1353_1352__outside'] = 28
        x_index['L1353_6014__L6014_6013'] = 26
        x_index['L1353_6014__outside'] = 27
        x_index['L1867_1349__L1349_1202'] = 28
        x_index['L1867_1349__L1349_1353'] = 29
        x_index['L1867_1349__L1349_3621'] = 30
        x_index['L1867_1352__L1352_1353'] = 31
        x_index['L1867_1352__outside'] = 32
        #x_index['L1867_1352__outside'] = 36
        x_index['L1867_3621__outside'] = 33
        x_index['L1867_4574__outside'] = 34
        x_index['L3621_1349__L1349_1202'] = 35
        x_index['L3621_1349__L1349_1353'] = 36
        x_index['L3621_1867__L1867_1349'] = 37
        x_index['L3621_1867__L1867_1352'] = 38
        x_index['L3621_1867__L1867_4574'] = 39
        x_index['L3966_1202__L1202_1349'] = 40
        x_index['L3966_1202__L1202_6013'] = 41
        x_index['L4574_1867__L1867_1349'] = 42
        x_index['L4574_1867__L1867_1352'] = 43
        x_index['L4574_1867__L1867_3621'] = 44
        x_index['L5840_6013__L6013_1202'] = 45
        x_index['L5840_6013__L6013_6014'] = 46
        x_index['L6013_1202__L1202_1349'] = 47
        x_index['L6013_1202__L1202_3967'] = 48
        x_index['L6013_5840__outside'] = 49
        x_index['L6013_6014__L6014_1353'] = 50
        x_index['L6013_6014__outside'] = 51
        x_index['L6014_1353__L1353_1349'] = 52
        x_index['L6014_1353__L1353_1352'] = 53
        x_index['L6014_6013__L6013_1202'] = 54
        x_index['L6014_6013__L6013_5840'] = 55
        x_index['L6159_1353__L1353_1349'] = 56
        x_index['L6159_1353__L1353_1352'] = 57
        x_index['L6159_6014__L6014_1353'] = 58
        x_index['L6159_6014__L6014_6013'] = 59
        x_index['outside__L1216_1352'] = 60
        x_index['outside__L1233_1352'] = 61
        x_index['outside__L3621_1867'] = 62
        x_index['outside__L5840_6013'] = 63
        x_index['outside__L6159_1353'] = 64
        x_index['outside__L6159_6014'] = 65

        c = np.empty(66)
        c.fill(-1)  # Because scipy.linprog can only minimize
        b = []
        A = []

        cap_L1202_1349 = np.empty(len(c))
        cap_L1202_1349.fill(0)
        cap_L1202_1349[x_index['L6013_1202__L1202_1349']] = 1
        cap_L1202_1349[x_index['L3966_1202__L1202_1349']] = 1
        cap_L1202_1349[x_index['L1202_1349__L1349_1867']] = -1
        cap_L1202_1349[x_index['L1202_1349__L1349_3621']] = -1
        A.append(cap_L1202_1349)
        b.append(88 - queues["L1202_1349"])

        cur_L1202_1349 = np.empty(len(c))
        cur_L1202_1349.fill(0)
        cur_L1202_1349[x_index['L1202_1349__L1349_1867']] = 1
        cur_L1202_1349[x_index['L1202_1349__L1349_3621']] = 1
        A.append(cur_L1202_1349)
        b.append(queues["L1202_1349"])

        cap_L1202_3967 = np.empty(len(c))
        cap_L1202_3967.fill(0)
        cap_L1202_3967[x_index['L6013_1202__L1202_3967']] = 1
        cap_L1202_3967[x_index['L1349_1202__L1202_3967']] = 1
        cap_L1202_3967[x_index['L1202_3967__outside']] = -1
        A.append(cap_L1202_3967)
        b.append(138 - queues["L1202_3967"])

        cur_L1202_3967 = np.empty(len(c))
        cur_L1202_3967.fill(0)
        cur_L1202_3967[x_index['L1202_3967__outside']] = 1
        A.append(cur_L1202_3967)
        b.append(queues["L1202_3967"])

        cap_L1202_6013 = np.empty(len(c))
        cap_L1202_6013.fill(0)
        cap_L1202_6013[x_index['L1349_1202__L1202_6013']] = 1
        cap_L1202_6013[x_index['L3966_1202__L1202_6013']] = 1
        cap_L1202_6013[x_index['L1202_6013__L6013_5840']] = -1
        cap_L1202_6013[x_index['L1202_6013__L6013_6014']] = -1
        A.append(cap_L1202_6013)
        b.append(61 - queues["L1202_6013"])

        cur_L1202_6013 = np.empty(len(c))
        cur_L1202_6013.fill(0)
        cur_L1202_6013[x_index['L1202_6013__L6013_5840']] = 1
        cur_L1202_6013[x_index['L1202_6013__L6013_6014']] = 1
        A.append(cur_L1202_6013)
        b.append(queues["L1202_6013"])

        cap_L1216_1352 = np.empty(len(c))
        cap_L1216_1352.fill(0)
        cap_L1216_1352[x_index['outside__L1216_1352']] = 1
        cap_L1216_1352[x_index['L1216_1352__L1352_1867']] = -1
        cap_L1216_1352[x_index['L1216_1352__outside']] = -1
        A.append(cap_L1216_1352)
        b.append(13 - queues["L1216_1352"])

        cur_L1216_1352 = np.empty(len(c))
        cur_L1216_1352.fill(0)
        cur_L1216_1352[x_index['L1216_1352__L1352_1867']] = 1
        cur_L1216_1352[x_index['L1216_1352__outside']] = 1
        A.append(cur_L1216_1352)
        b.append(queues["L1216_1352"])

        cap_L1233_1352 = np.empty(len(c))
        cap_L1233_1352.fill(0)
        cap_L1233_1352[x_index['outside__L1233_1352']] = 1
        cap_L1233_1352[x_index['L1233_1352__L1352_1353']] = -1
        cap_L1233_1352[x_index['L1233_1352__L1352_1867']] = -1
        cap_L1233_1352[x_index['L1233_1352__outside']] = -1
        A.append(cap_L1233_1352)
        b.append(30 - queues["L1233_1352"])

        cur_L1233_1352 = np.empty(len(c))
        cur_L1233_1352.fill(0)
        cur_L1233_1352[x_index['L1233_1352__L1352_1353']] = 1
        cur_L1233_1352[x_index['L1233_1352__L1352_1867']] = 1
        cur_L1233_1352[x_index['L1233_1352__outside']] = 1
        A.append(cur_L1233_1352)
        b.append(queues["L1233_1352"])

        cap_L1349_1202 = np.empty(len(c))
        cap_L1349_1202.fill(0)
        cap_L1349_1202[x_index['L1353_1349__L1349_1202']] = 1
        cap_L1349_1202[x_index['L3621_1349__L1349_1202']] = 1
        cap_L1349_1202[x_index['L1867_1349__L1349_1202']] = 1
        cap_L1349_1202[x_index['L1349_1202__L1202_3967']] = -1
        cap_L1349_1202[x_index['L1349_1202__L1202_6013']] = -1
        A.append(cap_L1349_1202)
        b.append(89 - queues["L1349_1202"])

        cur_L1349_1202 = np.empty(len(c))
        cur_L1349_1202.fill(0)
        cur_L1349_1202[x_index['L1349_1202__L1202_3967']] = 1
        cur_L1349_1202[x_index['L1349_1202__L1202_6013']] = 1
        A.append(cur_L1349_1202)
        b.append(queues["L1349_1202"])

        cap_L1349_1353 = np.empty(len(c))
        cap_L1349_1353.fill(0)
        cap_L1349_1353[x_index['L3621_1349__L1349_1353']] = 1
        cap_L1349_1353[x_index['L1867_1349__L1349_1353']] = 1
        cap_L1349_1353[x_index['L1349_1353__L1353_1352']] = -1
        cap_L1349_1353[x_index['L1349_1353__outside']] = -1
        A.append(cap_L1349_1353)
        b.append(78 - queues["L1349_1353"])

        cur_L1349_1353 = np.empty(len(c))
        cur_L1349_1353.fill(0)
        cur_L1349_1353[x_index['L1349_1353__L1353_1352']] = 1
        cur_L1349_1353[x_index['L1349_1353__outside']] = 1
        A.append(cur_L1349_1353)
        b.append(queues["L1349_1353"])

        cap_L1349_1867 = np.empty(len(c))
        cap_L1349_1867.fill(0)
        cap_L1349_1867[x_index['L1353_1349__L1349_1867']] = 1
        cap_L1349_1867[x_index['L1202_1349__L1349_1867']] = 1
        cap_L1349_1867[x_index['L1349_1867__L1867_1352']] = -1
        cap_L1349_1867[x_index['L1349_1867__L1867_4574']] = -1
        A.append(cap_L1349_1867)
        b.append(63 - queues["L1349_1867"])

        cur_L1349_1867 = np.empty(len(c))
        cur_L1349_1867.fill(0)
        cur_L1349_1867[x_index['L1349_1867__L1867_1352']] = 1
        cur_L1349_1867[x_index['L1349_1867__L1867_4574']] = 1
        A.append(cur_L1349_1867)
        b.append(queues["L1349_1867"])

        cap_L1349_3621 = np.empty(len(c))
        cap_L1349_3621.fill(0)
        cap_L1349_3621[x_index['L1867_1349__L1349_3621']] = 1
        cap_L1349_3621[x_index['L1202_1349__L1349_3621']] = 1
        cap_L1349_3621[x_index['L1353_1349__L1349_3621']] = 1
        cap_L1349_3621[x_index['L1349_3621__outside']] = -1
        A.append(cap_L1349_3621)
        b.append(181 - queues["L1349_3621"])

        cur_L1349_3621 = np.empty(len(c))
        cur_L1349_3621.fill(0)
        cur_L1349_3621[x_index['L1349_3621__outside']] = 1
        A.append(cur_L1349_3621)
        b.append(queues["L1349_3621"])

        cap_L1352_1353 = np.empty(len(c))
        cap_L1352_1353.fill(0)
        cap_L1352_1353[x_index['L1867_1352__L1352_1353']] = 1
        cap_L1352_1353[x_index['L1233_1352__L1352_1353']] = 1
        cap_L1352_1353[x_index['L1352_1353__L1353_6014']] = -1
        cap_L1352_1353[x_index['L1352_1353__outside']] = -1
        A.append(cap_L1352_1353)
        b.append(60 - queues["L1352_1353"])

        cur_L1352_1353 = np.empty(len(c))
        cur_L1352_1353.fill(0)
        cur_L1352_1353[x_index['L1352_1353__L1353_6014']] = 1
        cur_L1352_1353[x_index['L1352_1353__outside']] = 1
        A.append(cur_L1352_1353)
        b.append(queues["L1352_1353"])

        cap_L1352_1867 = np.empty(len(c))
        cap_L1352_1867.fill(0)
        cap_L1352_1867[x_index['L1216_1352__L1352_1867']] = 1
        cap_L1352_1867[x_index['L1233_1352__L1352_1867']] = 1
        cap_L1352_1867[x_index['L1352_1867__L1867_1349']] = -1
        cap_L1352_1867[x_index['L1352_1867__L1867_3621']] = -1
        cap_L1352_1867[x_index['L1352_1867__L1867_4574']] = -1
        A.append(cap_L1352_1867)
        b.append(73 - queues["L1352_1867"])

        cur_L1352_1867 = np.empty(len(c))
        cur_L1352_1867.fill(0)
        cur_L1352_1867[x_index['L1352_1867__L1867_1349']] = 1
        cur_L1352_1867[x_index['L1352_1867__L1867_3621']] = 1
        cur_L1352_1867[x_index['L1352_1867__L1867_4574']] = 1
        A.append(cur_L1352_1867)
        b.append(queues["L1352_1867"])

        cap_L1353_1349 = np.empty(len(c))
        cap_L1353_1349.fill(0)
        cap_L1353_1349[x_index['L6159_1353__L1353_1349']] = 1
        cap_L1353_1349[x_index['L6014_1353__L1353_1349']] = 1
        cap_L1353_1349[x_index['L1353_1349__L1349_1202']] = -1
        cap_L1353_1349[x_index['L1353_1349__L1349_1867']] = -1
        cap_L1353_1349[x_index['L1353_1349__L1349_3621']] = -1
        A.append(cap_L1353_1349)
        b.append(88 - queues["L1353_1349"])

        cur_L1353_1349 = np.empty(len(c))
        cur_L1353_1349.fill(0)
        cur_L1353_1349[x_index['L1353_1349__L1349_1202']] = 1
        cur_L1353_1349[x_index['L1353_1349__L1349_1867']] = 1
        cur_L1353_1349[x_index['L1353_1349__L1349_3621']] = 1
        A.append(cur_L1353_1349)
        b.append(queues["L1353_1349"])

        cap_L1353_1352 = np.empty(len(c))
        cap_L1353_1352.fill(0)
        cap_L1353_1352[x_index['L1349_1353__L1353_1352']] = 1
        cap_L1353_1352[x_index['L6159_1353__L1353_1352']] = 1
        cap_L1353_1352[x_index['L6014_1353__L1353_1352']] = 1
        cap_L1353_1352[x_index['L1353_1352__outside']] = -1
        A.append(cap_L1353_1352)
        b.append(119 - queues["L1353_1352"])

        cur_L1353_1352 = np.empty(len(c))
        cur_L1353_1352.fill(0)
        cur_L1353_1352[x_index['L1353_1352__outside']] = 1
        A.append(cur_L1353_1352)
        b.append(queues["L1353_1352"])

        cap_L1353_6014 = np.empty(len(c))
        cap_L1353_6014.fill(0)
        cap_L1353_6014[x_index['L1352_1353__L1353_6014']] = 1
        cap_L1353_6014[x_index['L1352_1353__L1353_6014']] = 1
        cap_L1353_6014[x_index['L1353_6014__L6014_6013']] = -1
        cap_L1353_6014[x_index['L1353_6014__outside']] = -1
        A.append(cap_L1353_6014)
        b.append(24 - queues["L1353_6014"])

        cur_L1353_6014 = np.empty(len(c))
        cur_L1353_6014.fill(0)
        cur_L1353_6014[x_index['L1353_6014__L6014_6013']] = 1
        cur_L1353_6014[x_index['L1353_6014__outside']] = 1
        A.append(cur_L1353_6014)
        b.append(queues["L1353_6014"])

        cap_L1867_1349 = np.empty(len(c))
        cap_L1867_1349.fill(0)
        cap_L1867_1349[x_index['L3621_1867__L1867_1349']] = 1
        cap_L1867_1349[x_index['L1352_1867__L1867_1349']] = 1
        cap_L1867_1349[x_index['L4574_1867__L1867_1349']] = 1
        cap_L1867_1349[x_index['L1867_1349__L1349_1202']] = -1
        cap_L1867_1349[x_index['L1867_1349__L1349_1353']] = -1
        cap_L1867_1349[x_index['L1867_1349__L1349_3621']] = -1
        A.append(cap_L1867_1349)
        b.append(104 - queues["L1867_1349"])

        cur_L1867_1349 = np.empty(len(c))
        cur_L1867_1349.fill(0)
        cur_L1867_1349[x_index['L1867_1349__L1349_1202']] = 1
        cur_L1867_1349[x_index['L1867_1349__L1349_1353']] = 1
        cur_L1867_1349[x_index['L1867_1349__L1349_3621']] = 1
        A.append(cur_L1867_1349)
        b.append(queues["L1867_1349"])

        cap_L1867_1352 = np.empty(len(c))
        cap_L1867_1352.fill(0)
        cap_L1867_1352[x_index['L4574_1867__L1867_1352']] = 1
        cap_L1867_1352[x_index['L1349_1867__L1867_1352']] = 1
        cap_L1867_1352[x_index['L3621_1867__L1867_1352']] = 1
        cap_L1867_1352[x_index['L1867_1352__L1352_1353']] = -1
        cap_L1867_1352[x_index['L1867_1352__outside']] = -1
        A.append(cap_L1867_1352)
        b.append(128 - queues["L1867_1352"])

        cur_L1867_1352 = np.empty(len(c))
        cur_L1867_1352.fill(0)
        cur_L1867_1352[x_index['L1867_1352__L1352_1353']] = 1
        cur_L1867_1352[x_index['L1867_1352__outside']] = 1
        A.append(cur_L1867_1352)
        b.append(queues["L1867_1352"])

        cap_L1867_3621 = np.empty(len(c))
        cap_L1867_3621.fill(0)
        cap_L1867_3621[x_index['L4574_1867__L1867_3621']] = 1
        cap_L1867_3621[x_index['L1352_1867__L1867_3621']] = 1
        cap_L1867_3621[x_index['L1867_3621__outside']] = -1
        A.append(cap_L1867_3621)
        b.append(19 - queues["L1867_3621"])

        cur_L1867_3621 = np.empty(len(c))
        cur_L1867_3621.fill(0)
        cur_L1867_3621[x_index['L1867_3621__outside']] = 1
        A.append(cur_L1867_3621)
        b.append(queues["L1867_3621"])

        #cap_L1867_3621 = np.empty(len(c))
        #cap_L1867_3621.fill(0)
        #cap_L1867_3621[x_index['L4574_1867__L1867_3621']] = 1
        #cap_L1867_3621[x_index['L1352_1867__L1867_3621']] = 1
        #cap_L1867_3621[x_index['L1867_3621__outside']] = -1
        #A.append(cap_L1867_3621)
        #b.append(62 - queues["L1867_3621"])# A bug? Weaker constraint than above

        #m.addConstr(L1867_3621__outside
        #            <= queues["L1867_3621"])
        cap_L1867_4574 = np.empty(len(c))
        cap_L1867_4574.fill(0)
        cap_L1867_4574[x_index['L1349_1867__L1867_4574']] = 1
        cap_L1867_4574[x_index['L1352_1867__L1867_4574']] = 1
        cap_L1867_4574[x_index['L3621_1867__L1867_4574']] = 1
        cap_L1867_4574[x_index['L1867_4574__outside']] = -1
        A.append(cap_L1867_4574)
        b.append(82 - queues["L1867_4574"])

        cur_L1867_4574 = np.empty(len(c))
        cur_L1867_4574.fill(0)
        cur_L1867_4574[x_index['L1867_4574__outside']] = 1
        A.append(cur_L1867_4574)
        b.append(queues["L1867_4574"])
        #m.addConstr(- L3621_1349__L1349_1202
        #            - L3621_1349__L1349_1353
        #            #+ queues["L3621_1349"]  # Problem initially exceeds capacity
        #            <= 75
        #            , "L3621_1349") # This constraint is always true

        cur_L3621_1349 = np.empty(len(c))
        cur_L3621_1349.fill(0)
        cur_L3621_1349[x_index['L3621_1349__L1349_1202']] = 1
        cur_L3621_1349[x_index['L3621_1349__L1349_1353']] = 1
        A.append(cur_L3621_1349)
        b.append(queues["L3621_1349"])

        cap_L3621_1867 = np.empty(len(c))
        cap_L3621_1867.fill(0)
        cap_L3621_1867[x_index['outside__L3621_1867']] = 1
        cap_L3621_1867[x_index['L3621_1867__L1867_1349']] = -1
        cap_L3621_1867[x_index['L3621_1867__L1867_1352']] = -1
        cap_L3621_1867[x_index['L3621_1867__L1867_4574']] = -1
        A.append(cap_L3621_1867)
        b.append(60 - queues["L3621_1867"])

        cur_L3621_1867 = np.empty(len(c))
        cur_L3621_1867.fill(0)
        cur_L3621_1867[x_index['L3621_1867__L1867_1349']] = 1
        cur_L3621_1867[x_index['L3621_1867__L1867_1352']] = 1
        cur_L3621_1867[x_index['L3621_1867__L1867_4574']] = 1
        A.append(cur_L3621_1867)
        b.append(queues["L3621_1867"])

        #m.addConstr(- L3966_1202__L1202_1349
        #            - L3966_1202__L1202_6013
        #            #+ queues["L3966_1202"]  # Problem initially exceeds capacity
        #            <= 101 # Always true
        #            , "L3966_1202")

        cur_L3966_1202 = np.empty(len(c))
        cur_L3966_1202.fill(0)
        cur_L3966_1202[x_index['L3966_1202__L1202_1349']] = 1
        cur_L3966_1202[x_index['L3966_1202__L1202_6013']] = 1
        A.append(cur_L3966_1202)
        b.append(queues["L3966_1202"])

        #m.addConstr(- L4574_1867__L1867_1349
        #            - L4574_1867__L1867_1352
        #            - L4574_1867__L1867_3621
        #            #+ queues["L4574_1867"]  # Problem initially exceeds capacity
        #            <= 179 # Always true
        #            , "L4574_1867")

        cur_L4574_1867 = np.empty(len(c))
        cur_L4574_1867.fill(0)
        cur_L4574_1867[x_index['L4574_1867__L1867_1349']] = 1
        cur_L4574_1867[x_index['L4574_1867__L1867_1352']] = 1
        cur_L4574_1867[x_index['L4574_1867__L1867_3621']] = 1
        A.append(cur_L4574_1867)
        b.append(queues["L4574_1867"])

        cap_L5840_6013 = np.empty(len(c))
        cap_L5840_6013.fill(0)
        cap_L5840_6013[x_index['outside__L5840_6013']] = 1
        cap_L5840_6013[x_index['L5840_6013__L6013_1202']] = -1
        cap_L5840_6013[x_index['L5840_6013__L6013_6014']] = -1
        A.append(cap_L5840_6013)
        b.append(40 - queues["L5840_6013"])

        cur_L5840_6013 = np.empty(len(c))
        cur_L5840_6013.fill(0)
        cur_L5840_6013[x_index['L5840_6013__L6013_1202']] = 1
        cur_L5840_6013[x_index['L5840_6013__L6013_6014']] = 1
        A.append(cur_L5840_6013)
        b.append(queues["L5840_6013"])

        cap_L6013_1202 = np.empty(len(c))
        cap_L6013_1202.fill(0)
        cap_L6013_1202[x_index['L5840_6013__L6013_1202']] = 1
        cap_L6013_1202[x_index['L6014_6013__L6013_1202']] = 1
        cap_L6013_1202[x_index['L6013_1202__L1202_1349']] = -1
        cap_L6013_1202[x_index['L6013_1202__L1202_3967']] = -1
        A.append(cap_L6013_1202)
        b.append(35 + queues["L6013_1202"])

        cur_L6013_1202 = np.empty(len(c))
        cur_L6013_1202.fill(0)
        cur_L6013_1202[x_index['L6013_1202__L1202_1349']] = 1
        cur_L6013_1202[x_index['L6013_1202__L1202_3967']] = 1
        A.append(cur_L6013_1202)
        b.append(queues["L6013_1202"])

        cap_L6013_5840 = np.empty(len(c))
        cap_L6013_5840.fill(0)
        cap_L6013_5840[x_index['L1202_6013__L6013_5840']] = 1
        cap_L6013_5840[x_index['L6014_6013__L6013_5840']] = 1
        cap_L6013_5840[x_index['L6013_5840__outside']] = -1
        A.append(cap_L6013_5840)
        b.append(24 - queues["L6013_5840"])

        cur_L6013_5840 = np.empty(len(c))
        cur_L6013_5840.fill(0)
        cur_L6013_5840[x_index['L6013_5840__outside']] = 1
        A.append(cur_L6013_5840)
        b.append(queues["L6013_5840"])

        cap_L6013_6014 = np.empty(len(c))
        cap_L6013_6014.fill(0)
        cap_L6013_6014[x_index['L1202_6013__L6013_6014']] = 1
        cap_L6013_6014[x_index['L5840_6013__L6013_6014']] = 1
        cap_L6013_6014[x_index['L6013_6014__L6014_1353']] = -1
        cap_L6013_6014[x_index['L6013_6014__outside']] = -1
        A.append(cap_L6013_6014)
        b.append(94 - queues["L6013_6014"])

        cur_L6013_6014 = np.empty(len(c))
        cur_L6013_6014.fill(0)
        cur_L6013_6014[x_index['L6013_6014__L6014_1353']] = 1
        cur_L6013_6014[x_index['L6013_6014__outside']] = 1
        A.append(cur_L6013_6014)
        b.append(queues["L6013_6014"])

        cap_L6014_1353 = np.empty(len(c))
        cap_L6014_1353.fill(0)
        cap_L6014_1353[x_index['L6013_6014__L6014_1353']] = 1
        cap_L6014_1353[x_index['L6159_6014__L6014_1353']] = 1
        cap_L6014_1353[x_index['L6014_1353__L1353_1349']] = -1
        cap_L6014_1353[x_index['L6014_1353__L1353_1352']] = -1
        A.append(cap_L6014_1353)
        b.append(23 - queues["L6014_1353"])

        cur_L6014_1353 = np.empty(len(c))
        cur_L6014_1353.fill(0)
        cur_L6014_1353[x_index['L6014_1353__L1353_1349']] = 1
        cur_L6014_1353[x_index['L6014_1353__L1353_1352']] = 1
        A.append(cur_L6014_1353)
        b.append(queues["L6014_1353"])

        cap_L6014_6013 = np.empty(len(c))
        cap_L6014_6013.fill(0)
        cap_L6014_6013[x_index['L1353_6014__L6014_6013']] = 1
        cap_L6014_6013[x_index['L6159_6014__L6014_6013']] = 1
        cap_L6014_6013[x_index['L6014_6013__L6013_1202']] = -1
        cap_L6014_6013[x_index['L6014_6013__L6013_5840']] = -1
        A.append(cap_L6014_6013)
        b.append(94 - queues["L6014_6013"])

        cur_L6014_6013 = np.empty(len(c))
        cur_L6014_6013.fill(0)
        cur_L6014_6013[x_index['L6014_6013__L6013_1202']] = 1
        cur_L6014_6013[x_index['L6014_6013__L6013_5840']] = 1
        A.append(cur_L6014_6013)
        b.append(queues["L6014_6013"])

        cap_L6159_1353 = np.empty(len(c))
        cap_L6159_1353.fill(0)
        cap_L6159_1353[x_index['outside__L6159_1353']] = 1
        cap_L6159_1353[x_index['L6159_1353__L1353_1349']] = -1
        cap_L6159_1353[x_index['L6159_1353__L1353_1352']] = -1
        A.append(cap_L6159_1353)
        b.append(24 - queues["L6159_1353"])

        cur_L6159_1353 = np.empty(len(c))
        cur_L6159_1353.fill(0)
        cur_L6159_1353[x_index['L6159_1353__L1353_1349']] = 1
        cur_L6159_1353[x_index['L6159_1353__L1353_1352']] = 1
        A.append(cur_L6159_1353)
        b.append(queues["L6159_1353"])

        cap_L6159_6014 = np.empty(len(c))
        cap_L6159_6014.fill(0)
        cap_L6159_6014[x_index['outside__L6159_6014']] = 1
        cap_L6159_6014[x_index['L6159_6014__L6014_1353']] = -1
        cap_L6159_6014[x_index['L6159_6014__L6014_6013']] = -1
        A.append(cap_L6159_6014)
        b.append(218 - queues["L6159_6014"])

        cur_L6159_6014 = np.empty(len(c))
        cur_L6159_6014.fill(0)
        cur_L6159_6014[x_index['L6159_6014__L6014_1353']] = 1
        cur_L6159_6014[x_index['L6159_6014__L6014_6013']] = 1
        A.append(cur_L6159_6014)
        b.append(queues["L6159_6014"])

        # Maximum flow
        '''
        m.addConstr(L1202_3967_sink <= 0.49333 * t * flows["L1202_3967_sink"])
        m.addConstr(L6013_1202_L1202_3967 <= 0.41067 * t * flows["L6013_1202_L1202_3967"])
        m.addConstr(L1349_1202_L1202_3967 <= 0.825 * t * flows["L1349_1202_L1202_3967"])
        '''
        rate_L1202_1349__L1349_1867 = np.empty(len(c))
        rate_L1202_1349__L1349_3621 = np.empty(len(c))
        rate_L1202_3967__outside = np.empty(len(c))
        rate_L1202_6013__L6013_5840 = np.empty(len(c))
        rate_L1202_6013__L6013_6014 = np.empty(len(c))
        rate_L1216_1352__L1352_1867 = np.empty(len(c))
        rate_L1216_1352__outside = np.empty(len(c))
        rate_L1233_1352__L1352_1353 = np.empty(len(c))
        rate_L1233_1352__L1352_1867 = np.empty(len(c))
        rate_L1233_1352__outside = np.empty(len(c))
        rate_L1349_1202__L1202_3967 = np.empty(len(c))
        rate_L1349_1202__L1202_6013 = np.empty(len(c))
        rate_L1349_1353__L1353_1352 = np.empty(len(c))
        rate_L1349_1353__outside = np.empty(len(c))
        rate_L1349_1867__L1867_1352 = np.empty(len(c))
        rate_L1349_1867__L1867_4574 = np.empty(len(c))
        rate_L1349_3621__outside = np.empty(len(c))
        rate_L1352_1353__L1353_6014 = np.empty(len(c))
        #rate_L1352_1353__L1353_6014 = np.empty(len(c))
        rate_L1352_1353__outside = np.empty(len(c))
        #rate_L1352_1353__outside = np.empty(len(c))
        rate_L1352_1867__L1867_1349 = np.empty(len(c))
        rate_L1352_1867__L1867_3621 = np.empty(len(c))
        rate_L1352_1867__L1867_4574 = np.empty(len(c))
        rate_L1353_1349__L1349_1202 = np.empty(len(c))
        rate_L1353_1349__L1349_1867 = np.empty(len(c))
        rate_L1353_1349__L1349_3621 = np.empty(len(c))
        rate_L1353_1352__outside = np.empty(len(c))
        #rate_L1353_1352__outside = np.empty(len(c))
        rate_L1353_6014__L6014_6013 = np.empty(len(c))
        rate_L1353_6014__outside = np.empty(len(c))
        rate_L1867_1349__L1349_1202 = np.empty(len(c))
        rate_L1867_1349__L1349_1353 = np.empty(len(c))
        rate_L1867_1349__L1349_3621 = np.empty(len(c))
        rate_L1867_1352__L1352_1353 = np.empty(len(c))
        rate_L1867_1352__outside = np.empty(len(c))
        #rate_L1867_1352__outside = np.empty(len(c))
        rate_L1867_3621__outside = np.empty(len(c))
        rate_L1867_4574__outside = np.empty(len(c))
        rate_L3621_1349__L1349_1202 = np.empty(len(c))
        rate_L3621_1349__L1349_1353 = np.empty(len(c))
        rate_L3621_1867__L1867_1349 = np.empty(len(c))
        rate_L3621_1867__L1867_1352 = np.empty(len(c))
        rate_L3621_1867__L1867_4574 = np.empty(len(c))
        rate_L3966_1202__L1202_1349 = np.empty(len(c))
        rate_L3966_1202__L1202_6013 = np.empty(len(c))
        rate_L4574_1867__L1867_1349 = np.empty(len(c))
        rate_L4574_1867__L1867_1352 = np.empty(len(c))
        rate_L4574_1867__L1867_3621 = np.empty(len(c))
        rate_L5840_6013__L6013_1202 = np.empty(len(c))
        rate_L5840_6013__L6013_6014 = np.empty(len(c))
        rate_L6013_1202__L1202_1349 = np.empty(len(c))
        rate_L6013_1202__L1202_3967 = np.empty(len(c))
        rate_L6013_5840__outside = np.empty(len(c))
        rate_L6013_6014__L6014_1353 = np.empty(len(c))
        rate_L6013_6014__outside = np.empty(len(c))
        rate_L6014_1353__L1353_1349 = np.empty(len(c))
        rate_L6014_1353__L1353_1352 = np.empty(len(c))
        rate_L6014_6013__L6013_1202 = np.empty(len(c))
        rate_L6014_6013__L6013_5840 = np.empty(len(c))
        rate_L6159_1353__L1353_1349 = np.empty(len(c))
        rate_L6159_1353__L1353_1352 = np.empty(len(c))
        rate_L6159_6014__L6014_1353 = np.empty(len(c))
        rate_L6159_6014__L6014_6013 = np.empty(len(c))
        rate_outside__L1216_1352 = np.empty(len(c))
        rate_outside__L1233_1352 = np.empty(len(c))
        rate_outside__L3621_1867 = np.empty(len(c))
        rate_outside__L5840_6013 = np.empty(len(c))
        rate_outside__L6159_1353 = np.empty(len(c))
        rate_outside__L6159_6014 = np.empty(len(c))


        rate_L1202_1349__L1349_1867.fill(0)
        rate_L1202_1349__L1349_3621.fill(0)
        rate_L1202_3967__outside.fill(0)
        rate_L1202_6013__L6013_5840.fill(0)
        rate_L1202_6013__L6013_6014.fill(0)
        rate_L1216_1352__L1352_1867.fill(0)
        rate_L1216_1352__outside.fill(0)
        rate_L1233_1352__L1352_1353.fill(0)
        rate_L1233_1352__L1352_1867.fill(0)
        rate_L1233_1352__outside.fill(0)
        rate_L1349_1202__L1202_3967.fill(0)
        rate_L1349_1202__L1202_6013.fill(0)
        rate_L1349_1353__L1353_1352.fill(0)
        rate_L1349_1353__outside.fill(0)
        rate_L1349_1867__L1867_1352.fill(0)
        rate_L1349_1867__L1867_4574.fill(0)
        rate_L1349_3621__outside.fill(0)
        rate_L1352_1353__L1353_6014.fill(0)
        rate_L1352_1353__L1353_6014.fill(0)
        rate_L1352_1353__outside.fill(0)
        rate_L1352_1353__outside.fill(0)
        rate_L1352_1867__L1867_1349.fill(0)
        rate_L1352_1867__L1867_3621.fill(0)
        rate_L1352_1867__L1867_4574.fill(0)
        rate_L1353_1349__L1349_1202.fill(0)
        rate_L1353_1349__L1349_1867.fill(0)
        rate_L1353_1349__L1349_3621.fill(0)
        rate_L1353_1352__outside.fill(0)
        rate_L1353_1352__outside.fill(0)
        rate_L1353_6014__L6014_6013.fill(0)
        rate_L1353_6014__outside.fill(0)
        rate_L1867_1349__L1349_1202.fill(0)
        rate_L1867_1349__L1349_1353.fill(0)
        rate_L1867_1349__L1349_3621.fill(0)
        rate_L1867_1352__L1352_1353.fill(0)
        rate_L1867_1352__outside.fill(0)
        rate_L1867_1352__outside.fill(0)
        rate_L1867_3621__outside.fill(0)
        rate_L1867_4574__outside.fill(0)
        rate_L3621_1349__L1349_1202.fill(0)
        rate_L3621_1349__L1349_1353.fill(0)
        rate_L3621_1867__L1867_1349.fill(0)
        rate_L3621_1867__L1867_1352.fill(0)
        rate_L3621_1867__L1867_4574.fill(0)
        rate_L3966_1202__L1202_1349.fill(0)
        rate_L3966_1202__L1202_6013.fill(0)
        rate_L4574_1867__L1867_1349.fill(0)
        rate_L4574_1867__L1867_1352.fill(0)
        rate_L4574_1867__L1867_3621.fill(0)
        rate_L5840_6013__L6013_1202.fill(0)
        rate_L5840_6013__L6013_6014.fill(0)
        rate_L6013_1202__L1202_1349.fill(0)
        rate_L6013_1202__L1202_3967.fill(0)
        rate_L6013_5840__outside.fill(0)
        rate_L6013_6014__L6014_1353.fill(0)
        rate_L6013_6014__outside.fill(0)
        rate_L6014_1353__L1353_1349.fill(0)
        rate_L6014_1353__L1353_1352.fill(0)
        rate_L6014_6013__L6013_1202.fill(0)
        rate_L6014_6013__L6013_5840.fill(0)
        rate_L6159_1353__L1353_1349.fill(0)
        rate_L6159_1353__L1353_1352.fill(0)
        rate_L6159_6014__L6014_1353.fill(0)
        rate_L6159_6014__L6014_6013.fill(0)
        rate_outside__L1216_1352.fill(0)
        rate_outside__L1233_1352.fill(0)
        rate_outside__L3621_1867.fill(0)
        rate_outside__L5840_6013.fill(0)
        rate_outside__L6159_1353.fill(0)
        rate_outside__L6159_6014.fill(0)

        rate_L1202_1349__L1349_1867[x_index['L1202_1349__L1349_1867']] = 1
        A.append(rate_L1202_1349__L1349_1867)
        b.append(rates["L1202_1349__L1349_1867"])

        rate_L1202_1349__L1349_3621[x_index['L1202_1349__L1349_3621']] = 1
        A.append(rate_L1202_1349__L1349_3621)
        b.append(rates["L1202_1349__L1349_3621"])

        rate_L1202_3967__outside[x_index['L1202_3967__outside']] = 1
        A.append(rate_L1202_3967__outside)
        b.append(rates["L1202_3967__outside"])

        rate_L1202_6013__L6013_5840[x_index['L1202_6013__L6013_5840']] = 1
        A.append(rate_L1202_6013__L6013_5840)
        b.append(rates["L1202_6013__L6013_5840"])

        rate_L1202_6013__L6013_6014[x_index['L1202_6013__L6013_6014']] = 1
        A.append(rate_L1202_6013__L6013_6014)
        b.append(rates["L1202_6013__L6013_6014"])

        rate_L1216_1352__L1352_1867[x_index['L1216_1352__L1352_1867']] = 1
        A.append(rate_L1216_1352__L1352_1867)
        b.append(rates["L1216_1352__L1352_1867"])

        rate_L1216_1352__outside[x_index['L1216_1352__outside']] = 1
        A.append(rate_L1216_1352__outside)
        b.append(rates["L1216_1352__outside"])

        rate_L1233_1352__L1352_1353[x_index['L1233_1352__L1352_1353']] = 1
        A.append(rate_L1233_1352__L1352_1353)
        b.append(rates["L1233_1352__L1352_1353"])

        rate_L1233_1352__L1352_1867[x_index['L1233_1352__L1352_1867']] = 1
        A.append(rate_L1233_1352__L1352_1867)
        b.append(rates["L1233_1352__L1352_1867"])

        rate_L1233_1352__outside[x_index['L1233_1352__outside']] = 1
        A.append(rate_L1233_1352__outside)
        b.append(rates["L1233_1352__outside"])

        rate_L1349_1202__L1202_3967[x_index['L1349_1202__L1202_3967']] = 1
        A.append(rate_L1349_1202__L1202_3967)
        b.append(rates["L1349_1202__L1202_3967"])

        rate_L1349_1202__L1202_6013[x_index['L1349_1202__L1202_6013']] = 1
        A.append(rate_L1349_1202__L1202_6013)
        b.append(rates["L1349_1202__L1202_6013"])

        rate_L1349_1353__L1353_1352[x_index['L1349_1353__L1353_1352']] = 1
        A.append(rate_L1349_1353__L1353_1352)
        b.append(rates["L1349_1353__L1353_1352"])

        rate_L1349_1353__outside[x_index['L1349_1353__outside']] = 1
        A.append(rate_L1349_1353__outside)
        b.append(rates["L1349_1353__outside"])

        rate_L1349_1867__L1867_1352[x_index['L1349_1867__L1867_1352']] = 1
        A.append(rate_L1349_1867__L1867_1352)
        b.append(rates["L1349_1867__L1867_1352"])

        rate_L1349_1867__L1867_4574[x_index['L1349_1867__L1867_4574']] = 1
        A.append(rate_L1349_1867__L1867_4574)
        b.append(rates["L1349_1867__L1867_4574"])

        rate_L1349_3621__outside[x_index['L1349_3621__outside']] = 1
        A.append(rate_L1349_3621__outside)
        b.append(rates["L1349_3621__outside"])

        rate_L1352_1353__L1353_6014[x_index['L1352_1353__L1353_6014']] = 1
        A.append(rate_L1352_1353__L1353_6014)
        b.append(rates["L1352_1353__L1353_6014"])

        #rate_L1352_1353__L1353_6014[x_index['L1352_1353__L1353_6014']] = 1
        #A.append(rate_L1352_1353__L1353_6014)
        #b.append(rates["L1352_1353__L1353_6014"])

        rate_L1352_1353__outside[x_index['L1352_1353__outside']] = 1
        A.append(rate_L1352_1353__outside)
        b.append(rates["L1352_1353__outside"])

        #<= rates["L1352_1353__outside"])

        rate_L1352_1867__L1867_1349[x_index['L1352_1867__L1867_1349']] = 1
        A.append(rate_L1352_1867__L1867_1349)
        b.append(rates["L1352_1867__L1867_1349"])

        rate_L1352_1867__L1867_3621[x_index['L1352_1867__L1867_3621']] = 1
        A.append(rate_L1352_1867__L1867_3621)
        b.append(rates["L1352_1867__L1867_3621"])

        rate_L1352_1867__L1867_4574[x_index['L1352_1867__L1867_4574']] = 1
        A.append(rate_L1352_1867__L1867_4574)
        b.append(rates["L1352_1867__L1867_4574"])

        rate_L1353_1349__L1349_1202[x_index['L1353_1349__L1349_1202']] = 1
        A.append(rate_L1353_1349__L1349_1202)
        b.append(rates["L1353_1349__L1349_1202"])

        rate_L1353_1349__L1349_1867[x_index['L1353_1349__L1349_1867']] = 1
        A.append(rate_L1353_1349__L1349_1867)
        b.append(rates["L1353_1349__L1349_1867"])

        rate_L1353_1349__L1349_3621[x_index['L1353_1349__L1349_3621']] = 1
        A.append(rate_L1353_1349__L1349_3621)
        b.append(rates["L1353_1349__L1349_3621"])

        rate_L1353_1352__outside[x_index['L1353_1352__outside']] = 1
        A.append(rate_L1353_1352__outside)
        b.append(rates["L1353_1352__outside"])

        #rate_L1353_1352__outside[x_index['L1353_1352__outside']] = 1
        #A.append(rate_L1353_1352__outside)
        #b.append(rates["L1353_1352__outside"])

        rate_L1353_6014__L6014_6013[x_index['L1353_6014__L6014_6013']] = 1
        A.append(rate_L1353_6014__L6014_6013)
        b.append(rates["L1353_6014__L6014_6013"])

        rate_L1353_6014__outside[x_index['L1353_6014__outside']] = 1
        A.append(rate_L1353_6014__outside)
        b.append(rates["L1353_6014__outside"])

        rate_L1867_1349__L1349_1202[x_index['L1867_1349__L1349_1202']] = 1
        A.append(rate_L1867_1349__L1349_1202)
        b.append(rates["L1867_1349__L1349_1202"])

        rate_L1867_1349__L1349_1353[x_index['L1867_1349__L1349_1202']] = 1
        A.append(rate_L1867_1349__L1349_1202)
        b.append(rates["L1867_1349__L1349_1353"])

        rate_L1867_1349__L1349_3621[x_index['L1867_1349__L1349_3621']] = 1
        A.append(rate_L1867_1349__L1349_3621)
        b.append(rates["L1867_1349__L1349_3621"])

        rate_L1867_1352__L1352_1353[x_index['L1867_1349__L1349_3621']] = 1
        A.append(rate_L1867_1349__L1349_3621)
        b.append(rates["L1867_1352__L1352_1353"])

        rate_L1867_1352__outside[x_index['L1867_1349__L1349_3621']] = 1
        A.append(rate_L1867_1349__L1349_3621)
        b.append(rates["L1867_1352__outside"])

        # L1867_1352__outside <= rates["L1867_1352__outside"])
        rate_L1867_3621__outside[x_index['L1867_3621__outside']] = 1
        A.append(rate_L1867_3621__outside)
        b.append(rates["L1867_3621__outside"])

        rate_L1867_4574__outside[x_index['L1867_4574__outside']] = 1
        A.append(rate_L1867_4574__outside)
        b.append(rates["L1867_4574__outside"])

        rate_L3621_1349__L1349_1202[x_index['L3621_1349__L1349_1202']] = 1
        A.append(rate_L3621_1349__L1349_1202)
        b.append(rates["L3621_1349__L1349_1202"])

        rate_L3621_1349__L1349_1353[x_index['L3621_1349__L1349_1353']] = 1
        A.append(rate_L3621_1349__L1349_1353)
        b.append(rates["L3621_1349__L1349_1353"])

        rate_L3621_1867__L1867_1349[x_index['L3621_1867__L1867_1349']] = 1
        A.append(rate_L3621_1867__L1867_1349)
        b.append(rates["L3621_1867__L1867_1349"])

        rate_L3621_1867__L1867_1352[x_index['L3621_1867__L1867_1352']] = 1
        A.append(rate_L3621_1867__L1867_1352)
        b.append(rates["L3621_1867__L1867_1352"])

        rate_L3621_1867__L1867_4574[x_index['L3621_1867__L1867_4574']] = 1
        A.append(rate_L3621_1867__L1867_4574)
        b.append(rates["L3621_1867__L1867_4574"])

        rate_L3966_1202__L1202_1349[x_index['L3966_1202__L1202_1349']] = 1
        A.append(rate_L3966_1202__L1202_1349)
        b.append(rates["L3966_1202__L1202_1349"])

        rate_L3966_1202__L1202_6013[x_index['L3966_1202__L1202_6013']] = 1
        A.append(rate_L3966_1202__L1202_6013)
        b.append(rates["L3966_1202__L1202_6013"])

        rate_L4574_1867__L1867_1349[x_index["L4574_1867__L1867_1349"]] = 1
        A.append(rate_L4574_1867__L1867_1349)
        b.append(rates['L4574_1867__L1867_1349'])

        rate_L4574_1867__L1867_1352[x_index["L4574_1867__L1867_1352"]] = 1
        A.append(rate_L4574_1867__L1867_1352)
        b.append(rates["L4574_1867__L1867_1352"])

        rate_L4574_1867__L1867_3621[x_index["L4574_1867__L1867_3621"]] = 1
        A.append(rate_L4574_1867__L1867_3621)
        b.append(rates["L4574_1867__L1867_3621"])

        rate_L5840_6013__L6013_1202[x_index["L5840_6013__L6013_1202"]] = 1
        A.append(rate_L5840_6013__L6013_1202)
        b.append(rates["L5840_6013__L6013_1202"])

        rate_L5840_6013__L6013_6014[x_index["L5840_6013__L6013_6014"]] = 1
        A.append(rate_L5840_6013__L6013_6014)
        b.append(rates["L5840_6013__L6013_6014"])

        rate_L6013_1202__L1202_1349[x_index['L6013_1202__L1202_1349']] = 1
        A.append(rate_L6013_1202__L1202_1349)
        b.append(rates["L6013_1202__L1202_1349"])

        rate_L6013_1202__L1202_3967[x_index['L6013_1202__L1202_3967']] = 1
        A.append(rate_L6013_1202__L1202_3967)
        b.append(rates["L6013_1202__L1202_3967"])

        rate_L6013_5840__outside[x_index['L6013_5840__outside']] = 1
        A.append(rate_L6013_5840__outside)
        b.append(rates["L6013_5840__outside"])

        rate_L6013_6014__L6014_1353[x_index['L6013_6014__L6014_1353']] = 1
        A.append(rate_L6013_6014__L6014_1353)
        b.append(rates["L6013_6014__L6014_1353"])

        rate_L6013_6014__outside[x_index['L6013_6014__outside']] = 1
        A.append(rate_L6013_6014__outside)
        b.append(rates["L6013_6014__outside"])

        rate_L6014_1353__L1353_1349[x_index['L6014_1353__L1353_1349']] = 1
        A.append(rate_L6014_1353__L1353_1349)
        b.append(rates["L6014_1353__L1353_1349"])

        rate_L6014_1353__L1353_1352[x_index['L6014_1353__L1353_1352']] = 1
        A.append(rate_L6014_1353__L1353_1352)
        b.append(rates["L6014_1353__L1353_1352"])

        rate_L6014_6013__L6013_1202[x_index['L6014_6013__L6013_1202']] = 1
        A.append(rate_L6014_6013__L6013_1202)
        b.append(rates["L6014_6013__L6013_1202"])

        rate_L6014_6013__L6013_5840[x_index['L6014_6013__L6013_5840']] = 1
        A.append(rate_L6014_6013__L6013_5840)
        b.append(rates["L6014_6013__L6013_5840"])

        rate_L6159_1353__L1353_1349[x_index['L6159_1353__L1353_1349']] = 1
        A.append(rate_L6159_1353__L1353_1349)
        b.append(rates["L6159_1353__L1353_1349"])

        rate_L6159_1353__L1353_1352[x_index['L6159_1353__L1353_1352']] = 1
        A.append(rate_L6159_1353__L1353_1352)
        b.append(rates["L6159_1353__L1353_1352"])

        rate_L6159_6014__L6014_1353[x_index['L6159_6014__L6014_1353']] = 1
        A.append(rate_L6159_6014__L6014_1353)
        b.append(rates["L6159_6014__L6014_1353"])

        rate_L6159_6014__L6014_6013[x_index['L6159_6014__L6014_6013']] = 1
        A.append(rate_L6159_6014__L6014_6013)
        b.append(rates["L6159_6014__L6014_6013"])

        rate_outside__L1216_1352[x_index['L6159_6014__L6014_6013']] = 1
        A.append(rate_L6159_6014__L6014_6013)
        b.append(rates["outside__L1216_1352"])

        rate_outside__L1233_1352[x_index['outside__L1233_1352']] = 1
        A.append(rate_outside__L1233_1352)
        b.append(rates["outside__L1233_1352"])

        rate_outside__L3621_1867[x_index['outside__L3621_1867']] = 1
        A.append(rate_outside__L3621_1867)
        b.append(rates["outside__L3621_1867"])

        rate_outside__L5840_6013[x_index['outside__L5840_6013']] = 1
        A.append(rate_outside__L5840_6013)
        b.append(rates["outside__L5840_6013"])

        rate_outside__L6159_1353[x_index['outside__L5840_6013']] = 1
        A.append(rate_outside__L6159_1353)
        b.append(rates["outside__L6159_1353"])

        rate_outside__L6159_6014[x_index['outside__L5840_6013']] = 1
        A.append(rate_outside__L6159_6014)
        b.append(rates["outside__L6159_6014"])

        # Non-negative
        '''
        m.addConstr(L1202_3967_sink >= 0)
        m.addConstr(L6013_1202_L1202_3967 >= 0)
        m.addConstr(L1349_1202_L1202_3967 >= 0)
        '''
        # m.addConstr(L1202_1349__L1349_1867 >= 0)
        # m.addConstr(L1202_1349__L1349_3621 >= 0)
        # m.addConstr(L1202_3967__outside >= 0)
        # m.addConstr(L1202_6013__L6013_5840 >= 0)
        # m.addConstr(L1202_6013__L6013_6014 >= 0)
        # m.addConstr(L1216_1352__L1352_1867 >= 0)
        # m.addConstr(L1216_1352__outside >= 0)
        # m.addConstr(L1233_1352__L1352_1353 >= 0)
        # m.addConstr(L1233_1352__L1352_1867 >= 0)
        # m.addConstr(L1233_1352__outside >= 0)
        # m.addConstr(L1349_1202__L1202_3967 >= 0)
        # m.addConstr(L1349_1202__L1202_6013 >= 0)
        # m.addConstr(L1349_1353__L1353_1352 >= 0)
        # m.addConstr(L1349_1353__outside >= 0)
        # m.addConstr(L1349_1867__L1867_1352 >= 0)
        # m.addConstr(L1349_1867__L1867_4574 >= 0)
        # m.addConstr(L1349_3621__outside >= 0)
        # m.addConstr(L1352_1353__L1353_6014 >= 0)
        # m.addConstr(L1352_1353__L1353_6014 >= 0)
        # m.addConstr(L1352_1353__outside >= 0)
        # m.addConstr(L1352_1353__outside >= 0)
        # m.addConstr(L1352_1867__L1867_1349 >= 0)
        # m.addConstr(L1352_1867__L1867_3621 >= 0)
        # m.addConstr(L1352_1867__L1867_4574 >= 0)
        # m.addConstr(L1353_1349__L1349_1202 >= 0)
        # m.addConstr(L1353_1349__L1349_1867 >= 0)
        # m.addConstr(L1353_1349__L1349_3621 >= 0)
        # m.addConstr(L1353_1352__outside >= 0)
        # m.addConstr(L1353_1352__outside >= 0)
        # m.addConstr(L1353_6014__L6014_6013 >= 0)
        # m.addConstr(L1353_6014__outside >= 0)
        # m.addConstr(L1867_1349__L1349_1202 >= 0)
        # m.addConstr(L1867_1349__L1349_1353 >= 0)
        # m.addConstr(L1867_1349__L1349_3621 >= 0)
        # m.addConstr(L1867_1352__L1352_1353 >= 0)
        # m.addConstr(L1867_1352__outside >= 0)
        # m.addConstr(L1867_1352__outside >= 0)
        # m.addConstr(L1867_3621__outside >= 0)
        # m.addConstr(L1867_4574__outside >= 0)
        # m.addConstr(L3621_1349__L1349_1202 >= 0)
        # m.addConstr(L3621_1349__L1349_1353 >= 0)
        # m.addConstr(L3621_1867__L1867_1349 >= 0)
        # m.addConstr(L3621_1867__L1867_1352 >= 0)
        # m.addConstr(L3621_1867__L1867_4574 >= 0)
        # m.addConstr(L3966_1202__L1202_1349 >= 0)
        # m.addConstr(L3966_1202__L1202_6013 >= 0)
        # m.addConstr(L4574_1867__L1867_1349 >= 0)
        # m.addConstr(L4574_1867__L1867_1352 >= 0)
        # m.addConstr(L4574_1867__L1867_3621 >= 0)
        # m.addConstr(L5840_6013__L6013_1202 >= 0)
        # m.addConstr(L5840_6013__L6013_6014 >= 0)
        # m.addConstr(L6013_1202__L1202_1349 >= 0)
        # m.addConstr(L6013_1202__L1202_3967 >= 0)
        # m.addConstr(L6013_5840__outside >= 0)
        # m.addConstr(L6013_6014__L6014_1353 >= 0)
        # m.addConstr(L6013_6014__outside >= 0)
        # m.addConstr(L6014_1353__L1353_1349 >= 0)
        # m.addConstr(L6014_1353__L1353_1352 >= 0)
        # m.addConstr(L6014_6013__L6013_1202 >= 0)
        # m.addConstr(L6014_6013__L6013_5840 >= 0)
        # m.addConstr(L6159_1353__L1353_1349 >= 0)
        # m.addConstr(L6159_1353__L1353_1352 >= 0)
        # m.addConstr(L6159_6014__L6014_1353 >= 0)
        # m.addConstr(L6159_6014__L6014_6013 >= 0)
        # m.addConstr(outside__L1216_1352 >= 0)
        # m.addConstr(outside__L1233_1352 >= 0)
        # m.addConstr(outside__L3621_1867 >= 0)
        # m.addConstr(outside__L5840_6013 >= 0)
        # m.addConstr(outside__L6159_1353 >= 0)
        # m.addConstr(outside__L6159_6014 >= 0)


        ''''
        fij = m.addVar(vtype=GRB.CONTINUOUS, name="fij")
        fkj = m.addVar(vtype=GRB.CONTINUOUS, name="fkj")
        
        # Set objective
        m.setObjective(fij + fkj, GRB.MAXIMIZE)
        
        # Add constraint: x + 2 y + 3 z <= 4
        m.addConstr(fij + fkj <= 1, "c0")
        m.addConstr(fij >= 0, "c1")
        m.addConstr(fkj >= 0, "c2")
        m.addConstr(fij <= 1)
        m.addConstr(fkj <= 10)
        '''
        for _ in range(166):
            # m.Params.outputFlag = 0  # Suppress logging
            # m.optimize()
            result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
            #max_flow = {}
            #for v in m.getVars():
            #    max_flow[v.varName] = v.x
        print(time.clock()-start_time)
    # else:
    #     m = Model("transition")
    #
    #     # Edges into network
    #
    #     # Edges out of network
    #     '''
    #     L1202_3967_sink = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_3967_sink")
    #     '''
    #
    #     # All other edges
    #     '''
    #     L6013_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_1202__L1202_3967")
    #     L1349_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1202__L1202_3967")
    #     '''
    #     L1202_1349__L1349_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_1349__L1349_1867")
    #     L1202_1349__L1349_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_1349__L1349_3621")
    #     L1202_3967__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_3967__outside")
    #     L1202_6013__L6013_5840 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_6013__L6013_5840")
    #     L1202_6013__L6013_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_6013__L6013_6014")
    #     L1216_1352__L1352_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1216_1352__L1352_1867")
    #     L1216_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1216_1352__outside")
    #     L1233_1352__L1352_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L1233_1352__L1352_1353")
    #     L1233_1352__L1352_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1233_1352__L1352_1867")
    #     L1233_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1233_1352__outside")
    #     L1349_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1202__L1202_3967")
    #     L1349_1202__L1202_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1202__L1202_6013")
    #     L1349_1353__L1353_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1353__L1353_1352")
    #     L1349_1353__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1353__outside")
    #     L1349_1867__L1867_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1867__L1867_1352")
    #     L1349_1867__L1867_4574 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1867__L1867_4574")
    #     L1349_3621__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_3621__outside")
    #     L1352_1353__L1353_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__L1353_6014")
    #     L1352_1353__L1353_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__L1353_6014")
    #     L1352_1353__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__outside")
    #     L1352_1353__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__outside")
    #     L1352_1867__L1867_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1867__L1867_1349")
    #     L1352_1867__L1867_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1867__L1867_3621")
    #     L1352_1867__L1867_4574 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1867__L1867_4574")
    #     L1353_1349__L1349_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1349__L1349_1202")
    #     L1353_1349__L1349_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1349__L1349_1867")
    #     L1353_1349__L1349_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1349__L1349_3621")
    #     L1353_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1352__outside")
    #     L1353_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1352__outside")
    #     L1353_6014__L6014_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_6014__L6014_6013")
    #     L1353_6014__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_6014__outside")
    #     L1867_1349__L1349_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1349__L1349_1202")
    #     L1867_1349__L1349_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1349__L1349_1353")
    #     L1867_1349__L1349_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1349__L1349_3621")
    #     L1867_1352__L1352_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1352__L1352_1353")
    #     L1867_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1352__outside")
    #     L1867_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1352__outside")
    #     L1867_3621__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_3621__outside")
    #     L1867_4574__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_4574__outside")
    #     L3621_1349__L1349_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1349__L1349_1202")
    #     L3621_1349__L1349_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1349__L1349_1353")
    #     L3621_1867__L1867_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1867__L1867_1349")
    #     L3621_1867__L1867_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1867__L1867_1352")
    #     L3621_1867__L1867_4574 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1867__L1867_4574")
    #     L3966_1202__L1202_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L3966_1202__L1202_1349")
    #     L3966_1202__L1202_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L3966_1202__L1202_6013")
    #     L4574_1867__L1867_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L4574_1867__L1867_1349")
    #     L4574_1867__L1867_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L4574_1867__L1867_1352")
    #     L4574_1867__L1867_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L4574_1867__L1867_3621")
    #     L5840_6013__L6013_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L5840_6013__L6013_1202")
    #     L5840_6013__L6013_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L5840_6013__L6013_6014")
    #     L6013_1202__L1202_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_1202__L1202_1349")
    #     L6013_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_1202__L1202_3967")
    #     L6013_5840__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_5840__outside")
    #     L6013_6014__L6014_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_6014__L6014_1353")
    #     L6013_6014__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_6014__outside")
    #     L6014_1353__L1353_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_1353__L1353_1349")
    #     L6014_1353__L1353_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_1353__L1353_1352")
    #     L6014_6013__L6013_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_6013__L6013_1202")
    #     L6014_6013__L6013_5840 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_6013__L6013_5840")
    #     L6159_1353__L1353_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_1353__L1353_1349")
    #     L6159_1353__L1353_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_1353__L1353_1352")
    #     L6159_6014__L6014_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_6014__L6014_1353")
    #     L6159_6014__L6014_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_6014__L6014_6013")
    #     outside__L1216_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L1216_1352")
    #     outside__L1233_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L1233_1352")
    #     outside__L3621_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L3621_1867")
    #     outside__L5840_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L5840_6013")
    #     outside__L6159_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L6159_1353")
    #     outside__L6159_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L6159_6014")
    #
    #     '''
    #     m.setObjective(L1202_3967_sink
    #                    + L6013_1202_L1202_3967
    #                    + L1349_1202_L1202_3967
    #                    , GRB.MAXIMIZE)
    #     '''
    #     m.setObjective(L1202_1349__L1349_1867
    #                    + L1202_1349__L1349_3621
    #                    + L1202_3967__outside
    #                    + L1202_6013__L6013_5840
    #                    + L1202_6013__L6013_6014
    #                    + L1216_1352__L1352_1867
    #                    + L1216_1352__outside
    #                    + L1233_1352__L1352_1353
    #                    + L1233_1352__L1352_1867
    #                    + L1233_1352__outside
    #                    + L1349_1202__L1202_3967
    #                    + L1349_1202__L1202_6013
    #                    + L1349_1353__L1353_1352
    #                    + L1349_1353__outside
    #                    + L1349_1867__L1867_1352
    #                    + L1349_1867__L1867_4574
    #                    + L1349_3621__outside
    #                    + L1352_1353__L1353_6014
    #                    + L1352_1353__L1353_6014
    #                    + L1352_1353__outside
    #                    + L1352_1353__outside
    #                    + L1352_1867__L1867_1349
    #                    + L1352_1867__L1867_3621
    #                    + L1352_1867__L1867_4574
    #                    + L1353_1349__L1349_1202
    #                    + L1353_1349__L1349_1867
    #                    + L1353_1349__L1349_3621
    #                    + L1353_1352__outside
    #                    + L1353_1352__outside
    #                    + L1353_6014__L6014_6013
    #                    + L1353_6014__outside
    #                    + L1867_1349__L1349_1202
    #                    + L1867_1349__L1349_1353
    #                    + L1867_1349__L1349_3621
    #                    + L1867_1352__L1352_1353
    #                    + L1867_1352__outside
    #                    + L1867_1352__outside
    #                    + L1867_3621__outside
    #                    + L1867_4574__outside
    #                    + L3621_1349__L1349_1202
    #                    + L3621_1349__L1349_1353
    #                    + L3621_1867__L1867_1349
    #                    + L3621_1867__L1867_1352
    #                    + L3621_1867__L1867_4574
    #                    + L3966_1202__L1202_1349
    #                    + L3966_1202__L1202_6013
    #                    + L4574_1867__L1867_1349
    #                    + L4574_1867__L1867_1352
    #                    + L4574_1867__L1867_3621
    #                    + L5840_6013__L6013_1202
    #                    + L5840_6013__L6013_6014
    #                    + L6013_1202__L1202_1349
    #                    + L6013_1202__L1202_3967
    #                    + L6013_5840__outside
    #                    + L6013_6014__L6014_1353
    #                    + L6013_6014__outside
    #                    + L6014_1353__L1353_1349
    #                    + L6014_1353__L1353_1352
    #                    + L6014_6013__L6013_1202
    #                    + L6014_6013__L6013_5840
    #                    + L6159_1353__L1353_1349
    #                    + L6159_1353__L1353_1352
    #                    + L6159_6014__L6014_1353
    #                    + L6159_6014__L6014_6013
    #                    + outside__L1216_1352
    #                    + outside__L1233_1352
    #                    + outside__L3621_1867
    #                    + outside__L5840_6013
    #                    + outside__L6159_1353
    #                    + outside__L6159_6014
    #                    , GRB.MAXIMIZE)
    #
    #     # Maximum capacities
    #     '''
    #     m.addConstr(L6013_1202_L1202_3967
    #                 + L1349_1202_L1202_3967
    #                 - L1202_3967_sink
    #                 <= 20,
    #                 "cap_L1202_3967")
    #     '''
    #     m.addConstr(L6013_1202__L1202_1349
    #                 + L3966_1202__L1202_1349
    #                 - L1202_1349__L1349_1867
    #                 - L1202_1349__L1349_3621
    #                 + queues["L1202_1349"]
    #                 <= 88
    #                 , "L1202_1349")
    #     m.addConstr(L1202_1349__L1349_1867
    #                 + L1202_1349__L1349_3621
    #                 <= queues["L1202_1349"])
    #     m.addConstr(L6013_1202__L1202_3967
    #                 + L1349_1202__L1202_3967
    #                 - L1202_3967__outside
    #                 + queues["L1202_3967"]
    #                 <= 138
    #                 , "L1202_3967")
    #     m.addConstr(L1202_3967__outside
    #                 <= queues["L1202_3967"])
    #     m.addConstr(L1349_1202__L1202_6013
    #                 + L3966_1202__L1202_6013
    #                 - L1202_6013__L6013_5840
    #                 - L1202_6013__L6013_6014
    #                 + queues["L1202_6013"]
    #                 <= 61
    #                 , "L1202_6013")
    #     m.addConstr(L1202_6013__L6013_5840
    #                 + L1202_6013__L6013_6014
    #                 <= queues["L1202_6013"])
    #     m.addConstr(outside__L1216_1352
    #                 - L1216_1352__L1352_1867
    #                 - L1216_1352__outside
    #                 + queues["L1216_1352"]
    #                 <= 13
    #                 , "L1216_1352") # There may be a bug in the original model here.
    #     m.addConstr(L1216_1352__L1352_1867
    #                 + L1216_1352__outside
    #                 <= queues["L1216_1352"])
    #     m.addConstr(outside__L1233_1352
    #                 - L1233_1352__L1352_1353
    #                 - L1233_1352__L1352_1867
    #                 - L1233_1352__outside
    #                 + queues["L1233_1352"]
    #                 <= 30
    #                 , "L1233_1352") # Here too
    #     m.addConstr(L1233_1352__L1352_1353
    #                 + L1233_1352__L1352_1867
    #                 + L1233_1352__outside
    #                 <= queues["L1233_1352"])
    #     m.addConstr(L1353_1349__L1349_1202
    #                 + L3621_1349__L1349_1202
    #                 + L1867_1349__L1349_1202
    #                 - L1349_1202__L1202_3967
    #                 - L1349_1202__L1202_6013
    #                 + queues["L1349_1202"]
    #                 <= 89
    #                 , "L1349_1202")
    #     m.addConstr(L1349_1202__L1202_3967
    #                 + L1349_1202__L1202_6013
    #                 <= queues["L1349_1202"])
    #     m.addConstr(L3621_1349__L1349_1353
    #                 + L1867_1349__L1349_1353
    #                 - L1349_1353__L1353_1352
    #                 - L1349_1353__outside
    #                 + queues["L1349_1353"]
    #                 <= 78
    #                 , "L1349_1353")
    #     m.addConstr(L1349_1353__L1353_1352
    #                 + L1349_1353__outside
    #                 <= queues["L1349_1353"])
    #     m.addConstr(L1353_1349__L1349_1867
    #                 + L1202_1349__L1349_1867
    #                 - L1349_1867__L1867_1352
    #                 - L1349_1867__L1867_4574
    #                 + queues["L1349_1867"]
    #                 <= 63
    #                 , "L1349_1867")
    #     m.addConstr(L1349_1867__L1867_1352
    #                 + L1349_1867__L1867_4574
    #                 <= queues["L1349_1867"])
    #     m.addConstr(L1867_1349__L1349_3621
    #                 + L1202_1349__L1349_3621
    #                 + L1353_1349__L1349_3621
    #                 - L1349_3621__outside
    #                 + queues["L1349_3621"]
    #                 <= 181
    #                 , "L1349_3621")
    #     m.addConstr(L1349_3621__outside
    #                 <= queues["L1349_3621"])
    #     m.addConstr(L1867_1352__L1352_1353
    #                 + L1233_1352__L1352_1353
    #                 - L1352_1353__L1353_6014
    #                 - L1352_1353__outside
    #                 + queues["L1352_1353"]
    #                 <= 60
    #                 , "L1352_1353")
    #     m.addConstr(L1352_1353__L1353_6014
    #                 + L1352_1353__outside
    #                 <= queues["L1352_1353"])
    #     m.addConstr(L1216_1352__L1352_1867
    #                 + L1233_1352__L1352_1867
    #                 - L1352_1867__L1867_1349
    #                 - L1352_1867__L1867_3621
    #                 - L1352_1867__L1867_4574
    #                 + queues["L1352_1867"]
    #                 <= 73
    #                 , "L1352_1867")
    #     m.addConstr(L1352_1867__L1867_1349
    #                 + L1352_1867__L1867_3621
    #                 + L1352_1867__L1867_4574
    #                 <= queues["L1352_1867"])
    #     m.addConstr(L6159_1353__L1353_1349
    #                 + L6014_1353__L1353_1349
    #                 - L1353_1349__L1349_1202
    #                 - L1353_1349__L1349_1867
    #                 - L1353_1349__L1349_3621
    #                 + queues["L1353_1349"]
    #                 <= 88
    #                 , "L1353_1349")
    #     m.addConstr(L1353_1349__L1349_1202
    #                 + L1353_1349__L1349_1867
    #                 + L1353_1349__L1349_3621
    #                 <= queues["L1353_1349"])
    #     m.addConstr(L1349_1353__L1353_1352
    #                 + L6159_1353__L1353_1352
    #                 + L6014_1353__L1353_1352
    #                 - L1353_1352__outside
    #                 + queues["L1353_1352"]
    #                 <= 119
    #                 , "L1353_1352")  # And this one
    #     m.addConstr(L1353_1352__outside
    #                 <= queues["L1353_1352"])
    #     m.addConstr(L1352_1353__L1353_6014
    #                 + L1352_1353__L1353_6014
    #                 - L1353_6014__L6014_6013
    #                 - L1353_6014__outside
    #                 + queues["L1353_6014"]
    #                 <= 24
    #                 , "L1353_6014")
    #     m.addConstr(L1353_6014__L6014_6013
    #                 + L1353_6014__outside
    #                 <= queues["L1353_6014"])
    #     m.addConstr(L3621_1867__L1867_1349
    #                 + L1352_1867__L1867_1349
    #                 + L4574_1867__L1867_1349
    #                 - L1867_1349__L1349_1202
    #                 - L1867_1349__L1349_1353
    #                 - L1867_1349__L1349_3621
    #                 + queues["L1867_1349"]
    #                 <= 104
    #                 , "L1867_1349")
    #     m.addConstr(L1867_1349__L1349_1202
    #                 + L1867_1349__L1349_1353
    #                 + L1867_1349__L1349_3621
    #                 <= queues["L1867_1349"])
    #     m.addConstr(L4574_1867__L1867_1352
    #                 + L1349_1867__L1867_1352
    #                 + L3621_1867__L1867_1352
    #                 - L1867_1352__L1352_1353
    #                 - L1867_1352__outside
    #                 + queues["L1867_1352"]
    #                 <= 128
    #                 , "L1867_1352")
    #     m.addConstr(L1867_1352__L1352_1353
    #                 + L1867_1352__outside
    #                 <= queues["L1867_1352"])
    #     m.addConstr(L4574_1867__L1867_3621
    #                 + L1352_1867__L1867_3621
    #                 - L1867_3621__outside
    #                 + queues["L1867_3621"]
    #                 <= 19
    #                 , "L1867_3621")
    #     m.addConstr(L1867_3621__outside
    #                 <= queues["L1867_3621"])
    #     m.addConstr(L4574_1867__L1867_3621
    #                 + L1352_1867__L1867_3621
    #                 - L1867_3621__outside
    #                 + queues["L1867_3621"]
    #                 <= 62 # A bug? Weaker constraint than above
    #                 , "L1867_3621")
    #     m.addConstr(L1867_3621__outside
    #                 <= queues["L1867_3621"])
    #     m.addConstr(L1349_1867__L1867_4574
    #                 + L1352_1867__L1867_4574
    #                 + L3621_1867__L1867_4574
    #                 - L1867_4574__outside
    #                 + queues["L1867_4574"]
    #                 <=82
    #                 , "L1867_4574")
    #     m.addConstr(L1867_4574__outside
    #                 <= queues["L1867_4574"])
    #     #m.addConstr(- L3621_1349__L1349_1202
    #     #            - L3621_1349__L1349_1353
    #     #            #+ queues["L3621_1349"]  # Problem initially exceeds capacity
    #     #            <= 75
    #     #            , "L3621_1349") # This constraint is always true
    #     m.addConstr(L3621_1349__L1349_1202
    #                 + L3621_1349__L1349_1353
    #                 <= queues["L3621_1349"])
    #     m.addConstr(outside__L3621_1867
    #                 - L3621_1867__L1867_1349
    #                 - L3621_1867__L1867_1352
    #                 - L3621_1867__L1867_4574
    #                 + queues["L3621_1867"]
    #                 <=60
    #                 , "L3621_1867")
    #     m.addConstr(L3621_1867__L1867_1349
    #                 + L3621_1867__L1867_1352
    #                 + L3621_1867__L1867_4574
    #                 <= queues["L3621_1867"])
    #     #m.addConstr(- L3966_1202__L1202_1349
    #     #            - L3966_1202__L1202_6013
    #     #            #+ queues["L3966_1202"]  # Problem initially exceeds capacity
    #     #            <= 101 # Always true
    #     #            , "L3966_1202")
    #     m.addConstr(L3966_1202__L1202_1349
    #                 + L3966_1202__L1202_6013
    #                 <= queues["L3966_1202"])
    #     #m.addConstr(- L4574_1867__L1867_1349
    #     #            - L4574_1867__L1867_1352
    #     #            - L4574_1867__L1867_3621
    #     #            #+ queues["L4574_1867"]  # Problem initially exceeds capacity
    #     #            <= 179 # Always true
    #     #            , "L4574_1867")
    #     m.addConstr(L4574_1867__L1867_1349
    #                 + L4574_1867__L1867_1352
    #                 + L4574_1867__L1867_3621
    #                 <= queues["L4574_1867"])
    #     m.addConstr(outside__L5840_6013
    #                 - L5840_6013__L6013_1202
    #                 - L5840_6013__L6013_6014
    #                 + queues["L5840_6013"]
    #                 <= 40
    #                 , "L5840_6013")
    #     m.addConstr(L5840_6013__L6013_1202
    #                 + L5840_6013__L6013_6014
    #                 <= queues["L5840_6013"])
    #     m.addConstr(L5840_6013__L6013_1202
    #                 + L6014_6013__L6013_1202
    #                 - L6013_1202__L1202_1349
    #                 - L6013_1202__L1202_3967
    #                 + queues["L6013_1202"]
    #                 <=35
    #                 , "L6013_1202")
    #     m.addConstr(L6013_1202__L1202_1349
    #                 + L6013_1202__L1202_3967
    #                 <= queues["L6013_1202"])
    #     m.addConstr(L1202_6013__L6013_5840
    #                 + L6014_6013__L6013_5840
    #                 - L6013_5840__outside
    #                 + queues["L6013_5840"]
    #                 <= 24
    #                 , "L6013_5840")
    #     m.addConstr(L6013_5840__outside
    #                 <= queues["L6013_5840"])
    #     m.addConstr(L1202_6013__L6013_6014
    #                 + L5840_6013__L6013_6014
    #                 - L6013_6014__L6014_1353
    #                 - L6013_6014__outside
    #                 + queues["L6013_6014"]
    #                 <= 94
    #                 , "L6013_6014")
    #     m.addConstr(L6013_6014__L6014_1353
    #                 + L6013_6014__outside
    #                 <= queues["L6013_6014"])
    #     m.addConstr(L6013_6014__L6014_1353
    #                 + L6159_6014__L6014_1353
    #                 - L6014_1353__L1353_1349
    #                 - L6014_1353__L1353_1352
    #                 + queues["L6014_1353"]
    #                 <= 23
    #                 , "L6014_1353")
    #     m.addConstr(L6014_1353__L1353_1349
    #                 + L6014_1353__L1353_1352
    #                 <= queues["L6014_1353"])
    #     m.addConstr(L1353_6014__L6014_6013
    #                 + L6159_6014__L6014_6013
    #                 - L6014_6013__L6013_1202
    #                 - L6014_6013__L6013_5840
    #                 + queues["L6014_6013"]
    #                 <= 94
    #                 , "L6014_6013")
    #     m.addConstr(L6014_6013__L6013_1202
    #                 + L6014_6013__L6013_5840
    #                 <= queues["L6014_6013"])
    #     m.addConstr(outside__L6159_1353
    #                 - L6159_1353__L1353_1349
    #                 - L6159_1353__L1353_1352
    #                 + queues["L6159_1353"]
    #                 <= 24
    #                 , "L6159_1353")
    #     m.addConstr(L6159_1353__L1353_1349
    #                 + L6159_1353__L1353_1352
    #                 <= queues["L6159_1353"])
    #     m.addConstr(outside__L6159_6014
    #                 - L6159_6014__L6014_1353
    #                 - L6159_6014__L6014_6013
    #                 + queues["L6159_6014"]
    #                 <= 218
    #                 , "L6159_6014")
    #     m.addConstr(L6159_6014__L6014_1353
    #                 + L6159_6014__L6014_6013
    #                 <= queues["L6159_6014"])
    #
    #     # Maximum flow
    #     '''
    #     m.addConstr(L1202_3967_sink <= 0.49333 * t * flows["L1202_3967_sink"])
    #     m.addConstr(L6013_1202_L1202_3967 <= 0.41067 * t * flows["L6013_1202_L1202_3967"])
    #     m.addConstr(L1349_1202_L1202_3967 <= 0.825 * t * flows["L1349_1202_L1202_3967"])
    #     '''
    #     m.addConstr(L1202_1349__L1349_1867 <= rates["L1202_1349__L1349_1867"])
    #     m.addConstr(L1202_1349__L1349_3621 <= rates["L1202_1349__L1349_3621"])
    #     m.addConstr(L1202_3967__outside <= rates["L1202_3967__outside"])
    #     m.addConstr(L1202_6013__L6013_5840 <= rates["L1202_6013__L6013_5840"])
    #     m.addConstr(L1202_6013__L6013_6014 <= rates["L1202_6013__L6013_6014"])
    #     m.addConstr(L1216_1352__L1352_1867 <= rates["L1216_1352__L1352_1867"])
    #     m.addConstr(L1216_1352__outside <= rates["L1216_1352__outside"])
    #     m.addConstr(L1233_1352__L1352_1353 <= rates["L1233_1352__L1352_1353"])
    #     m.addConstr(L1233_1352__L1352_1867 <= rates["L1233_1352__L1352_1867"])
    #     m.addConstr(L1233_1352__outside <= rates["L1233_1352__outside"])
    #     m.addConstr(L1349_1202__L1202_3967 <= rates["L1349_1202__L1202_3967"])
    #     m.addConstr(L1349_1202__L1202_6013 <= rates["L1349_1202__L1202_6013"])
    #     m.addConstr(L1349_1353__L1353_1352 <= rates["L1349_1353__L1353_1352"])
    #     m.addConstr(L1349_1353__outside <= rates["L1349_1353__outside"])
    #     m.addConstr(L1349_1867__L1867_1352 <= rates["L1349_1867__L1867_1352"])
    #     m.addConstr(L1349_1867__L1867_4574 <= rates["L1349_1867__L1867_4574"])
    #     m.addConstr(L1349_3621__outside <= rates["L1349_3621__outside"])
    #     m.addConstr(L1352_1353__L1353_6014 <= rates["L1352_1353__L1353_6014"])
    #     m.addConstr(L1352_1353__L1353_6014 <= rates["L1352_1353__L1353_6014"])
    #     m.addConstr(L1352_1353__outside <= rates["L1352_1353__outside"])
    #     m.addConstr(L1352_1353__outside <= rates["L1352_1353__outside"])
    #     m.addConstr(L1352_1867__L1867_1349 <= rates["L1352_1867__L1867_1349"])
    #     m.addConstr(L1352_1867__L1867_3621 <= rates["L1352_1867__L1867_3621"])
    #     m.addConstr(L1352_1867__L1867_4574 <= rates["L1352_1867__L1867_4574"])
    #     m.addConstr(L1353_1349__L1349_1202 <= rates["L1353_1349__L1349_1202"])
    #     m.addConstr(L1353_1349__L1349_1867 <= rates["L1353_1349__L1349_1867"])
    #     m.addConstr(L1353_1349__L1349_3621 <= rates["L1353_1349__L1349_3621"])
    #     m.addConstr(L1353_1352__outside <= rates["L1353_1352__outside"])
    #     m.addConstr(L1353_1352__outside <= rates["L1353_1352__outside"])
    #     m.addConstr(L1353_6014__L6014_6013 <= rates["L1353_6014__L6014_6013"])
    #     m.addConstr(L1353_6014__outside <= rates["L1353_6014__outside"])
    #     m.addConstr(L1867_1349__L1349_1202 <= rates["L1867_1349__L1349_1202"])
    #     m.addConstr(L1867_1349__L1349_1353 <= rates["L1867_1349__L1349_1353"])
    #     m.addConstr(L1867_1349__L1349_3621 <= rates["L1867_1349__L1349_3621"])
    #     m.addConstr(L1867_1352__L1352_1353 <= rates["L1867_1352__L1352_1353"])
    #     m.addConstr(L1867_1352__outside <= rates["L1867_1352__outside"])
    #     m.addConstr(L1867_1352__outside <= rates["L1867_1352__outside"])
    #     m.addConstr(L1867_3621__outside <= rates["L1867_3621__outside"])
    #     m.addConstr(L1867_4574__outside <= rates["L1867_4574__outside"])
    #     m.addConstr(L3621_1349__L1349_1202 <= rates["L3621_1349__L1349_1202"])
    #     m.addConstr(L3621_1349__L1349_1353 <= rates["L3621_1349__L1349_1353"])
    #     m.addConstr(L3621_1867__L1867_1349 <= rates["L3621_1867__L1867_1349"])
    #     m.addConstr(L3621_1867__L1867_1352 <= rates["L3621_1867__L1867_1352"])
    #     m.addConstr(L3621_1867__L1867_4574 <= rates["L3621_1867__L1867_4574"])
    #     m.addConstr(L3966_1202__L1202_1349 <= rates["L3966_1202__L1202_1349"])
    #     m.addConstr(L3966_1202__L1202_6013 <= rates["L3966_1202__L1202_6013"])
    #     m.addConstr(L4574_1867__L1867_1349 <= rates["L4574_1867__L1867_1349"])
    #     m.addConstr(L4574_1867__L1867_1352 <= rates["L4574_1867__L1867_1352"])
    #     m.addConstr(L4574_1867__L1867_3621 <= rates["L4574_1867__L1867_3621"])
    #     m.addConstr(L5840_6013__L6013_1202 <= rates["L5840_6013__L6013_1202"])
    #     m.addConstr(L5840_6013__L6013_6014 <= rates["L5840_6013__L6013_6014"])
    #     m.addConstr(L6013_1202__L1202_1349 <= rates["L6013_1202__L1202_1349"])
    #     m.addConstr(L6013_1202__L1202_3967 <= rates["L6013_1202__L1202_3967"])
    #     m.addConstr(L6013_5840__outside <= rates["L6013_5840__outside"])
    #     m.addConstr(L6013_6014__L6014_1353 <= rates["L6013_6014__L6014_1353"])
    #     m.addConstr(L6013_6014__outside <= rates["L6013_6014__outside"])
    #     m.addConstr(L6014_1353__L1353_1349 <= rates["L6014_1353__L1353_1349"])
    #     m.addConstr(L6014_1353__L1353_1352 <= rates["L6014_1353__L1353_1352"])
    #     m.addConstr(L6014_6013__L6013_1202 <= rates["L6014_6013__L6013_1202"])
    #     m.addConstr(L6014_6013__L6013_5840 <= rates["L6014_6013__L6013_5840"])
    #     m.addConstr(L6159_1353__L1353_1349 <= rates["L6159_1353__L1353_1349"])
    #     m.addConstr(L6159_1353__L1353_1352 <= rates["L6159_1353__L1353_1352"])
    #     m.addConstr(L6159_6014__L6014_1353 <= rates["L6159_6014__L6014_1353"])
    #     m.addConstr(L6159_6014__L6014_6013 <= rates["L6159_6014__L6014_6013"])
    #     m.addConstr(outside__L1216_1352 <= rates["outside__L1216_1352"])
    #     m.addConstr(outside__L1233_1352 <= rates["outside__L1233_1352"])
    #     m.addConstr(outside__L3621_1867 <= rates["outside__L3621_1867"])
    #     m.addConstr(outside__L5840_6013 <= rates["outside__L5840_6013"])
    #     m.addConstr(outside__L6159_1353 <= rates["outside__L6159_1353"])
    #     m.addConstr(outside__L6159_6014 <= rates["outside__L6159_6014"])
    #
    #     # Non-negative
    #     '''
    #     m.addConstr(L1202_3967_sink >= 0)
    #     m.addConstr(L6013_1202_L1202_3967 >= 0)
    #     m.addConstr(L1349_1202_L1202_3967 >= 0)
    #     '''
    #     m.addConstr(L1202_1349__L1349_1867 >= 0)
    #     m.addConstr(L1202_1349__L1349_3621 >= 0)
    #     m.addConstr(L1202_3967__outside >= 0)
    #     m.addConstr(L1202_6013__L6013_5840 >= 0)
    #     m.addConstr(L1202_6013__L6013_6014 >= 0)
    #     m.addConstr(L1216_1352__L1352_1867 >= 0)
    #     m.addConstr(L1216_1352__outside >= 0)
    #     m.addConstr(L1233_1352__L1352_1353 >= 0)
    #     m.addConstr(L1233_1352__L1352_1867 >= 0)
    #     m.addConstr(L1233_1352__outside >= 0)
    #     m.addConstr(L1349_1202__L1202_3967 >= 0)
    #     m.addConstr(L1349_1202__L1202_6013 >= 0)
    #     m.addConstr(L1349_1353__L1353_1352 >= 0)
    #     m.addConstr(L1349_1353__outside >= 0)
    #     m.addConstr(L1349_1867__L1867_1352 >= 0)
    #     m.addConstr(L1349_1867__L1867_4574 >= 0)
    #     m.addConstr(L1349_3621__outside >= 0)
    #     m.addConstr(L1352_1353__L1353_6014 >= 0)
    #     m.addConstr(L1352_1353__L1353_6014 >= 0)
    #     m.addConstr(L1352_1353__outside >= 0)
    #     m.addConstr(L1352_1353__outside >= 0)
    #     m.addConstr(L1352_1867__L1867_1349 >= 0)
    #     m.addConstr(L1352_1867__L1867_3621 >= 0)
    #     m.addConstr(L1352_1867__L1867_4574 >= 0)
    #     m.addConstr(L1353_1349__L1349_1202 >= 0)
    #     m.addConstr(L1353_1349__L1349_1867 >= 0)
    #     m.addConstr(L1353_1349__L1349_3621 >= 0)
    #     m.addConstr(L1353_1352__outside >= 0)
    #     m.addConstr(L1353_1352__outside >= 0)
    #     m.addConstr(L1353_6014__L6014_6013 >= 0)
    #     m.addConstr(L1353_6014__outside >= 0)
    #     m.addConstr(L1867_1349__L1349_1202 >= 0)
    #     m.addConstr(L1867_1349__L1349_1353 >= 0)
    #     m.addConstr(L1867_1349__L1349_3621 >= 0)
    #     m.addConstr(L1867_1352__L1352_1353 >= 0)
    #     m.addConstr(L1867_1352__outside >= 0)
    #     m.addConstr(L1867_1352__outside >= 0)
    #     m.addConstr(L1867_3621__outside >= 0)
    #     m.addConstr(L1867_4574__outside >= 0)
    #     m.addConstr(L3621_1349__L1349_1202 >= 0)
    #     m.addConstr(L3621_1349__L1349_1353 >= 0)
    #     m.addConstr(L3621_1867__L1867_1349 >= 0)
    #     m.addConstr(L3621_1867__L1867_1352 >= 0)
    #     m.addConstr(L3621_1867__L1867_4574 >= 0)
    #     m.addConstr(L3966_1202__L1202_1349 >= 0)
    #     m.addConstr(L3966_1202__L1202_6013 >= 0)
    #     m.addConstr(L4574_1867__L1867_1349 >= 0)
    #     m.addConstr(L4574_1867__L1867_1352 >= 0)
    #     m.addConstr(L4574_1867__L1867_3621 >= 0)
    #     m.addConstr(L5840_6013__L6013_1202 >= 0)
    #     m.addConstr(L5840_6013__L6013_6014 >= 0)
    #     m.addConstr(L6013_1202__L1202_1349 >= 0)
    #     m.addConstr(L6013_1202__L1202_3967 >= 0)
    #     m.addConstr(L6013_5840__outside >= 0)
    #     m.addConstr(L6013_6014__L6014_1353 >= 0)
    #     m.addConstr(L6013_6014__outside >= 0)
    #     m.addConstr(L6014_1353__L1353_1349 >= 0)
    #     m.addConstr(L6014_1353__L1353_1352 >= 0)
    #     m.addConstr(L6014_6013__L6013_1202 >= 0)
    #     m.addConstr(L6014_6013__L6013_5840 >= 0)
    #     m.addConstr(L6159_1353__L1353_1349 >= 0)
    #     m.addConstr(L6159_1353__L1353_1352 >= 0)
    #     m.addConstr(L6159_6014__L6014_1353 >= 0)
    #     m.addConstr(L6159_6014__L6014_6013 >= 0)
    #     m.addConstr(outside__L1216_1352 >= 0)
    #     m.addConstr(outside__L1233_1352 >= 0)
    #     m.addConstr(outside__L3621_1867 >= 0)
    #     m.addConstr(outside__L5840_6013 >= 0)
    #     m.addConstr(outside__L6159_1353 >= 0)
    #     m.addConstr(outside__L6159_6014 >= 0)
    #
    #
    #     ''''
    #     fij = m.addVar(vtype=GRB.CONTINUOUS, name="fij")
    #     fkj = m.addVar(vtype=GRB.CONTINUOUS, name="fkj")
    #
    #     # Set objective
    #     m.setObjective(fij + fkj, GRB.MAXIMIZE)
    #
    #     # Add constraint: x + 2 y + 3 z <= 4
    #     m.addConstr(fij + fkj <= 1, "c0")
    #     m.addConstr(fij >= 0, "c1")
    #     m.addConstr(fkj >= 0, "c2")
    #     m.addConstr(fij <= 1)
    #     m.addConstr(fkj <= 10)
    #     '''
    #
    #     m.Params.outputFlag = 0  # Suppress logging
    #     m.optimize()
    #
    #     max_flow = {}
    #     for v in m.getVars():
    #         max_flow[v.varName] = v.x

    return max_flow

if __name__ == "__main__":
    import state

    current_queues, current_intersections, goal = state.init_problem(200, 152, 357)

