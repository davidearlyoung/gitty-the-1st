import timeit

def timeTest():
    for i in range(1000):
        print(i)

print(timeit.timeit('timeTest()', setup='from __main__ import timeTest', number=20))
