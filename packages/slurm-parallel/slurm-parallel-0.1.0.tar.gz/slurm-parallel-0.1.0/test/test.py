import logging

import sqlalchemy as sa
import dfdb
import hyclib as lib

import slurm_parallel as sp

lib.logging.basic_config()
logger = logging.getLogger()
logger.setLevel('DEBUG')

db = dfdb.Database(database='test/data/test.db')

@sp.parallelize(database=db, table='results', columns='result', mem_per_cpu='1gb', c=1)
def func(a, b):
    return a + b

def main():
    if 'results' in db:
        del db['results']
        
    db['results'] = dfdb.TableDef(
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('a', sa.Integer()),
        sa.Column('b', sa.Integer()),
        sa.Column('result', sa.Integer()),
        sa.Column('created', sa.DateTime(), server_default=sa.func.now()),
    )
    
    configs = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 4},
        {'a': 5, 'b': 6},
        {'a': 7, 'b': 8},
    ]
    job = func.remote(configs, wait=True, max_n_tasks=3)
    
    print(db['results'].fetch())

if __name__ == '__main__':
    main()