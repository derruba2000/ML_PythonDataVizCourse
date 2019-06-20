import pandas as pd
import matplotlib.pyplot as plt

def RunExercise():
    print("Styling your plots")
    
    
    import pandas as pd
    reviews = pd.read_csv(r"C:\Data\Kaggle\DataSets\winemag-data_first150k.csv", index_col=0)
    reviews.head(3)
    
    reviews['points'].value_counts().sort_index().plot.bar(figsize=(12, 6))
    plt.show()
    
    
    
    reviews['points'].value_counts().sort_index().plot.bar(
        figsize=(12, 6),
        color='mediumvioletred'
    )
    plt.show()
    
    
    reviews['points'].value_counts().sort_index().plot.bar(
        figsize=(12, 6),
        color='mediumvioletred',
        fontsize=16,
        title='Rankings Given by Wine Magazine',
    )
    plt.show()
    
    
    ax = reviews['points'].value_counts().sort_index().plot.bar(
        figsize=(12, 6),
        color='mediumvioletred',
        fontsize=16
    )
    ax.set_title("Rankings Given by Wine Magazine", fontsize=20)
    plt.show()
    
    
    

    
        