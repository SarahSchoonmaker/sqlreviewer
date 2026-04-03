from sklearn.cluster import KMeans
import numpy as np

def cluster_queries(embeddings, k=5):
    model = KMeans(n_clusters=k)
    labels = model.fit_predict(np.array(embeddings))

    return labels