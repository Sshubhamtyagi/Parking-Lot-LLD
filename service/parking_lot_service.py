from models.parking_lot import ParkingLot
from models.slot import Slot
from models.ticket import Ticket


class ParkingLotService:
    def __init__(self, parking_lot: ParkingLot) -> None:
        self.parking_lot = parking_lot

    def _create_booking(self, vehicle_number, slot_id):
        ticket = Ticket.create_ticket(vehicle_number, slot_id)
        slot = Slot.get_slot_by_id(slot_id)
        slot.book()
        return ticket.ticket_id

    def park_vehicle(self, vehicle_type, vehicle_number):
        all_available_slots = self.parking_lot.get_available_slots()
        for slot in all_available_slots:
            if slot.slot_type == vehicle_type and slot.status == Slot.Status.AVAILABLE.name:
                ticket_id = self._create_booking(vehicle_number, slot.slot_id)
                return ticket_id
        
    def unpark_vehicle(self, ticket_id):
        ticket = Ticket.get_ticket_by_id(ticket_id)
        slot = Slot.get_slot_by_id(ticket.slot_id)
        slot.unbook()
        ticket.delete()
        return True
    