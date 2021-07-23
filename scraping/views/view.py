from scraping.models.dataset import Dataset
from scraping.models.service import Service


class View(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, bugs, melon):
        service = self.service
        this = self.preprocessing(bugs, melon)
        print(f'This is {type(this.bugs)}')  ###
        print(f'The Top 5 from Bugsmusic Chart are \n {this.bugs.head(5)}')
        print(f'The Top 5 from Melon Chart are \n {this.bugs.head(5)}')

    def preprocessing(self, bugs, melon) -> object:
        service = self.service
        this = self.dataset
        this.bugs = service.new_model(bugs)
        this.melon = service.new_model(melon)
        return this
