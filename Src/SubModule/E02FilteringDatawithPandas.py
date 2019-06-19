import pandas as pd

def RunExercise():
    print("Filtering with Pandas")


    melbourne_file_path = r'C:\Data\Kaggle\DataSets\melb_data.csv'
    melbourne_data = pd.read_csv(melbourne_file_path) 
    print(melbourne_data.columns)
    
    melbourne_price_data = melbourne_data.Price
    # the head command returns the top few lines of data.
    print(melbourne_price_data.head())
    
    columns_of_interest = ['Landsize', 'BuildingArea']
    two_columns_of_data = melbourne_data[columns_of_interest]
    print(two_columns_of_data.describe())
    
    
    