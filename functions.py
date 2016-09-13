
def print_name(*names):
    for name in names:
        print "hi %s " % name



def f():
    global s # if removed it shows error
    print s
    s=67
    print s

s=7
f()