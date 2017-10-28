if __name__ == "__main__":
    import sys
    print(sys.path)
    from gurobipy import *
    m = Model("transition")
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

    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
    print('Obj: %g' % m.objVal)
