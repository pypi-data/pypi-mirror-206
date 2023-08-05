import pandas as pd
from importlib import resources



def load_boston():
  class __Boston:
    def __init__(self):
      filename = "boston_house_prices.csv"
      path = resources.path("boston", filename)

      df = pd.read_csv(path, header=1)
      self.data = df.drop('MEDV', axis=1).values
      self.target = df['MEDV'].values
      self.feature_names = df.columns.values.tolist()
  return __Boston()


