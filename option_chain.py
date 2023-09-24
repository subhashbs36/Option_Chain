import requests
import pandas as pd
import xlwings as xw 
import time as tm

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

headers = {"Accept-Encoding":"gzip, deflate, br",
           "Accept-Language":"en-US,en;q=0.9",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

session = requests.Session()
data  = session.get(url,headers=headers).json()["records"]["data"]

ocdata = []

for i in data:
    for j,k in i.items():
        if j == 'CE' or j =='PE':
            info = k
            info["instrument_type"] = j
            ocdata.append(info)       



df = pd.DataFrame(data
)


print(df.head)