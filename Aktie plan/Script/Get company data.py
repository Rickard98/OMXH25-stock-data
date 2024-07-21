#!/usr/bin/env python
# coding: utf-8

# In[14]:


import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta


# In[21]:


# Define OMX Helsinki 25 stock symbols
omxh25_symbols = [
    'NESTE.HE', 'KNEBV.HE', 'FORTUM.HE', 'NDA-FI.HE', 'UPM.HE',
    'STERV.HE', 'MOCORP.HE', 'SAMPO.HE', 'KESKOA.HE', 'NOKIA.HE',
    'WRT1V.HE', 'TELIA1.HE', 'VALMT.HE', 'OUT1V.HE', 'ELISA.HE',
    'HUH1V.HE', 'KCR.HE', 'CGCBV.HE', 'AMEAS.HE', 'YTY1V.HE',
    'FSKRS.HE', 'CAPMAN.HE', 'QTCOM.HE', 'UNR1V.HE', 'KOJAMO.HE'
]


# In[32]:


# Define the end date as today
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = '2006-01-01'

# Create an empty dictionary to store stock data for each company
omxh25_data = {}
failed_symbols = []


# In[33]:


# Iterate through symbols and attempt to retrieve data
for symbol in omxh25_symbols:
    try:
        # Attempt to retrieve data with a start date one year ago
   #     start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        
        # Check if the retrieved DataFrame is not empty
        if not stock_data.empty:
            omxh25_data[symbol] = stock_data
        else:
            print(f"No data found for {symbol}")
            failed_symbols.append(symbol)
    except Exception as e:
        print(f"Failed to download data for {symbol}: {e}")
        failed_symbols.append(symbol)

print("Symbols that failed to download data:", failed_symbols)


# In[34]:


# Save data for each company to separate Excel files
folder_path = r'C:\Users\Ricks\OneDrive\Skrivbord\Aktie plan\Aktie data\\'  # Modify this path as needed

for symbol, data in omxh25_data.items():
    file_path = f"{folder_path}{symbol}.xlsx"
    data.to_excel(file_path)
    print(f"Data exported to {file_path} successfully!")


# In[36]:


# Symbol for Wärtsilä Corporation
company_symbol = 'NESTE.HE'

# Fetch the stock data for Wärtsilä Corporation
data = omxh25_data[company_symbol]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price')
plt.title('Stock Price for Wärtsilä Corporation (WRT1V.HE)')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




