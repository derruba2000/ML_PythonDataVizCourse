import pandas as pd

def RunExercise():
    print("Univariate plotting with pandas")
    
 
    reviews = pd.read_csv(r"C:\Data\Kaggle\DataSets\winemag-data_first150k.csv", index_col=0)
    print(reviews.head(3))


    reviews['province'].value_counts().head(10).plot.bar()