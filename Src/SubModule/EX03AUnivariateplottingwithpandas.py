import pandas as pd
import matplotlib.pyplot as plt

def RunExercise():
    print("Univariate plotting with pandas")
    
 
    reviews = pd.read_csv(r"C:\Data\Kaggle\DataSets\winemag-data_first150k.csv", index_col=0)
    print(reviews.head(3))


    reviews['province'].value_counts().head(10).plot.bar()
    plt.show()
    
    
    (reviews['province'].value_counts().head(10) / len(reviews)).plot.bar()
    plt.show()
    
    
    # Bar plot
    reviews['points'].value_counts().sort_index().plot.bar()
    plt.show()
    
    # Line Plot
    reviews['points'].value_counts().sort_index().plot.line()
    plt.show()
    
    # Area Plot
    reviews['points'].value_counts().sort_index().plot.area()
    plt.show()
    
    
    # Histogram
    reviews[reviews['price'] < 200]['price'].plot.hist()
    plt.show()
    
    # Histogram 2
    reviews['points'].plot.hist()
    