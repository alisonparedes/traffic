if __name__ == "__main__":
    import sys
    print(sys.path)

    t = 100  # seconds
    flows = {}
    flows[("L1202_3967", "sink")] = 1
    flows[("L6013_1202", "L1202_3967")] = 1
    flows[("L1349_1202", "L1202_3967")] = 1

    from gurobipy import *
    m = Model("transition")


    '''
    # Edges into network

    # Edges out of network
    L1202_3967_sink = m.addVar(vtype=GRB.INTEGER, name="L1202_3967_sink")

    # All other edges
    L6013_1202_L1202_3967 = m.addVar(vtype=GRB.INTEGER, name="L6013_1202_L1202_3967")
    L1349_1202_L1202_3967 = m.addVar(vtype=GRB.INTEGER, name="L1349_1202_L1202_3967")

    m.setObjective(L1202_3967_sink
                   + L6013_1202_L1202_3967
                   + L1349_1202_L1202_3967
                   , GRB.MAXIMIZE)

    # Maximum capacities
    m.addConstr(L6013_1202_L1202_3967
                + L1349_1202_L1202_3967
                - L1202_3967_sink <= 20, "cap_L1202_3967")

    # Maximum flow
    m.addConstr(L1202_3967_sink <= 0.49333 * t * flows["L1202_3967_sink"])
    m.addConstr(L6013_1202_L1202_3967 <= 0.41067 * t * flows["L6013_1202_L1202_3967"])
    m.addConstr(L1349_1202_L1202_3967 <= 0.825 * t * flows["L1349_1202_L1202_3967"])

    # Non-negative
    m.addConstr(L1202_3967_sink >= 0)
    m.addConstr(L6013_1202_L1202_3967 >= 0)
    m.addConstr(L1349_1202_L1202_3967 >= 0)
    '''


    ''''
    fij = m.addVar(vtype=GRB.INTEGER, name="fij")
    fkj = m.addVar(vtype=GRB.INTEGER, name="fkj")

    # Set objective
    m.setObjective(fij + fkj, GRB.MAXIMIZE)

    # Add constraint: x + 2 y + 3 z <= 4
    m.addConstr(fij + fkj <= 1, "c0")
    m.addConstr(fij >= 0, "c1")
    m.addConstr(fkj >= 0, "c2")
    m.addConstr(fij <= 1)
    m.addConstr(fkj <= 10)
    '''


    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
    print('Obj: %g' % m.objVal)