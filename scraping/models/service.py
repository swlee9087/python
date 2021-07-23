import pandas as pd

from scraping.models.dataset import Dataset


class Service(object):
    dataset = Dataset()

    def new_model(self,payload):
        this=self.dataset
        this.context = ''  ########
        this.fname=payload
        return pd.read_csv(this.context + this.fname)