# function for generating set of 2 word queries from a document
def twowordquery(d):
    tval = 5  # threshold value for the count to be above
    twowordq = []
    ind = 0
    counterd = Counter(d)
    while ind < len(d) - 1:
        w = d[ind]
        nw = d[ind + 1]
        if counterd[w] > tval and counterd[nw] > tval and len(w) > 1 and len(nw) > 1:
            # check if it is just punctuation len() > 1
            pair = [w, nw]
            twowordq.append(pair)
        ind = ind + 1
    return twowordq


# alternate version where check for nouns only
# use wordnet corpus
def twowordnounquery(d):
    from nltk.corpus import wordnet as wn
    nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
    tval = 5  # threshold value for the count to be above
    twowordq = []
    ind = 0
    counterd = Counter(d)
    while ind < len(d) - 1:
        w = d[ind]
        nw = d[ind + 1]
        if counterd[w] > tval and counterd[nw] > tval and len(w) > 1 and len(nw) > 1:
            # check if it is just punctuation len() > 1
            pair = [w, nw]
            if w in nouns and nw in nouns:
                twowordq.append(pair)
        ind = ind + 1
    return twowordq


def twowordquery(d):
    from nltk.corpus import wordnet as wn

    nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
    adj = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}
    verbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
    adverbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('r')}
    tval = 5  # threshold value for the count to be above
    twowordq = []
    ind = 0
    counterd = Counter(d)
    while ind < len(d) - 1:
        w = d[ind]
        nw = d[ind + 1]
        if counterd[w] > tval and counterd[nw] > tval and len(w) > 1 and len(nw) > 1:
            # check if it is just punctuation len() > 1
            pair = [w, nw]
            if w in nouns and nw in nouns:
                twowordq.append(pair)
            elif w in adj and nw in nouns:
                twowordq.append(pair)
            elif w in verbs and nw in adverbs:
                twowordq.append(pair)

        ind = ind + 1
    return twowordq


tw1 = twowordquery(news_text)

tw2 = twowordnounquery(news_text)