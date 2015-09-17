def do_something(fname, data):
    with open(fname, 'w') as f:
        for line in data:
            f.write('%s\n' % line)

def do_something_else(n):
    for i in range(n):
        for x in range(i):
            continue

do_something_else(2000)
do_something_else(15000)
do_something('test3.dat', ['asdf'] * 1000000)
do_something('test4.dat', ['asdf'] * 100000)
do_something('test5.dat', ['asdf'] * 1200000)
