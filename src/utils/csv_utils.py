import pandas as pd

class CsvUtils:
  @staticmethod
  def read_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

  @staticmethod
  def write_to_csv(file_path: str, data: pd.DataFrame):
    data.to_csv(file_path, index=False)