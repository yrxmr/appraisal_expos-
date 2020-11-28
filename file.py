from gensim.models import KeyedVectors
import spacy
import numpy as np


nlp = spacy.load("fr_core_news_md")
#on créée une liste avec des phrases types comme celles citées en exemple dans l'apparaisal theory
sentences = ['Un joli coucher de soleil', 'Un pull laid', 'Ce pull est bleu', 'Cette porte est noire', 'Il fait froid', 'Cette plume est légère', 'Cet exercise est dur' ]

#on a cherché les adjectifs les plus utilisés dans la langue française, et on a les a divisés en 3 listes d'une même longueur selon leur polarité
#positif, négatif ou bien neutre

pos_adj = ['beau', 'heureux', 'doux', 'gentil', 'meilleur', 'facile', 'vrai' ]
neg_adj = ['étrange', 'impossible', 'malade', 'sale', 'faux', 'désolé', 'difficile']
neutre_adj = ['jaune', 'petit', 'jeune', 'français', 'prochain', 'lourd', 'humain']
adj = []

#on cherche les tokens correspondant à des adjectifs dans les phrases types
for sentence in sentences:
    doc = nlp(sentence)
    for token in doc:
        if token.pos_ == 'ADJ':
            adj.append(token.text)



#on créé une fonction, où on spécifie comme argument la polarité que l'on veut tester pour chacun de ces adjectifs
def compare_vec(polarity_adj):
    #on obtient les vecteurs de similarité grâce à word2vec
    model = KeyedVectors.load_word2vec_format("frWac_no_postag_no_phrase_700_skip_cut50.bin", binary=True, unicode_errors="ignore")
    global similarity
    similarity= []
    #on compare chaque adjectif avec chacun des adjectifs de la polarité choisie
    for word in adj:
        for word1 in polarity_adj:
            pos_sim = model.similarity(word,word1)
            #les vecteurs sont récupérés sous format numpy, on les transforme donc de façon à pouvoir les utiliser
            for element in np.ndenumerate(pos_sim):
                x = np.char.replace(str(element), '()', '')
                x = np.char.replace(x, '(, ', '')
                x = np.char.replace(x, ')', '')
                similarity.append(str(x))

def average_pol():
    global sim
    sim = []
    #on transforme les vecteurs en objets float pour pouvoir les manipuler
    for item in similarity:

        sim.append(float(item))
    #on divise la liste de sorte à avoir une liste de listes, chaque sous-liste comprenant tous les vecteurs de comparaison par rapport à un seul adjectif
    lists = list(zip(*[iter(sim)]*(len(adj))))
    print(lists)
    global sums
    sums = []
    #on obtient chaque adjectif, et la moyenne de la somme des vecteurs de similarité s'y rapportant
    for i in range(0,len(lists)):
        print(adj[i])
        print(sum(lists[i]/len(lists)))
 
    
compare_vec(pos_adj)
average_pol()
