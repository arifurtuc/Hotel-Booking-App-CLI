import pandas

# Reading hotel information from a CSV file
df = pandas.read_csv("hotels.csv")


# Represents a hotel entity with booking and availability functionalities
class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass


# Represents a reservation for a customer at a hotel
class Reservation:
    def __init__(self, customer_name, hotel):
        pass

    def generate(self):
        pass


# Displaying the contents of the loaded CSV data
print(df)

# Asking for user input: hotel ID
id = input("Enter the ID of the hotel: ")
hotel = Hotel(id)

# Checking if the selected hotel is available
if hotel.available():
    hotel.book()

    # Ask for user input: customer name
    name = input("Enter your name: ")

    # Generate a reservation confirmation at the selected hotel
    reservation_confirmation = Reservation(name, hotel)
    print(reservation_confirmation.generate())
