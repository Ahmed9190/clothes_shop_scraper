import json

class FileUtils:
  @staticmethod
  def save_to_file(file_name: str, data: dict):
    with open(file_name, 'w', encoding='utf-8') as file:
      json.dump(data, file, indent=2)

  @staticmethod
  def read_from_file(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
      return json.load(file)