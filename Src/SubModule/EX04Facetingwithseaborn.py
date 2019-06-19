import pandas as pd
import seaborn as sns
import re
import numpy as np
import matplotlib.pyplot as plt


def RunExercise():
    print("Faceting with seaborn")
    
    pd.set_option('max_columns', None)
    df = pd.read_csv(r"C:\Data\Kaggle\DataSets\CompleteDataset.csv", index_col=0)



    footballers = df.copy()
    footballers['Unit'] = df['Value'].str[-1]
    footballers['Value (M)'] = np.where(footballers['Unit'] == '0', 0, 
                                        footballers['Value'].str[1:-1].replace(r'[a-zA-Z]',''))
    footballers['Value (M)'] = footballers['Value (M)'].astype(float)
    footballers['Value (M)'] = np.where(footballers['Unit'] == 'M', 
                                        footballers['Value (M)'], 
                                        footballers['Value (M)']/1000)
    footballers = footballers.assign(Value=footballers['Value (M)'],
                                    Position=footballers['Preferred Positions'].str.split().str[0])

    
    plt.figure(figsize=(10,6))
    df = footballers[footballers['Position'].isin(['ST', 'GK'])]
    g = sns.FacetGrid(df, col="Position")
    g.map(sns.kdeplot, "Overall")
    plt.show()
    
    
    df = footballers
    g = sns.FacetGrid(df, col="Position", col_wrap=6)
    g.map(sns.kdeplot, "Overall")
    plt.show()
    
    
    df = footballers[footballers['Position'].isin(['ST', 'GK'])]
    df = df[df['Club'].isin(['Real Madrid CF', 'FC Barcelona', 'Atlético Madrid'])]

    g = sns.FacetGrid(df, row="Position", col="Club", 
                  row_order=['GK', 'ST'],
                  col_order=['Atlético Madrid', 'FC Barcelona', 'Real Madrid CF'])
    g.map(sns.violinplot, "Overall")
    plt.show()
    
    
    sns.pairplot(footballers[['Overall', 'Potential', 'Value']])
    plt.show()