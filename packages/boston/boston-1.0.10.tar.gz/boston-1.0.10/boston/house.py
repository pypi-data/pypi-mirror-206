import pandas as pd
import os

def load_boston():
  class __Boston:
    def __init__(self):
      abs_path = os.path.abspath(__file__)
      path = os.path.dirname(abs_path)
      filename = "boston_house_prices.csv"
      df = pd.read_csv(os.path.join(path, 'resources', filename), header=0)
      self.data = df.drop('MEDV', axis=1).values
      self.target = df['MEDV'].values
      self.feature_names = df.columns.values.tolist()
  return __Boston()


