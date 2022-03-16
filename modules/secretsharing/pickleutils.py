import bz2
import pickle
import _pickle as cPickle

def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w', compresslevel=9) as f: 
        cPickle.dump(data, f)

def decompress_pickle(file):
    data = bz2.BZ2File(file + '.pbz2', 'rb', compresslevel=9)
    data = cPickle.load(data)
    return data