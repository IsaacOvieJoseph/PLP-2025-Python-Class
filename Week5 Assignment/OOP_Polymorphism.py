# -----------------------------
# Activity 2: Polymorphism Challenge
# -----------------------------

class Vehicle:
    def move(self):
        return "Moving in some way..."

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())