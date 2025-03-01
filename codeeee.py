class Customer:
    def __init__(self, customer_id, name, contact, address):
        self.__customer_id = customer_id
        self.__name = name
        self.__contact = contact
        self.__address = address
    
    def get_customer_details(self):
        """Returns customer details as a formatted string."""
        return f"Customer: {self.__name}, \nContact: {self.__contact}, \nAddress: {self.__address}"


class Order:
    def __init__(self, order_id, reference_number, customer, delivery_date, delivery_method, weight):
        self.__order_id = order_id
        self.__reference_number = reference_number
        self.__customer = customer
        self.__delivery_date = delivery_date
        self.__delivery_method = delivery_method
        self.__weight = weight
        self.__items = []
    
    def add_item(self, item):
        """Adds an item to the order."""
        self.__items.append(item)
    
    def get_order_summary(self):
        """Returns a formatted order summary including all items."""
        summary = f"Order ID: {self.__order_id}, \nReference Number: {self.__reference_number}, \nDelivery Date: {self.__delivery_date}, \nMethod: {self.__delivery_method}, \nWeight: {self.__weight}kg\n"
        summary += "\n\nItems:\n"
        for item in self.__items:
            summary += item.get_item_details() + "\n"
        return summary


class Item:
    def __init__(self, item_code, description, quantity, unit_price):
        self.__item_code = item_code
        self.__description = description
        self.__quantity = quantity
        self.__unit_price = unit_price
    
    def get_item_details(self):
        """Returns item details including item code."""
        return f"Item Code: {self.__item_code}, Description: {self.__description}, Qty: {self.__quantity}, Unit Price: AED {self.__unit_price}, Total: AED {self.__quantity * self.__unit_price}"


class DeliveryStaff:
    def __init__(self, staff_id, name, phone_number):
        self.__staff_id = staff_id
        self.__name = name
        self.__phone_number = phone_number
    
    def get_staff_details(self):
        """Returns delivery staff details."""
        return f"Delivery Staff: {self.__name}, Contact: {self.__phone_number}"


# Example Usage
customer = Customer(101, "Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE")
order = Order("DEL123456789", "DN-2025-001", customer, "January 25, 2025", "Courier", 7)

# Adding all 4 items as per sample output
item1 = Item("ITM001", "Wireless Keyboard", 1, 100.00)
item2 = Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00)
item3 = Item("ITM003", "Laptop Cooling Pad", 1, 120.00)
item4 = Item("ITM004", "Camera Lock", 3, 15.00)

order.add_item(item1)
order.add_item(item2)
order.add_item(item3)
order.add_item(item4)

delivery_staff = DeliveryStaff(201, "John Doe", "+971501234567")

# Printing details
print("Recipient Details: ")
print(customer.get_customer_details())

print("\nDelivery Information:")
print(order.get_order_summary())

print(delivery_staff.get_staff_details())