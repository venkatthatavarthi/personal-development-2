import random

def split_data(data, prob):
    """split data into fractions [prob, 1 - prob] where prob is the fraction that will be saved for training"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append[row]
    return results

def train_test_split(x, y, test_pct):
    data = zip(x, y)                                    # pair corresponding values
    train, test = split_data(data, 1 - test_pct)        # split the data set of pairs
    x_train, y_train = zip(*train)                      # magical un-zip trick
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

# So you might do something like
# model = SomeKindOfModel()
# x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.33)
# model.train(x_train, y_train)
# performance = model.test(x_test, y_test)


def accuracy(tp, fp, fn, tn):
    """tp = true fpositive, fp = false positive, tn = true negative, fn = false negative"""
    correct = tp + tn
    total = tp + tn + fp +fn
    accuracy = correct / total
    return accuracy

def precision(tp, fp, fn, tn):
    """measures how accurate our positive predictions were"""
    precision = tp / (tp + fp)
    return precision

def recall(tp, fp, fn, tn):
    """measures what fraction of the positives our model identified"""
    recall = tp / (tp + fn)
    return recall

def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    f1_score = 2 * p * r / (p + r)
    return f1_score