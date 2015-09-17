def do_something(d):
    fname, data = d
    with open(fname, 'w') as f:
        for line in data:
            f.write('%s\n' % line)

from multiprocessing import Pool

with Pool(5) as p:
    p.map(do_something, [
        ('test1.dat', ['asdf'] * 200000),
        ('test2.dat', ['asdf'] * 1500000),
        ('test3.dat', ['asdf'] * 1000000),
        ('test4.dat', ['asdf'] * 100000),
        ('test5.dat', ['asdf'] * 1200000)
        ])
