import numpy as np
from scipy.stats import mode

def build_tree(data, leaf_size=1):
    if data.shape[0] <= leaf_size:
        return # Redacted aggregation method of combining values in leaf
    elif np.all(data[:,-1] == data[0, -1]):
        return np.array([[-1, data[0, -1], -1, -1]])
    else:

         # Redacted 2 edge case handlers

        split_feature = np.random.randint(data.shape[1] - 1)
        split_val = np.median(data[:, split_feature])

        left_tree = build_tree(data[data[:,split_feature] <= split_val], leaf_size)
        right_tree = build_tree(data[data[:,split_feature] > split_val], leaf_size)

        root = np.array([split_feature, split_val, 1, left_tree.shape[0] + 1])
        return np.vstack((root, left_tree, right_tree))


class RTLearner(object):
    def __init__(self, leaf_size=1, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.decision_tree = None

    def author(self):
        return "ajasani9"

    def add_evidence(self, data_x, data_y):

        data_block = np.column_stack((data_x, data_y))
        self.decision_tree = build_tree(data_block, self.leaf_size)
        if self.verbose:
            print("Train X (first 5)\n", data_x[:5], "\n")
            print("Train Y (first 5)\n", data_y[:5], "\n")
            print("Decision Tree\n", self.decision_tree, "\n")


    def query(self, points):

        dt = self.decision_tree
        predict = np.zeros(points.shape[0])

        for i, p in enumerate(points):
            ind = 0

             # Redactd part of query logic

            if p[feature] <= dt[ind][1]:
                ind += int(1)
            else:
                ind += int(dt[ind][3])

        if self.verbose:
            print("Query (first 5)\n", points[:5], "\n")
            print("Predicted (first 5)\n", predict[:5], "\n")

        return predict