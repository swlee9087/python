from titanic.model.dataset import Dataset
from titanic.model.service import Service
from dataclasses import dataclass
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Plot(object):
    dataset = Dataset()
    service = Service()

    def __init__(self):  # using Plot will auto create
        self.df = self.service.new_model('train.csv')  # object is dataframe in Service()

    def show_plot_survived_dead(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize=(18, 8))  # f=line, ax=col
        series = this['Survived'].value_counts()  # ret data will print in col type = df->series
        print(type(series))
        print(series)
        series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망 VS 1.생존')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망 VS 1.생존')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def show_plot_pclass(self):
        this = self.df
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['좌석등급'] = this['Pclass'].replace(1, '1등급').replace(2, '2등급').replace(3, '3등급')
        sns.countplot(data=this, x='좌석등급', hue='생존결과')
        plt.show()

    def show_plot_embarked(self):
        this = self.df
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['승선항구'] = this['Embarked'].replace('C', '쉘버그').replace('S', '사우스햄튼').replace('Q', '퀸즈타운')
        sns.countplot(data=this, x='승선항구', hue='생존결과')
        plt.show()

    def show_plot_sex(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        male_series = this['Survived'][this['Sex'] == 'male'].value_counts()
        female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
        male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('남성의 생존비율 0.사망 VS 1.생존')
        ax[0].set_ylabel('')
        ax[1].set_title('여성의 생존비율 0.사망 VS 1.생존')
        plt.show()
