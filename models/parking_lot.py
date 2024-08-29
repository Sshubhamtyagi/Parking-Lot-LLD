from models.slot import Slot
import uuid

class ParkingLot:
    def __init__(self, total_floors : int, no_of_slots_per_floor: int) -> None:
        self.parking_lot_id = str(uuid.uuid4())
        self.total_floors = total_floors
        self.no_of_slots_per_floor = no_of_slots_per_floor
        self._create_slots()
    
    @classmethod
    def create_parking_lot(cls, total_floors : int, no_of_slots_per_floor: int):
        parking_lot = ParkingLot(total_floors, no_of_slots_per_floor)
        return parking_lot

    def _create_slots(self):
        for i in range(self.total_floors):
            for j in range(self.no_of_slots_per_floor):
                slot_id = str(uuid.uuid4())
                slot_type = Slot.SlotType.CAR.name
                if j == 0:
                    slot_type = Slot.SlotType.TRUCK.name
                elif 1 <= j <= 2:
                    slot_type = Slot.SlotType.CAR.name
                Slot.create_slot(self.parking_lot_id, i, slot_type, slot_id)
    
    def get_all_slots(self):
        return Slot.get_slots_by_parking_lot(self.parking_lot_id)
    
    def get_available_slots(self):
        return Slot.get_available_slots(self.parking_lot_id)

    def show_slot_details(self):
        for slot in self.get_all_slots():
            print(slot.get_slot_details())