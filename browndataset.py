# have a collection of documents to test
#just use text corpus - structured collection of texts

from nltk.corpus import brown
#for name in brown.fileids():
#    name.decode('utf-8')
# print(name)
news_text = brown.words(categories = 'news')

def str_tuple(t, encoding="ascii"):
    return tuple([i.encode(encoding) for i in t])
#news_text =
news_text = str_tuple(news_text)
ed_text = brown.words(categories = 'editorial')
ed_text = str_tuple(ed_text)
rev_text = brown.words(categories = 'reviews')
rev_text = str_tuple(rev_text)
hob_text = brown.words(categories='hobbies')
hob_text = str_tuple(hob_text)
lore_text = brown.words(categories ='lore')
lore_text = str_tuple(lore_text)
fic_text = brown.words(categories = 'fiction')
fic_text = str_tuple(fic_text)

adv_text = brown.words(categories='adventure')
adv_text = str_tuple(adv_text)

bel_text = brown.words(categories='belles_lettres')
bel_text = str_tuple(bel_text)

gov_text = brown.words(categories='government')
gov_text=str_tuple(gov_text)

learn_text = brown.words(categories='learned')
learn_text = str_tuple(learn_text)

rel_text = brown.words(categories= 'religion')
rel_text = str_tuple(rel_text)

rom_text = brown.words(categories = 'romance')
rom_text = str_tuple(rom_text)

scifi_text = brown.words(categories = 'science_fiction')
scifi_text = str_tuple(scifi_text)

collection1 = []
collection1.append(news_text)
collection1.append(ed_text)
collection1.append(rev_text)
collection1.append(hob_text)
collection1.append(lore_text)
collection1.append(fic_text)

collection1.append(adv_text)
collection1.append(bel_text)
collection1.append(gov_text)

collection1.append(learn_text)
collection1.append(rel_text)
collection1.append(rom_text)
collection1.append(scifi_text)



query1 = ['romance','county']
query2 = ['County','and']
query3= ['county']
doc1 = ['county','club','golf']
doc2 = ['county','golfing','running']
doc3 = ['play','bowling','sports']
collection2= []
collection2.append(doc1)
collection2.append(doc2)
collection2.append(doc3)