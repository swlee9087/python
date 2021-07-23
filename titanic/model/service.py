import pandas as pd

from titanic.model.dataset import Dataset


# 2

class Service(object):
    dataset = Dataset()  # constructorrrrr

    def new_model(self, payload: str) -> object:
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


def create_train(this):
    return this

def create_label(this):
    return this

def drop_feature(this, *feature):
    return this

def embarked_nominal(this):  # QSC
    return this

def fare_ordinal(this):  # paid or not
    return this

def title_nominal(this):  # mr mrs miss master ms
    return this

def gender_nominal(this):  # mf
    return this

def age_ordinal(this):  #
    return this

def create_k_fold():  #
    return None

def accuracy_by_classifier():  #
    return ""

