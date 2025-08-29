# -----------------------------
# Assignment 1: Design Your Own Class
# -----------------------------

# Base class: Gadget
class Gadget:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_info(self):
        return f"Gadget: {self.brand} {self.model}"

# Subclass: Smartphone inherits from Gadget
class Smartphone(Gadget):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Call parent constructor
        self.os = os
        self.storage = storage
    
    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."
    
    def take_photo(self):
        return f"{self.brand} {self.model} is taking a photo 📸"
    
    # Method overriding (polymorphism with parent)
    def show_info(self):
        return f"Smartphone: {self.brand} {self.model}, OS: {self.os}, Storage: {self.storage}GB"


# Example usage
phone1 = Smartphone("Apple", "iPhone 15", "iOS", 256)
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", 512)

print(phone1.show_info())
print(phone1.make_call("08012345678"))
print(phone2.take_photo())
