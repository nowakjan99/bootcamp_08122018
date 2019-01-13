import time

start = time.time()
lista = [x*2 for x in range(1000000)]
stop = time.time()

print(stop-start)

def baz():
    pass

def foo(bar):
    print(bar.__name__)

foo(print)