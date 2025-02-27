# Write a class Train which has methods to book a ticket, get Status (no of seats) and get fare information of 
# trains running under American Railways.
"""
1 2 3 4 5 6 7 8 9 10
"""
class Train:
    def __init__(self, passenger_name, train_name, available_seats, fare):
        self.passenger_name = passenger_name
        self.train_name = train_name
        self.available_seats = available_seats
        self.fare = fare
        self.tickets_booked = 0  
        
    def get_status(self):
        print(f"Welcome to {self.train_name}!")
        print(f"Available seats: {self.available_seats}\n")
    
    def get_fare_info(self):
        print(f"The fare for {self.train_name} is ${self.fare} per ticket.\n")

    def book_ticket(self):
        print(f"Booking ticket for {self.passenger_name}...")
        if self.available_seats > 0:
            self.available_seats -= 1
            self.tickets_booked += 1
            print(f"Ticket successfully booked for {self.passenger_name}!\n")
        else:
            print(f"Sorry, no seats are available. Please try again later.\n")

    def cancel_ticket(self):
        print(f"Canceling ticket for {self.passenger_name}...")
        if self.tickets_booked > 0:
            self.available_seats += 1
            self.tickets_booked -= 1
            print(f"Ticket canceled successfully. Available seats: {self.available_seats}\n")
        else:
            print(f"No tickets booked under {self.passenger_name}'s name to cancel.\n")

    def __str__(self):
        return f"Train({self.train_name}): Passenger - {self.passenger_name}, Seats Available - {self.available_seats}, Fare - ${self.fare}"


passenger = Train("Palsang", "Virginia Metro Station", 2, 2.45)
passenger.get_status()
passenger.get_fare_info()
passenger.book_ticket()
passenger.book_ticket()
passenger.cancel_ticket()
passenger.book_ticket()
print(passenger) 
