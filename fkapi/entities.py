""" 
This module implements all the domain objects that are finally consumable by
the API clients. 
"""

class Product():
  """ 
  A listed product on flipkart.com. The product maps to a SKU (shop keeping
  unit) on flipkart.com. 
  """

  def __init__(self, product_id, title, categories, product_brand, product_url,
      image_urls=[], mrp=None, price=None, delivery_time=None,
      in_stock=False, cod_available=False, emi_available=False, offers=[],
      discount=False, cash_back=0):
    """
    An unassuming constructor. The default values are deplorable at best.
    Field names seem descriptive enough. Give me a shout if they aren't.
    """

    self.product_id = product_id
    self.title = title
    self.image_urls = image_urls
    self.mrp = mrp
    self.price = price
    self.product_url = product_url
    self.categories = categories
    self.product_brand = product_brand
    self.delivery_time = delivery_time
    self.in_stock = in_stock
    self.cod_available = cod_available
    self.emi_available = emi_available
    self.offers = offers
    self.discount = discount
    self.cash_back = cash_back


class Offers():
  """
  TODO A listed offer on flipkart.com. Contains details of the offer.
  """
  pass

