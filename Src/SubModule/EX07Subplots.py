import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def RunExercise():
    print("Subplots")
    
    
    
    reviews = pd.read_csv(r"C:\Data\Kaggle\DataSets\winemag-data_first150k.csv", index_col=0)
    
    fig, axarr = plt.subplots(2, 1, figsize=(12, 8))
    plt.show()
    
    
    fig, axarr = plt.subplots(2, 1, figsize=(12, 8))

    reviews['points'].value_counts().sort_index().plot.bar(
        ax=axarr[0]
    )

    reviews['province'].value_counts().head(20).plot.bar(
        ax=axarr[1]
    )
    plt.show()
    
    
    fig, axarr = plt.subplots(2, 2, figsize=(12, 8))

    reviews['points'].value_counts().sort_index().plot.bar(
        ax=axarr[0][0], fontsize=12, color='mediumvioletred'
    )
    axarr[0][0].set_title("Wine Scores", fontsize=18)

    reviews['variety'].value_counts().head(20).plot.bar(
        ax=axarr[1][0], fontsize=12, color='mediumvioletred'
    )
    axarr[1][0].set_title("Wine Varieties", fontsize=18)

    reviews['province'].value_counts().head(20).plot.bar(
        ax=axarr[1][1], fontsize=12, color='mediumvioletred'
    )
    axarr[1][1].set_title("Wine Origins", fontsize=18)

    reviews['price'].value_counts().plot.hist(
        ax=axarr[0][1], fontsize=12, color='mediumvioletred'
    )
    axarr[0][1].set_title("Wine Prices", fontsize=18)

    plt.subplots_adjust(hspace=.3)

   
    sns.despine()
    plt.show()
    