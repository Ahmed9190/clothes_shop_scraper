class Product:
  _name: str
  _price: float
  _image: str
  def __init__(self, name:str, price:float, image:str):
    self._name = name
    self._price = price
    self._image = image

  def get_name(self)-> str:
    return self._name

  def get_price(self) -> float:
    return self._price

  def get_image(self) -> str:
    return self._image

  def __str__(self) -> str:
    return f"Name: {self._name}, Price: {self._price}, Image: {self._image}"

  def to_dict(self)-> dict:
    return {'Product Name': self._name, 'Product Price': self._price, 'Product Image': self._image}
