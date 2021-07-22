import pandas as pd

from titanic2.model.dataset import Dataset


class Service(object):
    dataset = Dataset()

    def new_model(self, payload):
#        self.dataset.context = '../data/'
#        self.dataset.fname = payload
#        return pd.read_csv(self.dataset.context + self.dataset.fname)
#        줄여봤자 길어짐

        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
