def do_something(n):
    for i in range(n):
        for x in range(i):
            continue

from multiprocessing.pool import ThreadPool as Pool

with Pool(5) as p:
    p.map(do_something, [
        2000,
        15000,
        10000,
        1000,
        12000
        ])
