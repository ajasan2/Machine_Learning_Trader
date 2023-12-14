import numpy as np
import random as random
from scipy.stats import mode

class BagLearner(object):
    def __init__(self, learner, kwargs={}, bags=20, boost=False, verbose=False):
        # Redacted class setup

    def author(self):
        return "ajasani9"

    def add_evidence(self, data_x, data_y):

        # Redacted bootstrap aggregation setup

        random_indices = [random.randint(0, len(data_x) - 1) for _ in range(len(data_x))]
        data_x_subset = data_x[random_indices]
        data_y_subset = data_y[random_indices]

        learner = self.learner(**self.kwargs)
        learner.add_evidence(data_x_subset, data_y_subset)


    def query(self, points):

        prediction_set = np.zeros((self.bags, len(points)))

        # Redacted query of bootstrap aggregation

        return mode(prediction_set, axis=0).mode[0]