def pr1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(self.restaurant_name)
            print(self.cuisine_type)

        def open_restaurant(self):
            print('Ресторан открыт!')

    newRestaurant = Restaurant("Little Italy", "Итальянская кухня")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()


def pr2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(self.restaurant_name)
            print(self.cuisine_type, '\n')

        def open_restaurant(self):
            print('Ресторан открыт!')

    Restaurant1 = Restaurant("Made in China", "Китайская кухня")
    Restaurant1.describe_restaurant()
    Restaurant2 = Restaurant("Француз", "Французская кухня")
    Restaurant2.describe_restaurant()
    Restaurant3 = Restaurant("American food", "Американская кухня")
    Restaurant3.describe_restaurant()


def pr3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_reyt):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.restaurant_reyt = restaurant_reyt

        def describe_restaurant(self):
            print(self.restaurant_name)
            print(self.cuisine_type)

        def obnov_reyt(self):
            print(self.restaurant_reyt)
            self.restaurant_reyt = input()
            print(self.restaurant_reyt)

        def open_restaurant(self):
            print('Ресторан открыт!')

    Restaurant1 = Restaurant("цвфвфцв", "dwadawdwa", "0")
    Restaurant1.obnov_reyt()


pr3()
