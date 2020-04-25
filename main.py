import numpy as np
from matplotlib import pyplot as plt
import sklearn.cluster
from scipy.cluster.hierarchy import dendrogram
from my_comparators import *
from my_tokenizer import *
from sklearn.cluster import AgglomerativeClustering


def jaro_inv(word1, word2):

    return 1 - jaro(word1, word2)

def jaro_winkler_inv(word1, word2):

    return 1 - jaro_winkler(word1, word2)

def plot_dendrogram(model, **kwargs):

    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    dendrogram(linkage_matrix, **kwargs)

DISTANCE_METRIC = jaro_inv
# hammington, jaro_inv, jaro_winkler_inv

text_file = open("source_text.txt", "r")
words = text_file.read()
words = get_words(words)

X = -1*np.array([[DISTANCE_METRIC(w1,w2) for w1 in words] for w2 in words])

model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
model = model.fit(X)

plot_dendrogram(model,leaf_label_func = lambda id: words[id], truncate_mode='level', leaf_font_size = 8)
plt.show()
