import threading

def worker(count):
    print "Este es el %s " % count
    return


t = threading.Thread(target=worker, args=("a"))
t.start()
b = threading.Thread(target=worker, args=("b"))
b.start()