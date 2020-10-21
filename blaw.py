import collections

LAW_PERCENT = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

def blaw(data):

    """
    Implement Benford´s Law
    ref. https://en.wikipedia.org/wiki/Benford%27s_law
    @Author: Everaldo Lima
    """
    law = []
    digits = list(map(lambda d: str(d)[0], data))
    frequencies = collections.Counter(digits)

    for d in range(1, 10):
        frequency = frequencies[str(d)]
        percent = (frequency / len(data))*100
        vlaw = LAW_PERCENT[d]*100
        law.append({'d': d, 'p': percent, 'q': frequency,'law': vlaw})

    return law
