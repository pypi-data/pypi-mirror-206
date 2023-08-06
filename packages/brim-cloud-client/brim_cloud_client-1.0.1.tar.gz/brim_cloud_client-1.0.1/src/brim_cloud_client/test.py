from BRIM import TMB
tmb_client = TMB(cm=0.9, cb=0.6, p='tmb', Rc=31000, C=49e-15, anneal=0.00011, seed=0)
tmb_client.set_remote_server('https://ord1.isingmodel.org/')
state, status, results = tmb_client.solve('../example/cust-u500-01.cnf')
print(state)
