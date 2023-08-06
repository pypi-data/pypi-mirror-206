import pandas as pd
from regbot import signal

df = pd.read_csv('../jupyter/regbot_v38_validation.csv')

y_pred = []
def getSignal(rsi_5,rsi_15,grad_sma25):
    return 1 if signal(rsi_5,rsi_15,grad_sma25) > 0.5 else 0


df = df.head(10000) #[df['enter_long'] == 0]
print(df.head())

df['result'] = df.apply(lambda row: getSignal(row['rsi-05'],row['rsi-15'],row['grad-sma-25']), axis=1)

print(df.head())

print(len(df[df['result'] == df['enter_long']]), len(df))
