#!/usr/bin/env python3
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import joblib
import numpy as np
from pkg_resources import resource_filename
import fire


class Regbot:
  reg_model_path = resource_filename(__name__, 'minute_model.h5')
  model_scaler_path = resource_filename(__name__, 'minutescaler.gz')
  #thr = 0.5 uncomment this and return
  #(cls.loadmodel().predict_proba(scalledInput)[:,1] >= cls.thr).astype(int)[0]
  # in the buySignalGenerator to use static thresholds

  def __init__(self,*args):
  	pass



  @classmethod
  def loadmodel(cls):
    try:
      return joblib.load(open(f'{cls.reg_model_path}', 'rb'))
    except Exception as e:
      return {
        'Error': e
      }


  @classmethod
  def prepareInput(cls,rsi_5,rsi_15,grad_sma25):
    try:
      testdata = np.array([[rsi_5,rsi_15,grad_sma25]])
      scaler = joblib.load(f'{cls.model_scaler_path}')
      testdata = scaler.transform(testdata)

      return testdata
    except Exception as e:
      return {
        'Error': e
      }


  @classmethod
  def buySignalGenerator(cls,rsi_5,rsi_15,grad_sma25):
    scalledInput = cls.prepareInput(rsi_5,rsi_15,grad_sma25)
    try:
      return (cls.loadmodel().predict_proba(scalledInput)[:,1])[0]
    except Exception as e:
      return {
        'Error': e
      }



def signal(rsi_5,rsi_15,grad_sma25):
  try:
    return Regbot.buySignalGenerator(rsi_5,rsi_15,grad_sma25)
  except Exception as e:
    return {
      'Error': e
    }


if __name__ == '__main__':
  fire.Fire(signal)
