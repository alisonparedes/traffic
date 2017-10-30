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


def mccluskey_state():
    queues = mccluskey_queues()
    intersections = mccluskey_intersections()
    return queues, intersections


def mccluskey_actions():
    phases = mccluskey_phases()
    flows = mccluskey_flows()
    cycles = mccluskey_cycles()
    min_time, max_time, inter_time = mccluskey_times()
    return phases, flows, cycles, min_time, max_time, inter_time


def mccluskey_queues():
    queues = {}
    queues["L6013_1202"] = 0.0
    queues["L3966_1202"] = 300.0
    queues["L1202_3967"] = 11.0
    queues["L1202_6013"] = 8.0
    queues["L1349_3621"] = 0.0
    queues["L1867_1349"] = 59.0
    queues["L1353_1349"] = 0.0
    queues["L1349_1353"] = 0.0
    queues["L3621_1349"] = 152.0
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
    queues["L4574_1867"] = 357.0
    queues["L1867_4574"] = 5.0
    queues["L1233_1352"] = 16.0
    queues["L1216_1352"] = 10.0
    queues["L6159_1353"] = 0.0
    queues["L1349_1202"] = 10.0
    queues["L1202_1349"] = 10.0
    queues["outside"] = 0
    return queues


def mccluskey_flows():
    flows = {}
    flows["L1202_1349__L1349_1867"] = ("L1202_1349", "L1349_1867")
    flows["L1202_1349__L1349_3621"] = ("L1202_1349", "L1349_3621")
    flows["L1202_3967__outside"] = ("L1202_3967", "outside")
    flows["L1202_6013__L6013_5840"] = ("L1202_6013", "L6013_5840")
    flows["L1202_6013__L6013_6014"] = ("L1202_6013", "L6013_6014")
    flows["L1216_1352__L1352_1867"] = ("L1216_1352", "L1352_1867")
    flows["L1216_1352__outside"] = ("L1216_1352", "outside")
    flows["L1233_1352__L1352_1353"] = ("L1233_1352", "L1352_1353")
    flows["L1233_1352__L1352_1867"] = ("L1233_1352", "L1352_1867")
    flows["L1233_1352__outside"] = ("L1233_1352", "outside")
    flows["L1349_1202__L1202_3967"] = ("L1349_1202", "L1202_3967")
    flows["L1349_1202__L1202_6013"] = ("L1349_1202", "L1202_6013")
    flows["L1349_1353__L1353_1352"] = ("L1349_1353", "L1353_1352")
    flows["L1349_1353__outside"] = ("L1349_1353", "outside")
    flows["L1349_1867__L1867_1352"] = ("L1349_1867", "L1867_1352")
    flows["L1349_1867__L1867_4574"] = ("L1349_1867", "L1867_4574")
    flows["L1349_3621__outside"] = ("L1349_3621", "outside")
    flows["L1352_1353__L1353_6014"] = ("L1352_1353", "L1353_6014")
    flows["L1352_1353__L1353_6014"] = ("L1352_1353", "L1353_6014")
    flows["L1352_1353__outside"] = ("L1352_1353", "outside")
    flows["L1352_1353__outside"] = ("L1352_1353", "outside")
    flows["L1352_1867__L1867_1349"] = ("L1352_1867", "L1867_1349")
    flows["L1352_1867__L1867_3621"] = ("L1352_1867", "L1867_3621")
    flows["L1352_1867__L1867_4574"] = ("L1352_1867", "L1867_4574")
    flows["L1353_1349__L1349_1202"] = ("L1353_1349", "L1349_1202")
    flows["L1353_1349__L1349_1867"] = ("L1353_1349", "L1349_1867")
    flows["L1353_1349__L1349_3621"] = ("L1353_1349", "L1349_3621")
    flows["L1353_1352__outside"] = ("L1353_1352", "outside")
    flows["L1353_1352__outside"] = ("L1353_1352", "outside")
    flows["L1353_6014__L6014_6013"] = ("L1353_6014", "L6014_6013")
    flows["L1353_6014__outside"] = ("L1353_6014", "outside")
    flows["L1867_1349__L1349_1202"] = ("L1867_1349", "L1349_1202")
    flows["L1867_1349__L1349_1353"] = ("L1867_1349", "L1349_1353")
    flows["L1867_1349__L1349_3621"] = ("L1867_1349", "L1349_3621")
    flows["L1867_1352__L1352_1353"] = ("L1867_1352", "L1352_1353")
    flows["L1867_1352__outside"] = ("L1867_1352", "outside")
    flows["L1867_1352__outside"] = ("L1867_1352", "outside")
    flows["L1867_3621__outside"] = ("L1867_3621", "outside")
    flows["L1867_4574__outside"] = ("L1867_4574", "outside")
    flows["L3621_1349__L1349_1202"] = ("L3621_1349", "L1349_1202")
    flows["L3621_1349__L1349_1353"] = ("L3621_1349", "L1349_1353")
    flows["L3621_1867__L1867_1349"] = ("L3621_1867", "L1867_1349")
    flows["L3621_1867__L1867_1352"] = ("L3621_1867", "L1867_1352")
    flows["L3621_1867__L1867_4574"] = ("L3621_1867", "L1867_4574")
    flows["L3966_1202__L1202_1349"] = ("L3966_1202", "L1202_1349")
    flows["L3966_1202__L1202_6013"] = ("L3966_1202", "L1202_6013")
    flows["L4574_1867__L1867_1349"] = ("L4574_1867", "L1867_1349")
    flows["L4574_1867__L1867_1352"] = ("L4574_1867", "L1867_1352")
    flows["L4574_1867__L1867_3621"] = ("L4574_1867", "L1867_3621")
    flows["L5840_6013__L6013_1202"] = ("L5840_6013", "L6013_1202")
    flows["L5840_6013__L6013_6014"] = ("L5840_6013", "L6013_6014")
    flows["L6013_1202__L1202_1349"] = ("L6013_1202", "L1202_1349")
    flows["L6013_1202__L1202_3967"] = ("L6013_1202", "L1202_3967")
    flows["L6013_5840__outside"] = ("L6013_5840", "outside")
    flows["L6013_6014__L6014_1353"] = ("L6013_6014", "L6014_1353")
    flows["L6013_6014__outside"] = ("L6013_6014", "outside")
    flows["L6014_1353__L1353_1349"] = ("L6014_1353", "L1353_1349")
    flows["L6014_1353__L1353_1352"] = ("L6014_1353", "L1353_1352")
    flows["L6014_6013__L6013_1202"] = ("L6014_6013", "L6013_1202")
    flows["L6014_6013__L6013_5840"] = ("L6014_6013", "L6013_5840")
    flows["L6159_1353__L1353_1349"] = ("L6159_1353", "L1353_1349")
    flows["L6159_1353__L1353_1352"] = ("L6159_1353", "L1353_1352")
    flows["L6159_6014__L6014_1353"] = ("L6159_6014", "L6014_1353")
    flows["L6159_6014__L6014_6013"] = ("L6159_6014", "L6014_6013")
    flows["outside__L1216_1352"] = ("outside", "L1216_1352")
    flows["outside__L1233_1352"] = ("outside", "L1233_1352")
    flows["outside__L3621_1867"] = ("outside", "L3621_1867")
    flows["outside__L5840_6013"] = ("outside", "L5840_6013")
    flows["outside__L6159_1353"] = ("outside", "L6159_1353")
    flows["outside__L6159_6014"] = ("outside", "L6159_6014")
    return flows


