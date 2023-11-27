import pandas

# Reading hotel information from a CSV file
df = pandas.read_csv("hotels.csv", dtype={"id": str})


# Represents a hotel entity with booking and availability functionalities
class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

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
    def __init__(self, customer_name, hotel_object):
        """Initialize a Reservation object with customer name and the
            corresponding hotel object"""
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        """Generate and return a confirmation message for the reservation at the
            selected hotel"""
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


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
    reservation_confirmation = Reservation(customer_name=name,
                                           hotel_object=hotel)
    print(reservation_confirmation.generate())
else:
    print("Hotel is not available!")