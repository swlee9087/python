import pandas as pd

from titanic.model.dataset import Dataset


class Service(object):
    dataset = Dataset()  # constructorrrrr

    # @property
    # def dataset(self) -> Dataset: return self._dataset
    # @dataset.setter
    # def dataset(self, dataset): self._dataset = dataset
    def new_model(self, payload):
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
