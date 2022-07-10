# Functions


#Takes in closing dates and closing price and creates a DataFrame with average daily returns
def csvread_date(location_,column_):
    
    #Define path
    ticker_data = Path(location_)
    
    # Reading whale returns and set index with column_ object
    ticker_df = pd.read_csv(ticker_data, index_col=column_, infer_datetime_format=True, parse_dates=True)
    
    # Sort by Date
    ticker_df.sort_index(inplace=True)
    
    #Average Return
    ticker_df = ticker_df.pct_change().copy()
    
    #Drop Nulls
    ticker_df.dropna(inplace=True)
    
    # x = df | Return DataFrame indexed by date_time
    return ticker_df



def csvread_date(location_,column_):
    
    #Define path
    ticker_data = Path(location_)
    
    # Reading whale returns and set index with column_ object
    ticker_df = pd.read_csv(ticker_data, index_col=column_, infer_datetime_format=True, parse_dates=True)
    
    # Sort by Date
    ticker_df.sort_index(inplace=True)
    
    # x = df | Return DataFrame indexed by date_time
    return ticker_df