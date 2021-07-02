import pandas
import yfinance as yf
from iexfinance.stocks import Stock


def get_tickers():
    return ['MMM','ABT','ABBV','ABMD','ACN','ATVI','ADBE','AMD','AAP','AES','AFL','A','APD','AKAM','ALK','ALB','ARE','ALXN','ALGN','ALLE','LNT','ALL','GOOGL','GOOG','MO','AMZN','AMCR','AEE','AAL','AEP','AXP','AIG','AMT','AWK','AMP','ABC','AME','AMGN','APH','ADI','ANSS','ANTM','AON','AOS','APA','AIV','AAPL','AMAT','APTV','ADM','ANET','AJG','AIZ','T','ATO','ADSK','ADP','AZO','AVB','AVY','BKR','BLL','BAC','BK','BAX','BDX','BBY','BIO','BIIB','BLK','BA','BKNG','BWA','BXP','BMY','AVGO','BR','CHRW','COG','CDNS','CPB','COF','CAH','KMX','CCL','CARR','CTLT','CAT','CBOE','CBRE','CDW','CE','CNC','CNP','CERN','CF','SCHW','CHTR','CVX','CMG','CB','CHD','CI','CINF','CTAS','CSCO','C','CFG','CTXS','CLX','CME','CMS','KO','CTSH','CL','CMCSA','CMA','DIS','WM','WAT','WEC','WFC','WELL','WST','WDC','WU','WRK','WY','WHR','WMB','WLTW','WYNN','XEL','XRX','XLNX','XYL','YUM','ZBRA','ZBH','ZION','ZTS']


def get_df_columns():
    return ['Ticker', 'Sector', 'Open', 'Close', 'Volume', 'SharesOutstanding']


def get_current_price(ticker):
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


if __name__ == '__main__':
    iex_token = '<enter_token>'

    yfinance_df = pandas.DataFrame([], columns=get_df_columns())
    for ticker in get_tickers():
        tickers = yf.Tickers(ticker)
        print(tickers.tickers[0].info)

        yfinance_df = yfinance_df.append({'Ticker': tickers.tickers[0].ticker.upper(), 'Name': tickers.tickers[0].info['shortName'],
                                          'Sector': tickers.tickers[0].info['sector'],
                        'Open': tickers.tickers[0].info['open'], 'Close': get_current_price(tickers.tickers[0]),
                        'Volume':tickers.tickers[0].info['volume'],
                        'SharesOutstanding':tickers.tickers[0].info['sharesOutstanding']}, ignore_index=True)



    iexfinance_df = pandas.DataFrame([], columns=get_df_columns())
    for ticker in get_tickers():
        iex_stock_info = Stock(ticker, TOKEN=iex_token)
        iexfinance_df = iexfinance_df.append({'Ticker': ticker.upper(), 'Name': iex_stock_info.get_company_name(),
                                              'Sector': iex_stock_info.get_sector(),
                        'Open': iex_stock_info.get_previous_day_prices()['open'][0], 'Close': iex_stock_info.get_previous_day_prices()['close'][0],
                        'Volume': iex_stock_info.get_previous_day_prices()['volume'][0],
                        'SharesOutstanding': iex_stock_info.get_shares_outstanding()}, ignore_index=True)


    yfinance_df.to_csv('./yfinance.csv', index=False)
    iexfinance_df.to_csv('./iexfinance.csv', index=False)

