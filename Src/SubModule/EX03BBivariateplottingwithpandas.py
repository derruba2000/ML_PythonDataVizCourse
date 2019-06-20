import pandas as pd
import matplotlib.pyplot as plt

def RunExercise():
    print("Bivariate plotting with pandas")
    
    reviews = pd.read_csv(r"C:\Data\Kaggle\DataSets\winemag-data_first150k.csv", index_col=0)
    reviews.head()
    
    reviews[reviews['price'] < 100].sample(100).plot.scatter(x='price', y='points')
    plt.show()
    
    reviews[reviews['price'] < 100].plot.scatter(x='price', y='points')
    plt.show()
    
    reviews[reviews['price'] < 100].plot.hexbin(x='price', y='points', gridsize=15)
    plt.show()
    
    wine_counts = pd.read_csv(r"C:\Data\Kaggle\DataSets\top-five-wine-score-counts.csv", index_col=0)
    wine_counts.plot.bar(stacked=True)
    plt.show()
    
    wine_counts.plot.area()
    plt.show()
    wine_counts.plot.line()  
    plt.show()
                           
    