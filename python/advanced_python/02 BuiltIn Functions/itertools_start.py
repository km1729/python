# advanced iteration functions in the itertools package
# https://docs.python.org/3/library/itertools.html

import itertools

def testFunction(x):
    if x < 50:
        return x


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # TODO: use count to create a simple counter
    count1 = itertools.count(2.5,0.5)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # TODO: accumulate creates an iterator that accumulates values
    print("#### accumulate: ")
    vals = [10,20,30,40,50,40,30]
    accumu = list(itertools.accumulate(vals))
    print(accumu)

    # TODO: use chain to connect sequences together
    print("#### chain: ")
    print(list(itertools.chain("ABCD","12345")))

    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops themprint(list(itertools.dropwhile(vals)))
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))



if __name__ == "__main__":
    main()
