import streamlit as st
import pandas as pd
from binance import Client
import mplfinance as mpf

client = Client(
    api_key ,
    api_secret)

st.set_option('deprecation.showPyplotGlobalUse', False)

def app():


    st.markdown("""
    Crypto Dashoboard to monitor how the market is moving and your favorite coins.
    Visually show data on Crypto(BTC,DOGE & ETH)
    """)

    tickers = client.get_all_tickers()
    tickers
    #st.write(tickers)

    ticker_df = pd.DataFrame(tickers)
    ticker_df.set_index('symbol', inplace=True)
    st.write(ticker_df.head())

    # order book depth
    #depth = client.get_order_book(symbol='BTCUSD')
    #depth_df = pd.DataFrame(depth)
    #st.write(depth_df.head())

    historical = client.get_historical_klines('ETHBTC', Client.KLINE_INTERVAL_1DAY, '1 Jan 2021')
    hist_df = pd.DataFrame(historical)
    hist_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']
    
    hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time']/ 1000, unit='s')
    hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time']/ 1000, unit='s')

    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'TB Base Volume', 'TB Quote Volume']

    hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)

    hist_df.dtypes
    st.write(hist_df.head())

    f = mpf.plot(hist_df.set_index('Close Time'), type='candle', style='charles', volume=True, title='ETHBTC', mav=(10,20))
    st.pyplot(f)
    #timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')

    #hist_df.shape

    #bars = client.get_historical_klines('BTCUSDT', '1d', timestamp, limit = 356)

    #btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
    #btc_df.set_index('date', inplace=True)
    #print(btc_df.head())
