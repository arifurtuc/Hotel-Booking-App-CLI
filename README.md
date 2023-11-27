# What is this project?

This Python project simulates a hotel booking system with added credit card authentication features.

## Overview

1. **Initialization:**
   - The system reads hotel information from `data/hotels.csv`.
   - Credit card details are read from `data/cards.csv` and `data/card_security.csv`.

2. **Hotel Booking:**
   - The system displays a list of available hotels.
   - Asks for user input for the hotel ID.
   - Checks for hotel availability and credit card validation.

3. **Credit Card Validation:**
   - Uses the `CreditCard` and `SecureCreditCard` classes to validate card details.
   - `SecureCreditCard` performs an additional step by authenticating the card with a password.

4. **Reservation Confirmation:**
   - Generates a reservation confirmation message upon successful booking and authentication.

