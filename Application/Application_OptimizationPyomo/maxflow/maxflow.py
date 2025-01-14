from pyomo.environ import *

model = AbstractModel()

# Nodes in the network
model.N = Set()
# Network arcs
model.A = Set(within=model.N*model.N)

# Source node
model.s = Param(within=model.N)
# Sink node
model.t = Param(within=model.N)
# Flow capacity limits
model.c = Param(model.A)

# The flow over each arc
model.f = Var(model.A, within=NonNegativeReals)

# Maximize the flow into the sink nodes
def total_rule(model):
    return sum(model.f[i,j] for (i, j) in model.A if j == value(model.t))
model.total = Objective(rule=total_rule, sense=maximize)

# Enforce an upper limit on the flow across each arc
def limit_rule(model, i, j):
    return model.f[i,j] <= model.c[i, j]
model.limit = Constraint(model.A, rule=limit_rule)

# Enforce flow through each node
def flow_rule(model, k):
    if k == value(model.s) or k == value(model.t):
        return Constraint.Skip
    inFlow  = sum(model.f[i,j] for (i,j) in model.A if j == k)
    outFlow = sum(model.f[i,j] for (i,j) in model.A if i == k)
    return inFlow == outFlow
model.flow = Constraint(model.N, rule=flow_rule)

instance = model.create_instance('maxflow.dat')
opt = SolverFactory("glpk")
results = opt.solve(instance)
results.write()

for i in instance.A.value:
    print("Flow on the branch {}: {}".format(i, value(instance.f[i])))