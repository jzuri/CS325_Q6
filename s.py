# Write a program on how you would refactor the Order class to follow the Single Responsibility Principle

class Order:
  def __init__(self, customer_info, items, shipping_address):
    self.customer_info = customer_info
    self.items = items
    self.shipping_address = shipping_address
    

