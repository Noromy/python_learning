class Chef:

    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes a special dish")

class ChineseChef(Chef): # Inherits from Chef

    def make_salad(self):
        print("The chef makes a Chinese salad")

    def make_special_dish(self):
        print("The chef makes a Chinese special dish")
    
    def make_chicken(self):
        print("The chef makes chicken Tiren")