def mccluskey_intersections(): #TODO: Model intergreen
    intersections = {}
    intersections["S1202"] = ("S1202_s0", 0)
    intersections["S1349"] = ("S1349_s0", 0)
    intersections["S1352"] = ("S1352_s0", 0)
    intersections["S1353"] = ("S1353_s0", 0)
    intersections["S1867"] = ("S1867_s0", 0)
    intersections["S6013"] = ("S6013_s0", 0)
    intersections["S6014"] = ("S6014_s0", 0)
    return intersections


def mccluskey_phases():
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
    if phases.get("fake"):
        phases["fake"].append(("L6013_5840__outside", 0.13833))
    else:
        phases["fake"] = [("L6013_5840__outside", 0.13833)]
    if phases.get("S6014_s0"):
        phases["S6014_s0"].append(("L6013_6014__outside", 0.31875))
    else:
        phases[" "] = [("L6013_6014__outside", 0.31875)]
    return phases


def mccluskey_cycles():
    cycles = {}
    cycles["S1202_s0"] = "S1202_s1"
    cycles["S1202_s1"] = "S1202_s2"
    cycles["S1202_s2"] = "S1202_s3"
    cycles["S1202_s3"] = "S1202_s4"
    cycles["S1202_s4"] = "S1202_s5"
    cycles["S1202_s5"] = "S1202_s6"
    cycles["S1202_s6"] = "S1202_s0"
    cycles["S1349_s0"] = "S1349_s1"
    cycles["S1349_s1"] = "S1349_s2"
    cycles["S1349_s2"] = "S1349_s3"
    cycles["S1349_s3"] = "S1349_s0"
    cycles["S6014_s0"] = "S6014_s1"
    cycles["S6014_s1"] = "S6014_s2"
    cycles["S6014_s2"] = "S6014_s3"
    cycles["S6014_s3"] = "S6014_s0"
    cycles["S6013_s0"] = "S6013_s1"
    cycles["S6013_s1"] = "S6013_s2"
    cycles["S6013_s2"] = "S6013_s0"
    cycles["S1353_s0"] = "S1353_s1"
    cycles["S1353_s1"] = "S1353_s2"
    cycles["S1353_s2"] = "S1353_s0"
    cycles["S1352_s0"] = "S1352_s1"
    cycles["S1352_s1"] = "S1352_s0"
    cycles["S1867_s0"] = "S1867_s1"
    cycles["S1867_s1"] = "S1867_s2"
    cycles["S1867_s2"] = "S1867_s0"
    return cycles


