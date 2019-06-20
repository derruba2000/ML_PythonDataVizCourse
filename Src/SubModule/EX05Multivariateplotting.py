import pandas as pd
import seaborn as sns
import re
import numpy as np
import matplotlib.pyplot as plt


def RunExercise():
    print("Multivariate Plotting")
    
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
    
    
    sns.lmplot(x='Value', y='Overall', hue='Position', 
           data=footballers.loc[footballers['Position'].isin(['ST', 'RW', 'LW'])], 
           fit_reg=False)
    
    plt.show()
    
    
    f = (footballers
         .loc[footballers['Position'].isin(['ST', 'GK'])]
         .loc[:, ['Value', 'Overall', 'Aggression', 'Position']]
    )
    f = f[f["Overall"] >= 80]
    f = f[f["Overall"] < 85]
    f['Aggression'] = f['Aggression'].astype(float)

    sns.boxplot(x="Overall", y="Aggression", hue='Position', data=f)
    plt.show()
    
    
    
    f = (
    footballers.loc[:, ['Acceleration', 'Aggression', 'Agility', 'Balance', 'Ball control']]
        .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan)
        .dropna()
    ).corr()

    sns.heatmap(f, annot=True)
    plt.show()
    

    f = (
    footballers.iloc[:, 12:17]
        .loc[footballers['Position'].isin(['ST', 'GK'])]
        .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan)
        .dropna()
    )
    f['Position'] = footballers['Position']
    f = f.sample(200)

    parallel_coordinates(f, 'Position')
    plt.show()
    
    