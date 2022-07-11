# Functions


#Takes in closing dates and closing price and creates a DataFrame with average daily returns
def sheets_returns_csvread_date(location_,column_,name_):

    # #Define path
    # ticker_data = Path(location_)
    
    # Reading whale returns and set index with column_ object
    ticker_df = pd.read_csv(location_, index_col=column_, infer_datetime_format=True, parse_dates=True)
    
    # Sort by Date
    ticker_df.sort_index(inplace=True)
    
    #Remove Null Columns
    ticker_df.drop(columns=ticker_df.columns[[0,2,3]], axis=1, inplace=True)
    
    #Rename Close Price Column
    ticker_df.rename(columns = {"Close":name_}, inplace = True)
    
    #Average Return
    # ticker_df = ticker_df.pct_change().copy()
    
    #Drop Nulls
    ticker_df.dropna(inplace=True)
    
    # x = df | Return DataFrame indexed by date_time
    return ticker_df



def csvread_date(location_,column_):
    import pandas as pd

    #Define path
    # ticker_data = Path(location_)
    
    # Reading whale returns and set index with column_ object
    ticker_df = pd.read_csv(location_, index_col=column_, infer_datetime_format=True, parse_dates=True)
    
    # Sort by Date
    ticker_df.sort_index(inplace=True)
    
    # x = df | Return DataFrame indexed by date_time
    return ticker_df