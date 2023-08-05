import pandas as pd
from sklearn.utils import Bunch
import os

def load_boston():
  abs_path = os.path.abspath(__file__)
  path = os.path.dirname(abs_path)
  filename = "boston_house_prices.csv"
  df = pd.read_csv(os.path.join(path, 'resources', filename), header=0)

  bunch = Bunch(data=df.drop('MEDV', axis=1).values, 
                target=df['MEDV'].values,
                feature_names = df.columns.values.tolist())
  return bunch



