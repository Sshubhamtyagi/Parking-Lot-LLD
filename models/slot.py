from enum import Enum

class Slot:
    
    _all_slots = {}

    class SlotType(Enum):
        TRUCK = 1
        CAR = 2
        BIKE = 3
    
    class Status(Enum):
        AVAILABLE = 'AVAILABLE'
        BOOKED = 'BOOKED'
    
    def __init__(self, parking_lot_id, floor, slot_type, slot_id) -> None:
        self.parking_lot_id = parking_lot_id
        self.floor = floor
        self.slot_type = slot_type
        self.slot_id = slot_id
        self.status = Slot.Status.AVAILABLE.name
    
    @classmethod
    def create_slot(cls, parking_lot_id, floor, slot_type, slot_id):
        slot = Slot(parking_lot_id, floor, slot_type, slot_id)
        cls._all_slots[slot_id] = slot
        return slot
    
    @classmethod
    def get_slot_by_id(cls, slot_id):
        return cls._all_slots[slot_id]
    
    @classmethod
    def get_all_slots(cls):
        return cls._all_slots
    
    def get_slot_details(self):
        return {
            'parking_lot_id': self.parking_lot_id,
            'floor': self.floor,
            'slot_type': self.slot_type,
            'slot_id': self.slot_id
        }
    
    @classmethod
    def get_slots_by_parking_lot(cls, parking_lot_id):
        for _, slot in cls.get_all_slots().items():
            if parking_lot_id == slot.parking_lot_id:
                yield slot

    @classmethod
    def get_available_slots(cls, parking_lot_id):
        result = []
        for slot in cls.get_slots_by_parking_lot(parking_lot_id):
            if slot.status == Slot.Status.AVAILABLE.name:
                result.append(slot)
        return result
    
    
    @classmethod
    def get_booked_slots(cls, parking_lot_id):
        result = []
        for slot in cls.get_slots_by_parking_lot(parking_lot_id):
            if slot.status == Slot.Status.BOOKED.name:
                result.append(slot)
        return result
    
    def book(self):
        self.status = Slot.Status.BOOKED.name
        self._all_slots[self.slot_id] = self
        return self
    
    def unbook(self):
        self.status = Slot.Status.AVAILABLE.name
        self._all_slots[self.slot_id] = self
        return self
    
    
    