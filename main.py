import pandas

# Reading hotel information from a CSV file
df = pandas.read_csv("hotels.csv", dtype={"id": str})


# Represents a hotel entity with booking and availability functionalities
class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book the hotel by updating its availability in the DataFrame and
        saving it back to the CSV file"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available based on its availability status
        in the DataFrame"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


# Represents a reservation for a customer at a hotel
class Reservation:
    def __init__(self, customer_name, hotel):
        pass

    def generate(self):
        pass


# Displaying the contents of the loaded CSV data
print(df)

# Asking for user input: hotel ID
hotel_ID = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_ID)

# Checking if the selected hotel is available
if hotel.available():
    # If available, proceed with the booking process
    hotel.book()

    # Ask for user input: customer name
    name = input("Enter your name: ")

    # Generate a reservation confirmation at the selected hotel
    reservation_confirmation = Reservation(name, hotel)
    print(reservation_confirmation.generate())
