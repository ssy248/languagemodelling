from nltk.probability import FreqDist
from math import log

from collections import Counter

# query
q = ['the', 'car']


# p(t | d) = prod_{t \in q} M_d (t)^q_t
def probabilityrankingmodel(q, t, d):
    prob = 1
    for w in q:
        prob = prob * Mfunction(d, t, q)
    return prob


def Mfunction(d, t, q):
    # q_t equals number of times t is in q
    c = Counter(q)
    qt = c[t]
    d = Counter(d)
    freq = FreqDist(d)
    return (freq[t] / d[t]) ^ qt


def sumwordcount(d):
    return sum(d[w] for w in d)


def totalcollectionwordcount(collection):
    s = 0
    for d in collection:
        s = s + len(d)
    return s


def totaltermcount(collection, t):
    s = 0
    for d in collection:
        freq = FreqDist(d)
        s = s + freq[t]
    return s


# language modeling with Jelinek-Mercer smoothing
def LMJM(q, d, lam, collection):
    num_words = len(d)
    tnum_words = totalcollectionwordcount(collection)
    print('totalcollectionwordcount', tnum_words)
    r = 0
    freq = FreqDist(d)
    counterd = Counter(d)
    for t in q:
        tt = totaltermcount(collection, t)
        # print('freq/numwrods',freq[t]/float(num_words))
        # print('counterd/nwords', counterd[t])
        # print('tnumwords/tt', tnum_words/tt)
        r = r + log(1 + ((1 - lam) / float(lam))) * (freq[t] / float(num_words)) * (tnum_words / float(tt))
    return r


from math import pow


# for research dev purposes
# alternative measure of statistical distance between distributions
def chisquareLM(q, d, collection):
    num_words = len(d)
    n = len(q)
    r = 0
    counterq = Counter(q)
    freq = FreqDist(d)
    for t in q:
        qt = counterq[t]  # count times t appears in query
        r = r + n * pow(freq[t] / float(num_words) - qt / float(n), 2) / qt
    return r


# hellinger coefficient
def hellingercoeff(q, d, collection):
    num_words = len(d)
    n = len(q)
    r = 0
    counterq = Counter(q)
    freq = FreqDist(d)
    for t in q:
        qt = counterq[t]  # count times t appears in query
        # p = freq[t]/float(num_words) q = qt/n
        r = r + pow(freq[t] / float(num_words) * qt / float(n), 0.5)
    return r


def hellingerdist(q, d, collection):
    num_words = len(d)
    n = len(q)
    r = 0
    counterq = Counter(q)
    freq = FreqDist(d)
    for t in q:
        qt = counterq[t]  # count times t appears in query
        # p = freq[t]/float(num_words) q = qt/n
        r = r + pow(freq[t] / float(num_words) * qt / float(n), 0.5)
    return math.sqrt(2 - 2 * r)


def chernoffcoeff(q, d, collection, alpha):
    num_words = len(d)
    n = len(q)
    r = 0
    counterq = Counter(q)
    freq = FreqDist(d)
    for t in q:
        qt = counterq[t]  # count times t appears in query
        # p = freq[t]/float(num_words) q = qt/n
        r = r + pow(freq[t] / float(num_words), alpha) * pow(qt / float(n), 1 - alpha)
    return r


def jeffreysdist(q, d, collection):
    num_words = len(d)
    n = len(q)
    r = 0
    counterq = Counter(q)
    freq = FreqDist(d)
    for t in q:
        qt = counterq[t]  # count times t appears in query
        # p = freq[t]/float(num_words) q = qt/n
        r = r + pow(pow(freq[t] / float(num_words), 0.5) - pow(qt / float(n), 0.5), 2)
    return r


# directed divergence

def DirectedDivergence(q, d, lam, collection):
    num_words = len(d)
    n = len(q)
    tnum_words = totalcollectionwordcount(collection)
    print('totalcollectionwordcount', tnum_words)
    r = 0
    freq = FreqDist(d)
    counterd = Counter(d)
    counterq = Counter(q)
    for t in q:
        qt = counterq[t]
        tt = totaltermcount(collection, t)
        # print('freq/numwrods',freq[t]/float(num_words))
        # print('counterd/nwords', counterd[t])
        # print('tnumwords/tt', tnum_words/tt)
        r = r + freq[t] / float(num_words) * log((freq[t] / float(num_words)) * n / float(qt))
    return r


# symmetric directed divergence
def SymmDirectedDivergence(q, d, collection):
    num_words = len(d)
    n = len(q)
    tnum_words = totalcollectionwordcount(collection)
    print('totalcollectionwordcount', tnum_words)
    r = 0
    freq = FreqDist(d)
    counterd = Counter(d)
    counterq = Counter(q)
    for t in q:
        qt = counterq[t]
        tt = totaltermcount(collection, t)
        r = r + (freq[t] / float(num_words) - qt / float(n)) * log((freq[t] / float(num_words)) * n / float(qt))
    return r


# symmetric directed divergence  with lambda
def SymmDirectedDivergenceLambda(q, d, lam, collection):
    num_words = len(d)
    n = len(q)
    tnum_words = totalcollectionwordcount(collection)
    print('totalcollectionwordcount', tnum_words)
    r = 0
    freq = FreqDist(d)
    counterd = Counter(d)
    counterq = Counter(q)
    for t in q:
        qt = counterq[t]
        tt = totaltermcount(collection, t)
        r = r + (freq[t] / float(num_words) - qt / float(n)) * log(
            1 + ((1 - lam) / lam) * (freq[t] / float(num_words)) * n / float(qt))
    return r

# generalized KL divergence

