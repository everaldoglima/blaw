import collections

LAW_PERCENT = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

def blaw(data):

    """
    Implement Benford´s Law
    ref. https://en.wikipedia.org/wiki/Benford%27s_law
    """
    law = []
    digits = list(map(lambda n: str(n)[0], data))
    frequencies = collections.Counter(digits)

    for n in range(1, 10):
        frequency = frequencies[str(n)]
        percent = (frequency / len(data))
        vlaw = (LAW_PERCENT[n] == percent)
        law.append({'n': n, '%': (percent*100), 'valid': vlaw})

    return law
