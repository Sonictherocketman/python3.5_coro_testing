def do_something(d):
    fname, data = d
    with open(fname, 'w') as f:
        for line in data:
            f.write('%s\n' % line)

def do_something_else(n):
    for i in range(n[0]):
        for x in range(i):
            continue

def f(args):
    fn, args = args[0], args[1:]
    fn(args)

from multiprocessing import Pool

with Pool(5) as p:
    p.map(f, [
        (do_something_else, 2000),
        (do_something_else, 15000),
        (do_something, 'test3.dat', ['asdf'] * 1000000),
        (do_something, 'test4.dat', ['asdf'] * 100000),
        (do_something, 'test5.dat', ['asdf'] * 1200000)
        ])
