from models.slot import Slot

class Ticket:
    
    _all_tickets = {}
    
    def __init__(self, vehicle_number, slot_id):
        self.vehicle_number = vehicle_number
        self.slot_id = slot_id
        self.ticket_id = f"{vehicle_number}{slot_id}"
    
    @classmethod
    def create_ticket(cls, vehicle_number, slot_id):
        ticket = Ticket(vehicle_number, slot_id)
        cls._all_tickets[ticket.ticket_id] = ticket
        return ticket
    
    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        return cls._all_tickets[ticket_id]
    
    def delete(self):
        del self._all_tickets[self.ticket_id]
    