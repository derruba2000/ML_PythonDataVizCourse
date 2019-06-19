    
import pandas as pd

def RunExercise():
    print("Accessing Data with Pandas")

    print("3 Rows")
    df = pd.read_csv(r'C:\Data\Kaggle\DataSets\parks.csv', index_col=['Park Code'])
    print(df.head(3))


    print("3 rows from 1 record")
    print(df.iloc[2])

    print("using index for BADL")
    print(df.loc['BADL'])

    print("Just three rows, index order")
    print(df.loc[['BADL', 'ARCH', 'ACAD']])


    print("Just three rows, index number order")
    print(df.iloc[[2, 1, 0]])


    print("Slicing data 1")
    print(df[:3])
    
    print("Slicing data 2")
    print(df[3:6])


    # Columns ##################################################
    print("Indexing Columns -> State ex01")
    print(df['State'].head(3))

    print("Indexing Columns -> State ex02")
    print(df.State.head(3))

    print("Indexing Columns -> Reviewing column names")
    df.columns = [col.replace(' ', '_').lower() for col in df.columns]
    print(df.columns)

    print("Indexing: Columns and Rows")
    print(df[['state', 'acres']][:3])

    print("Indexing: Scalar Values")
    print(df.state.iloc[2])

    print(df.state.iloc[[2]])

    print("Selecting a Subset of the Data")
    print((df.state == 'UT').head(3))

    print(df[df.state == 'UT'])

    print("Several conditioning filtering")
    print(df[(df.latitude > 60) | (df.acres > 10**6)].head(3))


    print("Lambdas expression")
    print(df[df['park_name'].str.split().apply(lambda x: len(x) == 3)].head(3))

    print("Is in operator")
    print(df[df.state.isin(['WA', 'OR', 'CA'])].head())
    
