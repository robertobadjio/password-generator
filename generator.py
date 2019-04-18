import itertools
import random
import pymorphy2


def reservoir_sample(iterable, k, randrange=random.randrange, shuffle=random.shuffle):
    """Select *k* random elements from *iterable*.

    Use O(n) Algorithm R https://en.wikipedia.org/wiki/Reservoir_sampling
    """
    it = iter(iterable)
    sample = list(itertools.islice(it, k))  # fill the reservoir
    if len(sample) < k:
        raise ValueError("Sample larger than population")
    shuffle(sample)
    for i, item in enumerate(it, start=k + 1):
        j = randrange(i)  # random [0..i)
        if j < k:
            sample[j] = item  # replace item with gradually decreasing probability
    return sample


def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n") or x.endswith("\r"): return x[:-1]
    return x


with open('russian.txt') as f:
    list = (reservoir_sample(f, 4))

digit = random.randint(1, 99)

morph = pymorphy2.MorphAnalyzer()
word = morph.parse(chomp(list[0]))[0]

print(str(digit) + ' ' + word.make_agree_with_number(digit).word + ' ' + chomp(list[1]) + ' ' + chomp(list[2]) + ' ' + chomp(list[3]))
