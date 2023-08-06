# brim-cloud-client

BRIM Cloud Client is a minimal implementation of the REST interface used
to communicate with BRIM servers.

## Quick start

### Installation

```bash
pip install brim-cloud-client
```

### Usage - Solve a CNF file

```python
from BRIM import TMB


tmb_client = TMB(cm=0.9, cb=0.6, p='tmb', Rc=31000, C=49e-15, anneal=0.00011, seed=0)
tmb_client.print_neofetch() # print remote server information provided by neofetch
state, status, results = tmb_client.solve('../example/cust-u500-01.cnf')
print(state, status, results)

```
