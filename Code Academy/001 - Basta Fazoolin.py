brunch = {
    "pancakes": 7.50,
    "waffles": 9.00,
    "burger": 11.00,
    "home fries": 4.50,
    "coffee": 1.50,
    "espresso": 3.00,
    "tea": 1.00,
    "mimosa": 10.50,
    "orange juice": 3.50,
}
early_bird = {
    "salumeria plate": 8.00,
    "salad and breadsticks (serves 2, no refills)": 14.00,
    "pizza with quattro formaggi": 9.00,
    "duck ragu": 17.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 1.50,
    "espresso": 3.00,
}
dinner = {
    "crostini with eggplant caponata": 13.00,
    "caesar salad": 16.00,
    "pizza with quattro formaggi": 11.00,
    "duck ragu": 19.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 2.00,
    "espresso": 3.00,
}
kids = {
    "chicken nuggets": 6.50,
    "fusilli with wild mushrooms": 12.00,
    "apple juice": 3.00,
}


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} menu is available from {start_time} to {end_time}".format(
            name=self.name, start_time=self.start_time, end_time=self.end_time
        )

    def calculate_bill(self, purchased_items):
        total_price = 0
        for i in purchased_items:
            if i in self.items:
                total_price += self.items[i]
        return total_price


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        print("The restaurant address is {address}".format(address=self.address))

    def available_menus(self, time):
        available_menus = []
        for m in self.menus:
            if m.start_time <= time <= m.end_time:
                available_menus.append(m)
        return available_menus


brunch = Menu("brunch", brunch, 1100, 1600)
early_bird = Menu("early bird", early_bird, 1500, 1800)
dinner = Menu("dinner", dinner, 1700, 2300)
kids = Menu("kids", kids, 1100, 2100)
# print(brunch)
# print(brunch.calculate_bill( ['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise(
    "12 East Mulberry Street", [brunch, early_bird, dinner, kids]
)
print(flagship_store.available_menus(1200))
