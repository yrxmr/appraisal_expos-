from gensim.models import KeyedVectors
import spacy
import numpy as np

nlp = spacy.load("fr_core_news_md")
sentences = ['Un joli coucher de soleil', 'Un pull laid', 'Ce pull est bleu', 'Cette porte est noire', 'Il fait froid', 'Cette plume est légère', 'Cet exercise est dur' ]
pos_adj = ['beau', 'heureux', 'doux', 'gentil', 'meilleur', 'facile', 'vrai' ]
neg_adj = ['étrange', 'impossible', 'malade', 'sale', 'faux', 'désolé', 'difficile']
neutre_adj = ['jaune', 'petit', 'jeune', 'français', 'prochain', 'lourd', 'humain']
adj = []
for sentence in sentences:
    doc = nlp(sentence)
    for token in doc:
        if token.pos_ == 'ADJ':
            adj.append(token.text)




def compare_vec(polarity_adj):
    model = KeyedVectors.load_word2vec_format("frWac_no_postag_no_phrase_700_skip_cut50.bin", binary=True, unicode_errors="ignore")
    global similarity
    similarity= []
    for word in adj:
        for word1 in polarity_adj:
            pos_sim = model.similarity(word,word1)
            for element in np.ndenumerate(pos_sim):
                x = np.char.replace(str(element), '()', '')
                x = np.char.replace(x, '(, ', '')
                x = np.char.replace(x, ')', '')
                similarity.append(str(x))

def average_pol():
    global sim
    sim = []
    for item in similarity:

        sim.append(float(item))
    lists = list(zip(*[iter(sim)]*(len(adj))))
    print(lists)
    global sums
    sums = []
    for i in range(0,len(lists)):
        print(adj[i])
        print(sum(lists[i]))
 
    
compare_vec(pos_adj)
average_pol()