def mccluskey_times():
    min_time = dict()
    max_time = dict()
    inter_time = dict()
    inter_time["S1202_s0"] = 0
    inter_time["S1202_s1"] = 0
    inter_time["S1202_s2"] = 0
    inter_time["S1202_s3"] = 0
    inter_time["S1202_s4"] = 5
    inter_time["S1202_s5"] = 0
    inter_time["S1202_s6"] = 5
    min_time["S1202_s0"] = 5
    min_time["S1202_s1"] = 5
    min_time["S1202_s2"] = 0
    min_time["S1202_s3"] = 5
    min_time["S1202_s4"] = 5
    min_time["S1202_s5"] = 0
    min_time["S1202_s6"] = 5
    max_time["S1202_s0"] = 40
    max_time["S1202_s1"] = 20
    max_time["S1202_s2"] = 10
    max_time["S1202_s3"] = 60
    max_time["S1202_s4"] = 70
    max_time["S1202_s5"] = 15
    max_time["S1202_s6"] = 50
    inter_time["S1349_s0"] = 5
    inter_time["S1349_s1"] = 5
    inter_time["S1349_s2"] = 10
    inter_time["S1349_s3"] = 10
    min_time["S1349_s0"] = 5
    min_time["S1349_s1"] = 5
    min_time["S1349_s2"] = 5
    min_time["S1349_s3"] = 10
    max_time["S1349_s0"] = 70
    max_time["S1349_s1"] = 70
    max_time["S1349_s2"] = 70
    max_time["S1349_s3"] = 75
    inter_time["S6014_s0"] = 5
    inter_time["S6014_s1"] = 10
    inter_time["S6014_s2"] = 0
    inter_time["S6014_s3"] = 5
    min_time["S6014_s0"] = 5
    min_time["S6014_s1"] = 5
    min_time["S6014_s2"] = 10
    min_time["S6014_s3"] = 5
    max_time["S6014_s0"] = 50
    max_time["S6014_s1"] = 40
    max_time["S6014_s2"] = 50
    max_time["S6014_s3"] = 45
    inter_time["S6013_s0"] = 5
    inter_time["S6013_s1"] = 10
    inter_time["S6013_s2"] = 5
    min_time["S6013_s0"] = 5
    min_time["S6013_s1"] = 5
    min_time["S6013_s2"] = 5
    max_time["S6013_s0"] = 90
    max_time["S6013_s1"] = 95
    max_time["S6013_s2"] = 95
    inter_time["S1353_s0"] = 10
    inter_time["S1353_s1"] = 10
    inter_time["S1353_s2"] = 5
    min_time["S1353_s0"] = 5
    min_time["S1353_s1"] = 5
    min_time["S1353_s2"] = 5
    max_time["S1353_s0"] = 55
    max_time["S1353_s1"] = 50
    max_time["S1353_s2"] = 50
    inter_time["S1352_s0"] = 5
    inter_time["S1352_s1"] = 25
    min_time["S1352_s0"] = 5
    min_time["S1352_s1"] = 5
    max_time["S1352_s0"] = 55
    max_time["S1352_s1"] = 40
    inter_time["S1867_s0"] = 0
    inter_time["S1867_s1"] = 20
    inter_time["S1867_s2"] = 10
    min_time["S1867_s0"] = 5
    min_time["S1867_s1"] = 5
    min_time["S1867_s2"] = 5
    max_time["S1867_s0"] = 65
    max_time["S1867_s1"] = 60
    max_time["S1867_s2"] = 60
    return min_time, max_time, inter_time


def mccluskey_goal():
    goal = {}
    goal["L4574_1867"] = 50.0
    goal["L3966_1202"] = 50.0
    goal["L3621_1349"] = 50.0
    return goal

if __name__ == "__main__":
    pass