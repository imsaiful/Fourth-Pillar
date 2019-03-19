from feed.models import Republic, Ndtv, Indiatoday, Hindustan, Thehindu, Zeenews, IndexTop10
import nltk
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist
import numpy

hd = []

new_stop_words = ['says', 'khan', 'singh', "'s", "''",
                  'to', 'in', 'for', 'on', 'of', '``', 'and', 'the',
                  'a', 'after', '10', "n't", 'man', 'us', 'first', 'day', "'", '’', '‘', 'new', 'vs', 'india', 'top',
                  '...', 'life',
                  'gets', 'back', 'takes', 'rs', 'take'

                  ]


def getHeadLine(headline):
    global hd
    for title in headline:
        hd.append(title.headline)


def run():
    global hd
    hd = []
    republic_headline = Republic.objects.order_by('-date')[0:100]
    ndtv_headline = Ndtv.objects.order_by('-date')[0:100]
    hindstan_headline = Hindustan.objects.order_by('-date')[0:100]
    thehindu_headline = Thehindu.objects.order_by('-date')[0:100]
    zeenews_headline = Zeenews.objects.order_by('-date')[0:100]

    getHeadLine(republic_headline)
    getHeadLine(ndtv_headline)
    getHeadLine(hindstan_headline)
    getHeadLine(thehindu_headline)
    getHeadLine(zeenews_headline)

    def ie_preprocess(document):
        stop_words = stopwords.words('english')
        document = ' '.join([i for i in document.split("w", 4) if i not in stop_words])
        sentences = nltk.sent_tokenize(document)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        return sentences

    names = []
    names2 = []
    for x in hd:
        sentences = ie_preprocess(x)
        for tagged_sentence in sentences:
            # print(names)
            for chunk in nltk.ne_chunk(tagged_sentence):
                if type(chunk) == nltk.tree.Tree:
                    if chunk.label() == "PERSON":
                        names.append(' '.join([c[0] for c in chunk]))
    names_dic = dict({'Word': names})
    # names=str(names_dic.items())
    for x in hd:
        sentences = ie_preprocess(x)
        for tagged_sentence in sentences:
            # print(names)
            for chunk in nltk.ne_chunk(tagged_sentence):
                if type(chunk) == nltk.tree.Tree:
                    if chunk.label() != "PERSON":
                        names2.append(' '.join([c[0] for c in chunk]))
                    # di_data=dict()
    for n in names2:
        names.append(n)

    namefreq = [names.count(p) for p in names]
    d3 = dict(zip(names, namefreq))
    # print(d3)
    s = [(k, d3[k]) for k in sorted(d3, key=d3.get, reverse=True)]
    i = 0
    print("Top 10 searched words")
    x = []
    y = []
    while i <= 10:
        x.append(s[i][0])
        y.append(s[i][1])
        i += 1
    print(x)
    print(y)

    pk = 0
    for (word, frequency) in zip(x, y):
        update = IndexTop10(pk, db_keyword=word, db_frequency=frequency)
        update.save()
        pk = pk + 1
