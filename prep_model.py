# load in the data and save as an text format for reading into R
from gensim.models import Word2Vec
import numpy as np

model = Word2Vec.load("./data/full.model")
vec = model.wv.vectors
terms = list(model.wv.vocab.keys())

np.savetxt("./temp_data/vectors.csv", vec, delimiter=",")
with open('./temp_data/terms.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % term for term in terms)


