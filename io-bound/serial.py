def do_something(fname, data):
    with open(fname, 'w') as f:
        for line in data:
            f.write('%s\n' % line)

do_something('test1.dat', ['asdf'] * 200000)
do_something('test2.dat', ['asdf'] * 1500000)
do_something('test3.dat', ['asdf'] * 1000000)
do_something('test4.dat', ['asdf'] * 100000)
do_something('test5.dat', ['asdf'] * 1200000)
