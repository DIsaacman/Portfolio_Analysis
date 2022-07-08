# How To Pull Data With Google Sheets

## Get Assets/Securities in Date Range


 ### Use Google Sheets to easily get price data
- Make Copy
- Insert Date and Ticker
- Export to .CSV 
- Use Python and PANDAS for Portfolio Analysis and Backtesting. 


#### Syntax




Markup :  `GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date|num_days], [interval])`



### Examples


Gather Data for for Stocks - AMD (Advanced Micro Devices)

```

=GOOGLEFINANCE("AMD","Price","5/9/2019",Today())

```

Gather Data for Currency Pairs - US Dollar and European Euro 

```

=GOOGLEFINANCE("CURRENCY:USDEUR","Price","5/9/2019",Today())

```
## ***Note***: For best result, use reference cells in G-Sheets to easily gather information:


![Google_Sheets_Data](Google_Sheets_Data.png)


[^1]: Here is [an example](https://docs.google.com/spreadsheets/d/1o_s3W20il3u-62fEhyoIMQFb3eignFwtVCyPga1fBwI/edit?usp=sharing) of the google sheet for reference. Make your own copy, download as CSV and start analysing now!