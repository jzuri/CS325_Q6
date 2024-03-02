# Write a program on how you would refactor the Order class to follow the Single Responsibility Principle

class Order:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address
    
    def total_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.price
        return total_cost

    def validate_order(self):
        print("Validating order")
      
    def send_confirmation(self):
        print("Confirmation for Order")
      
    def update_inventory(self):
        print("Updating store inventory")

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class OrderValidator:
    def order_validation(self, order):
        print("Validate Order")

class EmailSender:
    def order_confirmation(self, order):
        print("Send Order Confirmation")

class InventoryManager:
    def update_inventory(self, order):
        print("Update Store inventory")

    


