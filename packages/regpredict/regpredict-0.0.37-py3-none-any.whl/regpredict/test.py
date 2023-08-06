import pandas as pd
from regbot import signal

df = pd.read_csv('../jupyter/regbot_v37_validation.csv')

y_pred = []
def getSignal(vol,rsi_5,rsi_15,sma_5,sma_7,sma_25,vc_grad,grad_sma25,vol_grad):
    return signal(vol,rsi_5,rsi_15,sma_5,sma_7,sma_25,vc_grad,grad_sma25,vol_grad)


df = df.head(10000) #[df['enter_long'] == 0]
print(df.head())

df['result'] = df.apply(lambda row: getSignal(row['volume'],row['rsi-05'],row['rsi-15'],row['sma-05'],row['sma-07'],row['sma-25'],row['vc-grad'],row['grad-sma-25'],row['vol-grad'] ), axis=1)

print(df.head())

print(len(df[df['result'] == df['enter_long']]), len(df))
