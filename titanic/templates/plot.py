from titanic.model.dataset import Dataset
from titanic.model.service import Service
from dataclasses import dataclass
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Plot(object):
    dataset = Dataset()
    service = Service()

    def __init__(self):  # using Plot will auto create
        self.df = self.service.new_model('train.csv')  # object is dataframe in Service()

    def show_plot_survived_dead(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize=(18, 8))  #f=line, ax=col
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)  # ret data will print in col type
        ax[0].set_title('0.사망 VS 1.생존')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망 VS 1.생존')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()