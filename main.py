import pandas

# Reading hotel information from a CSV file
df = pandas.read_csv("data/hotels.csv", dtype={"id": str})

# Reading credit card info from CSV file
df_cards = pandas.read_csv("data/cards.csv",
                           dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("data/card_security.csv",
                                    dtype=str)


# Represents a hotel entity with booking and availability functionalities
class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book the hotel by updating its availability in the DataFrame and
        saving it back to the CSV file"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("data/hotels.csv", index=False)

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
        """Generate and return a confirmation message for the reservation at
        the selected hotel"""
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        """Initialize CreditCard object with the provided card number"""
        self.number = number

    def validate(self, expiration, cvc, holder):
        """Validate the credit card based on the provided details."""
        card_data = {"number": self.number,
                     "expiration": expiration,
                     "cvc": cvc,
                     "holder": holder}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        """Authenticate the secure credit card with the given password."""
        password = df_cards_security.loc[
            df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


# Displaying the list if hotels
print(df)

# Asking for user input: hotel ID
hotel_ID = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_ID)

# Checking if the selected hotel is available
if hotel.available():
    # Simulate credit card validation
    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26",
                            cvc="123",
                            holder="JOHN SMITH"):
        if credit_card.authenticate(given_password="mypass"):
            # Proceed with hotel booking and reservation confirmation
            hotel.book()

            # Ask for user input: customer name
            name = input("Enter your name: ")

            # Generate a reservation confirmation at the selected hotel
            reservation_confirmation = Reservation(customer_name=name,
                                                   hotel_object=hotel)
            print(reservation_confirmation.generate())
        else:
            print("Credit card authentication failed!")
    else:
        print("There is a problem with your payment!")
else:
    print("Hotel is not available!")
