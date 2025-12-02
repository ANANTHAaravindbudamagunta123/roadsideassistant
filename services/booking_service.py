class BookingService:
    def __init__(self):
        self.bookings = []
        self.booking_id_counter = 1
    
    def create_booking(self, booking_data):
        booking = {
            'id': self.booking_id_counter,
            'username': booking_data['username'],
            'vehicle': booking_data['vehicle'],
            'issue': booking_data['issue'],
            'customIssue': booking_data.get('customIssue', ''),
            'serviceCenter': booking_data['serviceCenter'],
            'userLatitude': booking_data['userLatitude'],
            'userLongitude': booking_data['userLongitude'],
            'status': 'Pending'
        }
        self.bookings.append(booking)
        self.booking_id_counter += 1
        return booking
    
    def get_bookings_by_username(self, username):
        return [b for b in self.bookings if b['username'] == username]
    
    def get_booking_by_id(self, booking_id):
        for booking in self.bookings:
            if booking['id'] == booking_id:
                return booking
        return None
    
    def update_booking_status(self, booking_id, status):
        booking = self.get_booking_by_id(booking_id)
        if booking:
            booking['status'] = status
