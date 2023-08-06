# Evx regpredict mlbot

This is a simplified version of [evxpredictor](https://pypi.org/project/evxpredictor/) package used to generate buy and sell signals for crypto and conventional stock markets based on the excess volume indicator(EVX). EVX is a concept where the bid-ask spread is estimated inherently from current market prices. 

You can read more about Evx in the whitepaper [here](https://www.researchgate.net/publication/345313655_DeFiPaper)  
# Installation
Install regpredict with `python3 -m pip install regpredict`  
# Usage

In your python script simply import the module and use as follows:

```  
from regpredict.regbot import signal
print(signal(20,65,85,25,68,23,0.25))
```
The above methods take an assets volume, rsi5,rsi15,sma5,sma7,sma25,vc-gradient obtained from EVX, and the two-period gradient to sma25 of the asset based on the time interval you have chosen. A zero classification output would instruct the user to sell, while one output means don't sell or buy if the asset is not already present in the orders.  

# Testing an entire dataframe
Testing of a dataframe for correct buy, sell signals is as simple as applying the function as follows:  

```
import pandas as pd
from regbot import signal
#from regpredict.regbot import signal
df = pd.read_csv('../path/to/your_validation.csv')

y_pred = []
def getSignal(vol,rsi_5,rsi_15,sma_5,sma_7,sma_25,vc_grad,grad_sma25,vol_grad):
    return 0 if signal(vol,rsi_5,rsi_15,sma_5,sma_7,sma_25,vc_grad grad_sma25,vol_grad) <= thr else 1

Where thr is a user defined threshold.


df = df[df['enter_long'] == 1]
print(df.head())

df['result'] = df.apply(lambda row: getSignal(row['volume'],row['rsi-05'],row['rsi-15'],row['sma-05'],row['sma-07'],row['sma-25'],row['vc-grad'],row['grad_sma25'],row['vol-grad'] ), axis=1)

print(df.head())

print(len(df[df['result'] == df['enter_long']]), len(df))

```

Your original data must already have some presumed 'buy' signal.

# Warning
This is not financial advise. Regpredict is entirely on its preliminary stages. Use it at your own risk.
